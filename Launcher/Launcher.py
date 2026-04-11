import sys
import os
import pygame
import json

pygame.init()

clock = pygame.time.Clock()

WIN_W = 800
WIN_H = 600

WIN = pygame.display.set_mode((WIN_W, WIN_H), pygame.RESIZABLE, vsync=1)

pygame.display.set_caption("FLauncher")
pygame.display.set_icon(pygame.image.load("Launcher/assets/ico.png"))

VERSIONS_DIR = "Launcher/versions"
versions_list = os.listdir(VERSIONS_DIR)

FPS = 60

font = pygame.font.SysFont(None, 25)

cols = {"black": (0, 0, 0), "white": (255, 255, 255),
    "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255),
    "yellow": (255, 255, 0), "cyan": (0, 255, 255), "magenta": (255, 0, 255),
    "gray": (128, 128, 128), "dark_gray": (64, 64, 64), "light_gray": (192, 192, 192)}

versionBox = pygame.Rect(30, 520, 150, 50)

def play(MODLOADER_PATH, selected_version):
    version_path = os.path.join(VERSIONS_DIR, selected_version)
    sys.argv = ["FinderOriginal.py", version_path]
    exec(open(MODLOADER_PATH, "r").read())

def renounce():
    versionBox.topleft, versionBox.size = (30, WIN_H - 80), (150, 50)

def crash(num):
    print(f"Crash: Error code '{num}'")
    return False

def draw(version):
    WIN.fill(cols["white"])
    pygame.draw.rect(WIN, cols["yellow"], versionBox)
    text = font.render(version, True, cols["black"])
    text_rect = text.get_rect(center=versionBox.center)
    WIN.blit(text, text_rect)
    pygame.display.update()

def main():
    global WIN, WIN_W, WIN_H, moddata
    run = True
    v = 0
    if any(not os.path.isdir(os.path.join(VERSIONS_DIR, v)) for v in os.listdir(VERSIONS_DIR)): run = crash("1x002")
    if len(versions_list) == 0: run = crash("1x000")
    while run:
        clock.tick(FPS)
        ATTRIBUTE_PATH = os.path.join(VERSIONS_DIR, versions_list[v], ".attr")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if versionBox.collidepoint(event.pos):
                    if event.button == 4: v = max(0, v-1)
                    elif event.button == 5: v = min(len(versions_list)-1, v+1)
                    elif event.button == 1:
                        if not os.path.isdir(os.path.join(VERSIONS_DIR, versions_list[v], "src")): run = crash("1x004")
                        play(f"Finder-Base/game.py", versions_list[v])
            elif event.type == pygame.VIDEORESIZE:
                WIN_W, WIN_H = event.w, event.h
                WIN = pygame.display.set_mode((WIN_W, WIN_H), pygame.RESIZABLE, vsync=1)
                renounce()
            
        try: 
            with open(ATTRIBUTE_PATH, "r") as f: json.load(f)
        except FileNotFoundError: run = crash("1x001")
        except json.JSONDecodeError: run = crash("1x003")

        draw(versions_list[v])

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()