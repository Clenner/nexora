import sys
import json
import os
import pygame
import time

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
    "tags": {},
    "assets": {}
}

randomAccessMemory = {}

def crash(num):
    print(f"Crash: Error code '{num}'")
    return False

class Entity:
    def __init__(self, name, mhp=20, inventory=False, pcs=None):
        if pcs is None:
            pcs = []

        self.name = name
        self.health = mhp
        self.max_health = mhp
        self.inventory = inventory
        self.processes = [
            os.path.join(VERSION_PATH, "src", "processes", process + ".py")
            for process in pcs
        ]

def setUpROM():
    # Basic checks
    #assets
    #gooeys
    #processes
    #entitys
    for folder_name in ["blocks", "dimensions", "recipes", "tags", "items"]:

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
    for asset in os.listdir(os.path.join(VERSION_PATH, "src", "assets")):
        image = pygame.image.load(os.path.join(VERSION_PATH, "src", "assets", asset))
        versionInfo["assets"].append(image)

    return versionInfo

versionInfo = setUpROM()
print(versionInfo)