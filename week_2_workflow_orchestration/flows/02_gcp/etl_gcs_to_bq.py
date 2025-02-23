from pathlib import Path 
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials


@task(log_prints=True, retries=3)
def extract_from_gcs(color:str, year: int, month:int) -> Path:
    """ Download trp data from GCS"""
    gcs_path=f"data/{color}/{color}_tripdata_{year}-{month:02}.parquet"
    gcs_block = GcsBucket.load("zoom-gcs-block")
    gcs_block.get_directory(from_path=gcs_path, local_path=f"../gcs/data/")
    return Path(f"../gcs/data/{gcs_path}")


@task(log_prints=True)
def transform_data(path: Path) -> pd.DataFrame:
    df = pd.read_parquet(path)
    print(f"pre: missing passenger count: {df.passenger_count.isna().sum()}")
    df.passenger_count.fillna(0, inplace=True)
    print(f"post: missing passenger count: {df.passenger_count.isna().sum()}")
    return df


@task(log_prints=True)
def write_bq(df: pd.DataFrame) -> None:
    """ Writing to BigQuery with Credentials """
    gcp_credentials_block = GcpCredentials.load("zoom-gcp-creds")

    df.to_gbq(
        destination_table = "dezoomcamp.rides",
        project_id = "de-zoomcamp-2023-375907",
        credentials = gcp_credentials_block.get_credentials_from_service_account(),
        chunksize = 500_000,
        if_exists = "append",
    )

@flow()
def etl_gcs_to_bq(color:str, year:int, month:int):
    """ Main ETL flow to load data into Big Query"""
    
    path = extract_from_gcs(color, year, month)
    df = transform_data(path)
    write_bq(df)

@flow()
def etl_parent_flow(months : list[int] = [1,2,3], year: int =2020, color:str = "yellow"):
    for month in months:
        etl_gcs_to_bq(color, year, month)


if __name__=="__main__":
    etl_gcs_to_bq()