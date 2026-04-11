import sys
import json
import os

VERSION_PATH = sys.argv[1]

versionInfo = {
    "attributes": {},
    "blocks": {},
    "dimensions": {},
    "entitys": {},
    "gooeys": {},
    "items": {},
    "processes": {},
    "recipes": {},
    "tags": {}
}

def crash(num):
    print(f"Crash: Error code '{num}'")
    return False

def setUpROM():
    for folder_name in ["blocks", "dimensions", "entitys", "recipes", "tags"]:

        folder_path = os.path.join(VERSION_PATH, "src", folder_name)

        if not os.path.isdir(folder_path): crash("1x005"); sys.exit()

        for file in os.listdir(folder_path):
            if not file.endswith("." + folder_name[:-1]): crash("1x006"); sys.exit()

            name = os.path.splitext(file)[0]
            file_path = os.path.join(folder_path, file)

            try:
                with open(file_path, "r") as f:
                    versionInfo[folder_name][name] = json.load(f)
            except json.JSONDecodeError:
                print(f"[ROM ERROR] Invalid JSON in {file_path}")
                versionInfo[folder_name][name] = None
            except Exception as e:
                print(f"[ROM ERROR] Failed to load {file_path}: {e}")
                versionInfo[folder_name][name] = None

    return versionInfo

versionInfo = setUpROM()
print(versionInfo)