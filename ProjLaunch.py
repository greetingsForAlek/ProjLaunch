from pathlib import Path
import json
import sys
import subprocess
import webbrowser

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

    commands_input = input("Would you like to run any commands upon opening project? seperate the commands with commas and no spaces between commands. > ")

    commands = commands_input.split(",")
    print(commands)

    urls_input = input("Would you like to open any URLs upon opening this project? Please seperate them with commas and no spaces between URLs. > ")

    urls = urls_input.split(",")
    print(urls)

    config["projects"][name] = {
        "path": path,
        "commands": commands,
        "urls": urls
    }

    save_config(config)


def launch_project(project_name):
    config = get_config()

    project = config["projects"].get(project_name)

    if project is None:
        print("Provided project does not exist.")
        return
    
    subprocess.Popen([
        "code",
        project["path"]
    ])

    for command in project["commands"]:
        subprocess.Popen(
            command,
            cwd=project["path"],
            shell=True
        )

    for url in project["urls"]:
        webbrowser.open_new_tab(url)
    



if __name__ == "__main__":
    args = sys.argv

    if sys.argv[1] == "add":
        add_project()
    elif sys.argv[1] == "launch":
        if len(sys.argv) > 2:
            launch_project(sys.argv[2])
        else:
            print("No project argument provided")
            print("command: ProjLaunch launch yourprojectname")
