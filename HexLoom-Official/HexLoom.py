import tkinter as tk
from tkinter import messagebox
import subprocess
import pygame
import sys

# Function to launch Pygame workspace selector
def run_pygame_selector():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Workspace Selector")

    # Simple pygame loop (just for the workspace selector)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))  # Fill screen with black
        pygame.display.flip()

    pygame.quit()

# Function to launch Tkinter workspace creation GUI
def run_tkinter_creation():
    window = tk.Tk()
    window.title("Create Workspace")

    mod_name_label = tk.Label(window, text="Mod Name:")
    mod_name_label.pack(pady=5)

    mod_name_entry = tk.Entry(window)
    mod_name_entry.pack(pady=5)

    mod_loader_label = tk.Label(window, text="Mod Loader:")
    mod_loader_label.pack(pady=5)

    mod_loader_var = tk.StringVar(window)
    mod_loader_var.set("Forge")  # Default value
    mod_loader_dropdown = tk.OptionMenu(window, mod_loader_var, "Forge", "Fabric")
    mod_loader_dropdown.pack(pady=5)

    version_label = tk.Label(window, text="Version:")
    version_label.pack(pady=5)

    version_var = tk.StringVar(window)
    version_var.set("1.0.0")  # Default version
    version_dropdown = tk.OptionMenu(window, version_var, "1.0.0")
    version_dropdown.pack(pady=5)

    def confirm():
        name = mod_name_entry.get()
        loader = mod_loader_var.get()
        version = version_var.get()

        if not name:
            messagebox.showwarning("Missing Info", "Please enter a mod name.")
            return

        messagebox.showinfo("Success", f"Workspace '{name}' created with:\nLoader: {loader}\nVersion: {version}")
        
        window.destroy()  # Close the creation window after confirming

    confirm_button = tk.Button(window, text="Create Workspace", command=confirm)
    confirm_button.pack(pady=20)

    open_workspace_button = tk.Button(window, text="Open Workspace", command=lambda: messagebox.showinfo("Open Workspace", "Open workspace functionality is not implemented yet."))
    open_workspace_button.pack(pady=5)

    window.mainloop()

# Main function to run both Tkinter and Pygame
def main():
    # Launch Pygame workspace selector in a subprocess
    pygame_process = subprocess.Popen(["python", "path_to_pygame_selector.py"])  # Replace with the correct path

    # Launch Tkinter workspace creation window in another subprocess
    tkinter_process = subprocess.Popen(["python", "path_to_tkinter_creation.py"])  # Replace with the correct path

    # Wait for both processes to complete
    pygame_process.wait()
    tkinter_process.wait()

if __name__ == "__main__":
    main()
