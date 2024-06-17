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
    missing_both = []

    # Get a list of media directories
    media_directories = os.listdir(base_media_directory)

    for media_directory in media_directories:
        media_assets_directory = os.path.join(assets_directory, media_directory)

        # Check if the assets directory exists
        if not os.path.exists(media_assets_directory):
            # If not, add to the list of missing directories
            missing_directories.append(media_directory)
        else:
            # Check if poster and background files exist
            poster_exists = check_file_exists(media_assets_directory, "poster")
            background_exists = check_file_exists(media_assets_directory, "background")

            # Track directories missing both posters and backgrounds
            if not poster_exists and not background_exists:
                missing_both.append(media_directory)
            # Track directories missing only posters
            if not poster_exists:
                missing_posters.append(media_directory)
            # Track directories missing only backgrounds
            if not background_exists:
                missing_backgrounds.append(media_directory)

    result_file = f"missing_assets_{media_directory_name}.txt"

    # Save the results to a text file
    with open(result_file, "w") as file:
        if missing_directories:
            file.write("Missing directories:\n")
            file.write("\n".join(missing_directories))
        if missing_both:
            file.write("\n\nMissing both poster and background:\n")
            file.write("\n".join(missing_both))
        if missing_posters:
            file.write("\n\nMissing posters:\n")
            file.write("\n".join(missing_posters))
        if missing_backgrounds:
            file.write("\n\nMissing backgrounds:\n")
            file.write("\n".join(missing_backgrounds))
