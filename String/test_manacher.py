import unittest
import manacher


class TestManacher(unittest.TestCase):
    def test_manacher(self):
        s = "ababc"
        i, j = manacher.manacher(s)
        self.assertEqual("bab", s[i:j])

        s = ""
        i, j = manacher.manacher(s)
        self.assertEqual("", s[i:j])

        s = "abcc"
        i, j = manacher.manacher(s)
        self.assertEqual("cc", s[i:j])


if __name__ == "__main__":
    unittest.main()
