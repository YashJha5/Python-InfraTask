import unittest
import main


class TestMain(unittest.TestCase):

    def test_positive_list(self):
        data = {'a': {'b': ['e', 'd']}, 'b': {'b': {'c': 'z'}}, 'y': 'j'}
        key_input = 'a/b'
        output = ['e', 'd']
        result = main.main(data, key_input)
        self.assertEqual(result, output)

    def test_negative_list(self):
        data = {'a': {'b': ['e', 'd']}, 'b': {'b': {'c': 'z'}}, 'y': 'j'}
        key_input = 'a/b/e'
        output = 'Not a valid key/ nested key'
        result = main.main(data, key_input)
        self.assertEqual(result, output)

    def test_positive_single_key(self):
        data = {'a': {'b': ['e', 'd']}, 'b': {'b': {'c': 'z'}}, 'y': 'j'}
        key_input = 'a'
        output = {'b': ['e', 'd']}
        result = main.main(data, key_input)
        self.assertEqual(result, output)

    def test_negative_single_key(self):
        data = {'a': {'b': ['e', 'd']}, 'b': {'b': {'c': 'z'}}, 'y': 'j'}
        key_input = 'j'
        output = 'Not a valid key/ nested key'
        result = main.main(data, key_input)
        self.assertEqual(result, output)

    def test_negative_keys(self):
        data = {'a': {'b': ['e', 'd']}, 'b': {'b': {'c': 'z'}}, 'y': 'j'}
        key_input = 'b/b/e'
        output = 'Not a valid key/ nested key'
        result = main.main(data, key_input)
        self.assertEqual(result, output)

    def test_input_not_dictionary(self):
        data = [1, 2, 3]
        key_input = 'b/b/e'
        self.assertRaises(Exception, main.main, data, key_input)

    def test_basic(self):
        data = {'a': {'b': {'c': 'd'}}}
        key_input = 'a/b/c'
        output = 'd'
        result = main.main(data, key_input)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
