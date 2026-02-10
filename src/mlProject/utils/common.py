import yaml
import os
from pathlib import Path


def read_yaml(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def create_project_structure(config_path):
    config = read_yaml(config_path)

    project_name = config["project"]["name"]
    folders = config["project"]["folders"]
    files = config["project"]["files"]

    # Create project root
    Path(project_name).mkdir(exist_ok=True)

    # Create folders
    for folder in folders:
        folder_path = Path(project_name) / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {folder_path}")

    # Create files
    for file in files:
        file_path = Path(project_name) / file
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch(exist_ok=True)
        print(f"Created file: {file_path}")


# Run
if __name__ == "__main__":
    create_project_structure("project_structure.yaml")
