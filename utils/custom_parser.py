import json
from pathlib import Path

configFile = "automation.json"
configFolder = "config"

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(configFolder).joinpath(configFile)

with open(CONFIG_FILE, "r") as file:
    config = json.load(file)


def getConfig(section, attribute):
    return config[section][attribute]


#getBaseURL("Home_Page","baseURL")