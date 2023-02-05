from prefect.filesystems import GitHub

block = GitHub(
    repository="https://github.com/Rende/data-engineering-zoomcamp/",
    access_token=<my_access_token> # only required for private repos
)
block.get_directory("week_2_workflow_orchestration/flows/homework/") # specify a subfolder of repo
block.save("homework")