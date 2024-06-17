import os
from asset_logic import compare_directories


def get_valid_directory(prompt):
    while True:
        directory = input(prompt)
        if os.path.isdir(directory):
            return directory
        else:
            print("Invalid directory. Please enter a valid directory path.")


if __name__ == "__main__":
    while True:
        use_hardcoded = input(
            "Do you want to use the default media directories? (y/n): "
        ).lower()

        if use_hardcoded == "y":
            assets_directory = "D:/Plex-Meta-Manager/assets"

            while True:
                choose_directory = input(
                    "Do you want to check for movies or tv? (m/t): "
                ).lower()
                if choose_directory == "t":
                    media_directory = "D:/tv"
                    break
                elif choose_directory == "m":
                    media_directory = "D:/movies"
                    break
                else:
                    print("Invalid choice. Please try again.")

            break

        elif use_hardcoded == "n":
            media_directory = get_valid_directory("Enter the media directory path: ")
            assets_directory = get_valid_directory("Enter the assets directory path: ")

            break

        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    compare_directories(media_directory, assets_directory)
    print("Report generated")
