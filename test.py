import convertTabsSpaces
import unittest

class TestMethods(unittest.TestCase):
    def test_empty(self):
        for l in range(1, 11):
            self.assertEqual('', convertTabsSpaces.convertLine('', l))

    def test_front(self):
        for l in range(1, 11):
            self.assertEqual(' ' * l, convertTabsSpaces.convertLine('	', l))

    def test_back(self):
        for l in range(1, 11):
            self.assertEqual('a' + ' ' * (l - 1), convertTabsSpaces.convertLine('a	', l))

    def test_middle(self):
        for l in range(1, 11):
            self.assertEqual('a' + ' ' * (l - 1) + 'b', convertTabsSpaces.convertLine('a	b', l))

if __name__ == '__main__':
    unittest.main()