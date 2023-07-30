import os
import tkinter as tk
from tkinter import filedialog


def check_file_exists(directory, filename):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file.lower().startswith(filename.lower()):
            return True
    return False


def compare_directories(media_dir, assets_dir):
    media_dir_name = os.path.basename(media_dir)
    missing_directories = []
    missing_posters = []
    missing_backgrounds = []

    media_directories = os.listdir(media_dir)

    for media_dir in media_directories:
        media_assets_dir = os.path.join(assets_dir, media_dir)
        if not os.path.exists(media_assets_dir):
            missing_directories.append(media_dir)
        else:
            if not check_file_exists(media_assets_dir, "poster"):
                missing_posters.append(media_dir)
            if not check_file_exists(media_assets_dir, "background"):
                missing_backgrounds.append(media_dir)

    result_file = f"missing_assets_{media_dir_name}.txt"

    with open(result_file, "w") as file:
        file.write(f"Missing Assets:\n\n")
        file.write("Missing directories:\n")
        file.write("\n".join(missing_directories))
        file.write("\n\nMissing posters:\n")
        file.write("\n".join(missing_posters))
        file.write("\n\nMissing backgrounds:\n")
        file.write("\n".join(missing_backgrounds))

    print(f"Comparison results saved to {result_file}")


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
window.mainloop()
