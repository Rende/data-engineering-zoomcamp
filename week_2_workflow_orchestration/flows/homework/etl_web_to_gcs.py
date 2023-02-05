from pathlib import Path 
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket


@task(retries=3)
def fetch(dataset_url:str) -> pd.DataFrame:
    """ Read taxi data from web into pandas DataFrame """
    df = pd.read_csv(dataset_url)
    return df 

@task(log_prints=True)
def clean(df:pd.DataFrame, color:str) -> pd.DataFrame:
    """Fix dtype issues"""
    # for the green dataset
    if color=="green":
        df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
        df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
    else:
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    
    print(f"rows: {len(df)}")
    return df

@task
def write_local(df: pd.DataFrame, color:str, dataset_file:str) -> Path:
    """Write DataFrame out as Parquet file"""
    path = Path(f"data/{color}/{dataset_file}.parquet")
    df.to_parquet(path, compression="gzip")
    return path

@task()
def write_gcs(path: Path) -> None:
    """Uploading local parquet file to GCS"""
    gcs_block = GcsBucket.load("zoom-gcs-block")
    gcs_block.upload_from_path(
        from_path=f"{path}",
        to_path=path
    )
    return
# first question
# https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-01.csv.gz

@flow(log_prints=True)
def etl_web_to_gcs(color:str, month:int, year:int) -> None:
    """ The main ETL function"""
    dataset_file = f"{color}_tripdata_{year}-{month:02}"
    dataset_url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/{dataset_file}.csv.gz"

    df = fetch(dataset_url)
    df_clean = clean(df, color)
    path = write_local(df_clean, color, dataset_file)
    print(path)
    write_gcs(path)

@flow(log_prints=True)
def etl_parent_flow(months : list[int] = [2,3], year: int =2019, color:str = "yellow"):
    for month in months:
        etl_web_to_gcs(color, month, year)

if __name__ == '__main__':
    etl_parent_flow()