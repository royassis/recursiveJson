import unittest
import recursiveJson.utils as utils

class MyTestCase(unittest.TestCase):
    def test_join_keys1(self):
        results = utils.join_keys("_", "a","b")
        self.assertEqual(results, "a_b")
    def test_filter_list(self):
        l = []
        input_a = "a"
        input_b = "b"
        input_x = excluded_values = ""
        results = utils.filter_list(excluded_values,input_a,input_b, input_x)
        self.assertEqual(results, ["a","b"])

    def test_add_prefix_to_dict_keys(self):
        prefix = "newprefix"
        prefix_edited = f"{prefix}"
        test_dict = {"roy":1, "mosh":1}

        expected_results = {f"{prefix_edited}__roy":1, f"{prefix_edited}__mosh":1}
        test_results = utils.add_prefix_to_dict_keys(test_dict, prefix)

        self.assertEqual(expected_results, test_results)

    def test_extract_dict_items_by_val_type_list(self):
        test_dict = {"roy": 1, "mosh": []}
        expected_results =  {"mosh": []}
        test_results = utils.extract_dict_items_by_val_type(test_dict, list)

        self.assertEqual(expected_results, test_results)

    def test_extract_dict_items_by_val_type_dict(self):
        test_dict = {"roy": 1, "mosh": {}}
        expected_results =  {"mosh": {}}
        test_results = utils.extract_dict_items_by_val_type(test_dict, dict)

        self.assertEqual(expected_results, test_results)

if __name__ == '__main__':
    unittest.main()
