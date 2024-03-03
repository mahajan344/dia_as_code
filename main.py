from diagrams import Diagram, Cluster
from diagrams.programming.flowchart import Action
from diagrams.generic.blank import Blank
from diagrams.azure.compute import ACR, ContainerInstances
from diagrams.onprem.ci import GithubActions

with Diagram("Git, GitHub, and GitHub Actions Workflow", show=False):
    acr = ACR("ACR")

    with Cluster("Web App"):
        github_repo_web = Blank("GitHub Repo Web")
        github_actions_web = GithubActions("GitHub Actions Web")
        web_app = ContainerInstances("Web App")
        github_repo_web >> github_actions_web >> acr >> web_app

    with Cluster("API 1"):
        github_repo_api1 = Blank("GitHub Repo API 1")
        github_actions_api1 = GithubActions("GitHub Actions API 1")
        api1 = ContainerInstances("API 1")
        github_repo_api1 >> github_actions_api1 >> acr >> api1

    with Cluster("API 2"):
        github_repo_api2 = Blank("GitHub Repo API 2")
        github_actions_api2 = GithubActions("GitHub Actions API 2")
        api2 = ContainerInstances("API 2")
        github_repo_api2 >> github_actions_api2 >> acr >> api2

    with Cluster("API 3"):
        github_repo_api3 = Blank("GitHub Repo API 3")
        github_actions_api3 = GithubActions("GitHub Actions API 3")
        api3 = ContainerInstances("API 3")
        github_repo_api3 >> github_actions_api3 >> acr >> api3