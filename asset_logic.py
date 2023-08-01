import os


# Function to check if a file with the given name exists in a directory
def check_file_exists(directory, filename):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file.lower().startswith(filename.lower()):
            return True
    return False


def compare_directories(base_media_directory, assets_directory):
    media_directory_name = os.path.basename(base_media_directory)
    missing_directories = []
    missing_posters = []
    missing_backgrounds = []

    # Get a list of media directories
    media_directories = os.listdir(base_media_directory)

    for media_directory in media_directories:
        media_assets_directory = os.path.join(assets_directory, media_directory)
        if not os.path.exists(media_assets_directory):
            missing_directories.append(media_directory)
        else:
            if not check_file_exists(media_assets_directory, "poster"):
                missing_posters.append(media_directory)
            if not check_file_exists(media_assets_directory, "background"):
                missing_backgrounds.append(media_directory)

    result_file = f"missing_assets_{media_directory_name}.txt"

    # Save the results to a text file
    with open(result_file, "w") as file:
        file.write("Missing directories:\n")
        file.write("\n".join(missing_directories))
        file.write("\n\nMissing posters:\n")
        file.write("\n".join(missing_posters))
        file.write("\n\nMissing backgrounds:\n")
        file.write("\n".join(missing_backgrounds))
