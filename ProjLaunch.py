from pathlib import Path
import json
import sys

config_dir = Path.home() / ".projlauncher"
config_file = config_dir / "projects.json"


def get_config():

    config_dir.mkdir(exist_ok=True)

    if not config_file.exists():
        with open(config_file, "w") as f:
            json.dump({"projects": {}}, f, indent=4)

    with open(config_file, "r") as f:
        return json.load(f)


def save_config(config):
    with open(config_file, "w") as f:
        json.dump(config, f, indent=4)


def add_project():
    config = get_config()
    name = input("Project name > ")

    if name in config["projects"]:
        print("Project already exists.")
        return

    path = input("Project Path > ")

    config["projects"][name] = {
        "path": path,
        "commands": [],
        "urls": []
    }

    save_config(config)


if __name__ == "__main__":
    args = sys.argv

    if sys.argv[1] == "add":
        add_project()
    elif sys.argv[1] == "launch":
        pass
