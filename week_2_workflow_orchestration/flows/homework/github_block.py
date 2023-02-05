from prefect.filesystems import GitHub

block = GitHub(
    repository="https://github.com/Rende/data-engineering-zoomcamp/",
)
block.get_directory("week_2_workflow_orchestration/flows/homework/") # specify a subfolder of repo
block.save("main")