import unittest
import name

class TestName(unittest.TestCase):
    def test_combine(self):
        result = name.combine("Matthew", "Brayton")
        self.assertEqual(result, "Matthew Brayton")

    def test_combine1(self):
        result = name.combine("1", "2")
        self.assertEqual(result, "1 2")

    def test_combine2(self):
        result = name.combine(":", ")")
        self.assertEqual(result, ": )")


if __name__ == '__main__':
    unittest.main()
