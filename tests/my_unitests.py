import unittest
from recursiveJson.utils import get_first_key_from_dict,join_keys,filter_list, add_prefix_to_dict_keys

class MyTestCase(unittest.TestCase):
    def test_get_first_key_from_dict(self):
        key = "a"
        val = 1
        input = {key:val}
        results = get_first_key_from_dict(input)
        self.assertEqual(results, key)

    def test_join_keys1(self):
        results = join_keys("_", "a","b")
        self.assertEqual(results, "a_b")

    def test_join_keys2(self):
        results = join_keys("_", "a","b")
        self.assertEqual(results, "a")

    def test_join_keys3(self):
        results = join_keys("_", "a","b")
        self.assertEqual(results, "a")

    def test_filter_list(self):
        l = []
        input_a = "a"
        input_b = "b"
        input_x = excluded_values = ""
        results = filter_list(excluded_values,input_a,input_b, input_x)
        self.assertEqual(results, ["a","b"])

    def test_add_prefix_to_dict_keys(self):
        prefix = "newprefix"
        prefix_edited = f"|{prefix}|"
        test_dict = {"roy":1, "mosh":1}

        expected_results = {f"{prefix_edited}_roy":1, f"{prefix_edited}_mosh":1}
        test_results = add_prefix_to_dict_keys(test_dict, prefix)

        self.assertEqual(expected_results, test_results)

if __name__ == '__main__':
    unittest.main()
