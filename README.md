# Asset Checker

This repository contains two scripts: `asset_check_cli.py` and `asset_check_gui.py`. These scripts allow you to compare directories and check for missing assets for Plex Meta Manager or other tools, looking for posters and backgrounds.

## Prerequisites

Before running the scripts, ensure that you have the following:

- Python 3 installed on your system.
- Required dependencies installed. You can install them by running the following command:

  ```
  pip install -r requirements.txt
  ```

## Usage

### CLI Version

The CLI version of the tool is implemented in `asset_check_cli.py`. To use it, follow these steps:

1. Open the script file `asset_check_cli.py` in a text editor or IDE.
2. Modify the `media_directory` and `assets_directory` variables at the beginning of the script to specify the directories you want to compare.
3. Save the changes.
4. Open a command-line interface.
5. Navigate to the directory where the script is saved.
6. Run the following command to execute the script:

   ```
   python asset_check_cli.py
   ```

7. The script will compare the specified directories and generate a `comparison_results.txt` file, which will contain the missing directories, missing posters, and missing backgrounds.
8. The comparison results will also be printed in the console.

### GUI Version

The GUI version of the tool is implemented in `asset_check_gui.py`. To use it, follow these steps:

1. Open the script file `asset_check_gui.py` in a text editor or IDE.
2. Modify the code if needed, such as setting default directories or customizing the GUI elements.
3. Save the changes.
4. Open a command-line interface.
5. Navigate to the directory where the script is saved.
6. Run the following command to execute the script:

   ```
   python asset_check_gui.py
   ```

7. The GUI window will appear.
8. Click the "Select" buttons next to the "Media Directory" and "Assets Directory" fields to choose the directories you want to compare.
9. Click the "Check For Assets" button to start the comparison.
10. The script will compare the selected directories and generate a `missing_assets_<media_directory>.txt` file, which will contain the missing directories, missing posters, and missing backgrounds.
11. The comparison results will also be printed in the console.

### Creating Executables

You can use `PyInstaller` to create standalone executables for the CLI and GUI versions of the tool. Follow these steps to create the executables:

#### CLI Version Executable

1. Open a command-line interface.
2. Navigate to the directory where the `asset_check_cli.py` script is saved.
3. Run the following command to create the executable:

   ```
   pyinstaller asset_check_cli.py --onefile
   ```

4. Once the process completes, the executable file will be created in the `dist` directory.

#### GUI Version Executable

1. Open a command-line interface.
2. Navigate to the directory where the `asset_check_gui.py` script is saved.
3. Run the following command to create the executable:

   ```
   pyinstaller asset_check_gui.py --onefile --noconsole
   ```

4. Once the process completes, the executable file will be created in the `dist` directory.
5. The `--noconsole` option is used to hide the console window for the GUI application.

**Note:** The `--onefile` option creates a single executable file. If you prefer a directory with multiple files, you can omit this option.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The CLI version of the script is based on the

 work of the original author.
- The GUI version of the script utilizes the `tkinter` library for creating the graphical interface.
