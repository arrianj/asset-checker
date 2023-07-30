import os
import tkinter as tk
from asset_logic import compare_directories
from tkinter import filedialog


def select_media_directory():
    media_dir = filedialog.askdirectory(title="Select Media Directory")
    media_dir_entry.delete(0, tk.END)
    media_dir_entry.insert(tk.END, media_dir)


def select_assets_directory():
    assets_dir = filedialog.askdirectory(title="Select Assets Directory")
    assets_dir_entry.delete(0, tk.END)
    assets_dir_entry.insert(tk.END, assets_dir)


def start_comparison():
    media_dir = media_dir_entry.get()
    assets_dir = assets_dir_entry.get()

    if media_dir and assets_dir:
        compare_directories(media_dir, assets_dir)


# Create the main window
window = tk.Tk()
window.geometry("290x115")

window.title("Directory Comparison")

# Create and place the media directory widgets
media_dir_label = tk.Label(window, text="Media Directory:")
media_dir_label.grid(row=0, column=0, sticky="E")

media_dir_entry = tk.Entry(window)
media_dir_entry.grid(row=0, column=1, padx=5, pady=5)

media_dir_button = tk.Button(window, text="Select", command=select_media_directory)
media_dir_button.grid(row=0, column=2, padx=5, pady=5)

# Create and place the assets directory widgets
assets_dir_label = tk.Label(window, text="Assets Directory:")
assets_dir_label.grid(row=1, column=0, sticky="E")

assets_dir_entry = tk.Entry(window)
assets_dir_entry.grid(row=1, column=1, padx=5, pady=5)

assets_dir_button = tk.Button(window, text="Select", command=select_assets_directory)
assets_dir_button.grid(row=1, column=2, padx=5, pady=5)

# Create and place the start button
start_button = tk.Button(window, text="Check For Assets", command=start_comparison)
start_button.grid(row=2, column=1, padx=5, pady=10)

# Run the GUI event loop
if __name__ == "__main__":
    window.mainloop()
