import unittest

from vegetable_patch import vegetable_patch
from vegetable_patch.string_utils import replace_case_insensitive

class TestReplaceCaseInsensitive(unittest.TestCase):
    def test_replace_case_insensitive(self):
        string = 'We can write: string, String, STRING, strinG'
        expected_res = 'We can write: string, string, string, string'

        self.assertEqual(
            replace_case_insensitive(
                input_string=string,
                search_pattern='string',
                replacement='string'),
            expected_res
        )

