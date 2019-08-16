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
        self.assertEqual('a' + ' ', convertTabsSpaces.convertLine('a	', 1))
        self.assertEqual('a' + ' ', convertTabsSpaces.convertLine('a	', 2))
        self.assertEqual('a' + '  ', convertTabsSpaces.convertLine('a	', 3))
        self.assertEqual('a' + '   ', convertTabsSpaces.convertLine('a	', 4))
        self.assertEqual('a' + '    ', convertTabsSpaces.convertLine('a	', 5))
        self.assertEqual('a' + '     ', convertTabsSpaces.convertLine('a	', 6))
        self.assertEqual('a' + '      ', convertTabsSpaces.convertLine('a	', 7))
        self.assertEqual('a' + '       ', convertTabsSpaces.convertLine('a	', 8))
        self.assertEqual('a' + '        ', convertTabsSpaces.convertLine('a	', 9))
        self.assertEqual('a' + '         ', convertTabsSpaces.convertLine('a	', 10))
        self.assertEqual('aa' + ' ', convertTabsSpaces.convertLine('aa	', 1))
        self.assertEqual('aa' + '  ', convertTabsSpaces.convertLine('aa	', 2))
        self.assertEqual('aa' + ' ', convertTabsSpaces.convertLine('aa	', 3))
        self.assertEqual('aa' + '  ', convertTabsSpaces.convertLine('aa	', 4))
        self.assertEqual('aa' + '   ', convertTabsSpaces.convertLine('aa	', 5))
        self.assertEqual('aa' + '    ', convertTabsSpaces.convertLine('aa	', 6))
        self.assertEqual('aa' + '     ', convertTabsSpaces.convertLine('aa	', 7))
        self.assertEqual('aa' + '      ', convertTabsSpaces.convertLine('aa	', 8))
        self.assertEqual('aa' + '       ', convertTabsSpaces.convertLine('aa	', 9))
        self.assertEqual('aa' + '        ', convertTabsSpaces.convertLine('aa	', 10))

    def test_middle(self):
        self.assertEqual('a' + ' b', convertTabsSpaces.convertLine('a	b', 1))
        self.assertEqual('a' + ' b', convertTabsSpaces.convertLine('a	b', 2))
        self.assertEqual('a' + '  b', convertTabsSpaces.convertLine('a	b', 3))
        self.assertEqual('a' + '   b', convertTabsSpaces.convertLine('a	b', 4))
        self.assertEqual('a' + '    b', convertTabsSpaces.convertLine('a	b', 5))
        self.assertEqual('a' + '     b', convertTabsSpaces.convertLine('a	b', 6))
        self.assertEqual('a' + '      b', convertTabsSpaces.convertLine('a	b', 7))
        self.assertEqual('a' + '       b', convertTabsSpaces.convertLine('a	b', 8))
        self.assertEqual('a' + '        b', convertTabsSpaces.convertLine('a	b', 9))
        self.assertEqual('a' + '         b', convertTabsSpaces.convertLine('a	b', 10))
        self.assertEqual('aa' + ' bb', convertTabsSpaces.convertLine('aa	bb', 1))
        self.assertEqual('aa' + '  bb', convertTabsSpaces.convertLine('aa	bb', 2))
        self.assertEqual('aa' + ' bb', convertTabsSpaces.convertLine('aa	bb', 3))
        self.assertEqual('aa' + '  bb', convertTabsSpaces.convertLine('aa	bb', 4))
        self.assertEqual('aa' + '   bb', convertTabsSpaces.convertLine('aa	bb', 5))
        self.assertEqual('aa' + '    bb', convertTabsSpaces.convertLine('aa	bb', 6))
        self.assertEqual('aa' + '     bb', convertTabsSpaces.convertLine('aa	bb', 7))
        self.assertEqual('aa' + '      bb', convertTabsSpaces.convertLine('aa	bb', 8))
        self.assertEqual('aa' + '       bb', convertTabsSpaces.convertLine('aa	bb', 9))
        self.assertEqual('aa' + '        bb', convertTabsSpaces.convertLine('aa	bb', 10))

    def test_code(self):
        self.assertEqual('    for (auto it(s.begin());    it != s.end();  ++it) {', convertTabsSpaces.convertLine('	for (auto it(s.begin());	it != s.end();	++it) {', 4))
        self.assertEqual('        str += *it + " ";', convertTabsSpaces.convertLine('		str += *it + " ";', 4))
        self.assertEqual('    };', convertTabsSpaces.convertLine('	};', 4))

if __name__ == '__main__':
    unittest.main()