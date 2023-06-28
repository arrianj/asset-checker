import os

# Function to check if a file with the given name exists in a directory
def check_file_exists(directory, filename):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file.lower().startswith(filename.lower()):
            return True
    return False

def compare_directories(movie_dir, assets_dir):
    missing_directories = []
    missing_posters = []
    missing_backgrounds = []

    # Get a list of movie directories
    movie_directories = os.listdir(movie_dir)

    for movie_directory in movie_directories:
        movie_assets_dir = os.path.join(assets_dir, movie_directory)
        if not os.path.exists(movie_assets_dir):
            missing_directories.append(movie_directory)
        else:
            if not check_file_exists(movie_assets_dir, "poster"):
                missing_posters.append(movie_directory)
            if not check_file_exists(movie_assets_dir, "background"):
                missing_backgrounds.append(movie_directory)

    # Save the results to a text file
    with open("comparison_results.txt", "w") as file:
        file.write("Missing directories:\n")
        file.write("\n".join(missing_directories))
        file.write("\n\nMissing posters:\n")
        file.write("\n".join(missing_posters))
        file.write("\n\nMissing backgrounds:\n")
        file.write("\n".join(missing_backgrounds))

    print("Comparison results saved to comparison_results.txt")


# Example usage
media_directory = "D:/movies"
assets_directory = "D:/Plex-Meta-Manager/assets"

compare_directories(media_directory, assets_directory)
