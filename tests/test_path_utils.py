import unittest
from vegetable_patch import vegetable_patch
from vegetable_patch.path_utils import get_stem_path
# from vegetable_patch.path_utils import get_stem_path

from pathlib import Path


class TestGetStemPath(unittest.TestCase):
    def test_get_stem_path(self):
        # Check if the current working directory is part of the stem path:
        # TODO What happens if pytest is run from another directory?
        self.assertEqual(get_stem_path("tests"), str(Path.cwd()))
        # Check that error is thrown when looking for a directory that is not in the stem path:
        self.assertRaises(ModuleNotFoundError, get_stem_path, "fictional_dir")