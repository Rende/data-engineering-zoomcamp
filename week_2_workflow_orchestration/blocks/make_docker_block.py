from prefect.infrastructure.docker import DockerContainer

docker_block = DockerContainer(
    image="aydanrende/prefect:zoom",
    image_pull_policy="ALWAYS",
    auto_remove=True,
)

docker_block.save("docker-block", overwrite=True)