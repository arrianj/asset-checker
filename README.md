# Asset Checker

![Python version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

The Asset Checker is a utility tool designed to compare directories and check for missing assets, such as posters and backgrounds, for media directories used in Plex Meta Manager or similar applications.

## Table of Contents

- [Asset Checker](#asset-checker)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
    - [CLI Version](#cli-version)
    - [GUI Version](#gui-version)
    - [Creating Executables](#creating-executables)
      - [CLI Version Executable](#cli-version-executable)
      - [GUI Version Executable](#gui-version-executable)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)

## Introduction

The repository contains two versions of the Asset Checker tool:

1. **CLI Version**: `asset_check_cli.py` provides a command-line interface for comparing media and assets directories. Users can specify directories and perform the comparison, generating a `comparison_results.txt` file with the missing directories, posters, and backgrounds.

2. **GUI Version**: `asset_check_gui.py` presents a graphical user interface using `tkinter`, allowing users to select directories via buttons. The GUI version outputs results to `missing_assets_<media_directory>.txt`, containing the missing directories, posters, and backgrounds.

## Prerequisites

To use the Asset Checker tool, ensure the following prerequisites are met:

- Python 3.6 or higher is installed on your system.
- Install the required dependencies by running:

  ```
  pip install -r requirements.txt
  ```

## Usage

### CLI Version

1. Open `asset_check_cli.py` in a text editor or IDE.
2. Modify `media_directory` and `assets_directory` variables at the beginning of the script to specify directories.
3. Save the changes.
4. Open a command-line interface.
5. Navigate to the script's directory.
6. Run the following command to execute the script:

   ```
   python asset_check_cli.py
   ```

7. The script compares directories and generates `comparison_results.txt`.

### GUI Version

1. Open `asset_check_gui.py` in a text editor or IDE.
2. Modify the code if needed, such as setting default directories or customizing GUI elements.
3. Save the changes.
4. Open a command-line interface.
5. Navigate to the script's directory.
6. Run the following command to execute the script:

   ```
   python asset_check_gui.py
   ```

7. The GUI window will appear.
8. Click the "Select" buttons next to "Media Directory" and "Assets Directory" fields to choose directories.
9. Click "Check For Assets" to start the comparison.
10. The script compares the selected directories and generates `missing_assets_<media_directory>.txt`.

### Creating Executables

You can use `PyInstaller` to create standalone executables for both versions:

#### CLI Version Executable

1. Open a command-line interface.
2. Navigate to the script's directory.
3. Run the following command to create the executable:

   ```
   pyinstaller asset_check_cli.py --onefile
   ```

4. The executable will be in the `dist` directory.

#### GUI Version Executable

1. Open a command-line interface.
2. Navigate to the script's directory.
3. Run the following command to create the executable:

   ```
   pyinstaller asset_check_gui.py --onefile --noconsole
   ```

4. The executable will be in the `dist` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The CLI version of the script is based on the work of the original author.
- The GUI version of the script utilizes the `tkinter` library for creating the graphical interface.

For any questions or issues, feel free to open an issue or contribute to the project!