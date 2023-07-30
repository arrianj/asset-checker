import unittest
import tempfile
import shutil
import os

from asset_logic import check_file_exists, compare_directories


class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory and files for testing
        self.temp_dir = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.temp_dir, "media_dir", "dir1"))
        os.makedirs(os.path.join(self.temp_dir, "media_dir", "dir2"))
        os.makedirs(os.path.join(self.temp_dir, "assets_dir", "dir1"))
        with open(
            os.path.join(self.temp_dir, "media_dir", "dir1", "poster.jpg"), "w"
        ) as f:
            f.write("This is a poster file.")
        with open(
            os.path.join(self.temp_dir, "media_dir", "dir2", "background.jpg"), "w"
        ) as f:
            f.write("This is a background file.")

    def tearDown(self):
        # Clean up temporary directory and files after testing
        shutil.rmtree(self.temp_dir)

    def test_check_file_exists(self):
        self.assertTrue(
            check_file_exists(
                os.path.join(self.temp_dir, "media_dir", "dir1"), "poster"
            )
        )
        self.assertTrue(
            check_file_exists(
                os.path.join(self.temp_dir, "media_dir", "dir2"), "background"
            )
        )
        self.assertFalse(
            check_file_exists(
                os.path.join(self.temp_dir, "media_dir", "dir1"), "background"
            )
        )
        self.assertFalse(
            check_file_exists(
                os.path.join(self.temp_dir, "media_dir", "dir2"), "poster"
            )
        )


class TestCompareDirectories(unittest.TestCase):
    def setUp(self):
        # Create temporary directories for testing
        self.media_dir = tempfile.mkdtemp()
        self.assets_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove temporary directories after testing
        shutil.rmtree(self.media_dir)
        shutil.rmtree(self.assets_dir)

    def test_compare_directories_with_no_missing_assets(self):
        # Create some test media directories and corresponding asset directories
        test_media_dirs = ["movie1", "movie2", "movie3"]
        for media_dir in test_media_dirs:
            media_path = os.path.join(self.media_dir, media_dir)
            os.makedirs(media_path)

            assets_path = os.path.join(self.assets_dir, media_dir)
            os.makedirs(assets_path)

            # Create empty "poster" and "background" files
            poster_file = os.path.join(assets_path, "poster")
            background_file = os.path.join(assets_path, "background")
            open(poster_file, "a").close()
            open(background_file, "a").close()

        # Call the function under test
        compare_directories(self.media_dir, self.assets_dir)

        # Assert the function produces the correct results
        result_file = f"missing_assets_{os.path.basename(self.media_dir)}.txt"
        with open(result_file, "r") as file:
            result_content = file.read()

        expected_result = (
            "Missing directories:\n\n\nMissing posters:\n\n\nMissing backgrounds:\n"
        )

        self.assertEqual(result_content, expected_result)
        os.remove(result_file)

    def test_compare_directories_with_missing_assets(self):
        # Create some test media directories without corresponding asset directories
        test_media_dirs = ["movie1", "movie2", "movie3"]
        for media_dir in test_media_dirs:
            media_path = os.path.join(self.media_dir, media_dir)
            os.makedirs(media_path)

        # Call the function under test
        compare_directories(self.media_dir, self.assets_dir)

        # Assert the function produces the correct results
        result_file = f"missing_assets_{os.path.basename(self.media_dir)}.txt"
        with open(result_file, "r") as file:
            result_content = file.read()

        root_dir = os.path.dirname(os.path.abspath(__file__))
        expected_result_file = os.path.join(
            root_dir, "test_data", "expected_missing_assets.txt"
        )

        with open(expected_result_file, "r") as file:
            expected_result = file.read()

        self.assertEqual(result_content, expected_result)
        os.remove(result_file)


if __name__ == "__main__":
    unittest.main()
