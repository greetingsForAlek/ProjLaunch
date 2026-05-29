from pathlib import Path
import json

def get_config():
    config_dir = Path.home() / ".projlauncher"
    config_file = config_dir / "projects.json"

    config_dir.mkdir(exist_ok=True)

    if not config_file.exists():
        with open(config_file, "w") as f:
            json.dump({"projects": {}}, f, indent=4)

    with open(config_file, "r") as f:
        return json.load(f)