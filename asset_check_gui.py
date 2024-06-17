import os
import tkinter as tk
from asset_logic import compare_directories
from tkinter import filedialog, messagebox


def select_media_directory():
    media_directory = filedialog.askdirectory(title="Select Media Directory")
    media_directory_entry.delete(0, tk.END)
    media_directory_entry.insert(tk.END, media_directory)


def select_assets_directory():
    assets_directory = filedialog.askdirectory(title="Select Assets Directory")
    assets_directory_entry.delete(0, tk.END)
    assets_directory_entry.insert(tk.END, assets_directory)


def start_comparison():
    media_directory = media_directory_entry.get()
    assets_directory = assets_directory_entry.get()

    if media_directory and assets_directory:
        compare_directories(media_directory, assets_directory)
        messagebox.showinfo("Report", "Report generated")


# Create the main window
window = tk.Tk()
window.geometry("290x115")
window.title("Directory Comparison")

# Create and place the media directory widgets
media_directory_label = tk.Label(window, text="Media Directory:")
media_directory_label.grid(row=0, column=0, sticky="E")

media_directory_entry = tk.Entry(window)
media_directory_entry.grid(row=0, column=1, padx=5, pady=5)

media_directory_button = tk.Button(
    window, text="Select", command=select_media_directory
)
media_directory_button.grid(row=0, column=2, padx=5, pady=5)

# Create and place the assets directory widgets
assets_directory_label = tk.Label(window, text="Assets Directory:")
assets_directory_label.grid(row=1, column=0, sticky="E")

assets_directory_entry = tk.Entry(window)
assets_directory_entry.grid(row=1, column=1, padx=5, pady=5)

assets_directory_button = tk.Button(
    window, text="Select", command=select_assets_directory
)
assets_directory_button.grid(row=1, column=2, padx=5, pady=5)

# Create and place the start button
start_button = tk.Button(window, text="Check For Assets", command=start_comparison)
start_button.grid(row=2, column=1, padx=5, pady=10)

# Run the GUI event loop
if __name__ == "__main__":
    window.mainloop()
