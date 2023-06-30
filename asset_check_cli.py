import os


# Function to check if a file with the given name exists in a directory
def check_file_exists(directory, filename):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file.lower().startswith(filename.lower()):
            return True
    return False


def compare_directories(media_dir, assets_dir):
    missing_directories = []
    missing_posters = []
    missing_backgrounds = []

    # Get a list of media directories
    media_directories = os.listdir(media_dir)

    for media_directory in media_directories:
        media_assets_dir = os.path.join(assets_dir, media_directory)
        if not os.path.exists(media_assets_dir):
            missing_directories.append(media_directory)
        else:
            if not check_file_exists(media_assets_dir, "poster"):
                missing_posters.append(media_directory)
            if not check_file_exists(media_assets_dir, "background"):
                missing_backgrounds.append(media_directory)

    result_file = f"missing_assets_{media_assets_dir}.txt"


    # Save the results to a text file
    with open("result_file.txt", "w") as file:
        file.write("Missing directories:\n")
        file.write("\n".join(missing_directories))
        file.write("\n\nMissing posters:\n")
        file.write("\n".join(missing_posters))
        file.write("\n\nMissing backgrounds:\n")
        file.write("\n".join(missing_backgrounds))

    print(f"Comparison results saved to {result_file}")

media_directory = "D:/movies"
assets_directory = "D:/Plex-Meta-Manager/assets"

compare_directories(media_directory, assets_directory)
