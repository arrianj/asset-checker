import unittest
import os
import tempfile
from unittest.mock import patch, call
from asset_logic import (
    check_file_exists,
    compare_directories,
)  # Adjust this import as needed


class TestFileExistenceFunctions(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.base_dir = tempfile.TemporaryDirectory()
        self.assets_dir = tempfile.TemporaryDirectory()

        # Create some directories and files for testing
        os.makedirs(os.path.join(self.base_dir.name, "media1"))
        os.makedirs(os.path.join(self.base_dir.name, "media2"))
        os.makedirs(os.path.join(self.assets_dir.name, "media1"))
        os.makedirs(os.path.join(self.assets_dir.name, "media2"))

        # Create test files
        with open(os.path.join(self.assets_dir.name, "media1", "poster.jpg"), "w") as f:
            f.write("test poster")
        with open(
            os.path.join(self.assets_dir.name, "media2", "background.jpg"), "w"
        ) as f:
            f.write("test background")

    def tearDown(self):
        # Cleanup temporary directories
        self.base_dir.cleanup()
        self.assets_dir.cleanup()

    def test_check_file_exists(self):
        # Test case where file exists
        self.assertTrue(
            check_file_exists(os.path.join(self.assets_dir.name, "media1"), "poster")
        )
        # Test case where file does not exist
        self.assertFalse(
            check_file_exists(
                os.path.join(self.assets_dir.name, "media1"), "background"
            )
        )

    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    def test_compare_directories(self, mock_open):
        compare_directories(self.base_dir.name, self.assets_dir.name)
        mock_open.assert_called_once_with(
            f"missing_assets_{os.path.basename(self.base_dir.name)}.txt", "w"
        )

        # Check contents written to the file
        handle = mock_open()

        # Print actual calls for debugging
        print("Actual write calls:", handle.write.mock_calls)

        expected_calls = [
            call.write("\n\nMissing posters:\n"),
            call.write("media2"),
            call.write("\n\nMissing backgrounds:\n"),
            call.write("media1"),
        ]

        handle.write.assert_has_calls(expected_calls, any_order=True)

    def test_compare_directories_no_missing(self):
        # Create the needed files so nothing is missing
        with open(
            os.path.join(self.assets_dir.name, "media1", "background.jpg"), "w"
        ) as f:
            f.write("test background")
        with open(os.path.join(self.assets_dir.name, "media2", "poster.jpg"), "w") as f:
            f.write("test poster")

        with patch("builtins.open", new_callable=unittest.mock.mock_open) as mock_open:
            compare_directories(self.base_dir.name, self.assets_dir.name)
            mock_open.assert_called_once_with(
                f"missing_assets_{os.path.basename(self.base_dir.name)}.txt", "w"
            )

            # Check contents written to the file
            handle = mock_open()
            handle.write.assert_not_called()


if __name__ == "__main__":
    unittest.main()
