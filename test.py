import convert_tabs_spaces
import unittest

class TestMethods(unittest.TestCase):
    def test_empty(self):
        for l in range(1, 11):
            self.assertEqual('', convert_tabs_spaces.convert_line('', l))

    def test_front(self):
        for l in range(1, 11):
            self.assertEqual(' ' * l, convert_tabs_spaces.convert_line('	', l))

    def test_back(self):
        self.assertEqual('a' + ' ', convert_tabs_spaces.convert_line('a	', 1))
        self.assertEqual('a' + ' ', convert_tabs_spaces.convert_line('a	', 2))
        self.assertEqual('a' + '  ', convert_tabs_spaces.convert_line('a	', 3))
        self.assertEqual('a' + '   ', convert_tabs_spaces.convert_line('a	', 4))
        self.assertEqual('a' + '    ', convert_tabs_spaces.convert_line('a	', 5))
        self.assertEqual('a' + '     ', convert_tabs_spaces.convert_line('a	', 6))
        self.assertEqual('a' + '      ', convert_tabs_spaces.convert_line('a	', 7))
        self.assertEqual('a' + '       ', convert_tabs_spaces.convert_line('a	', 8))
        self.assertEqual('a' + '        ', convert_tabs_spaces.convert_line('a	', 9))
        self.assertEqual('a' + '         ', convert_tabs_spaces.convert_line('a	', 10))
        self.assertEqual('aa' + ' ', convert_tabs_spaces.convert_line('aa	', 1))
        self.assertEqual('aa' + '  ', convert_tabs_spaces.convert_line('aa	', 2))
        self.assertEqual('aa' + ' ', convert_tabs_spaces.convert_line('aa	', 3))
        self.assertEqual('aa' + '  ', convert_tabs_spaces.convert_line('aa	', 4))
        self.assertEqual('aa' + '   ', convert_tabs_spaces.convert_line('aa	', 5))
        self.assertEqual('aa' + '    ', convert_tabs_spaces.convert_line('aa	', 6))
        self.assertEqual('aa' + '     ', convert_tabs_spaces.convert_line('aa	', 7))
        self.assertEqual('aa' + '      ', convert_tabs_spaces.convert_line('aa	', 8))
        self.assertEqual('aa' + '       ', convert_tabs_spaces.convert_line('aa	', 9))
        self.assertEqual('aa' + '        ', convert_tabs_spaces.convert_line('aa	', 10))

    def test_middle(self):
        self.assertEqual('a' + ' b', convert_tabs_spaces.convert_line('a	b', 1))
        self.assertEqual('a' + ' b', convert_tabs_spaces.convert_line('a	b', 2))
        self.assertEqual('a' + '  b', convert_tabs_spaces.convert_line('a	b', 3))
        self.assertEqual('a' + '   b', convert_tabs_spaces.convert_line('a	b', 4))
        self.assertEqual('a' + '    b', convert_tabs_spaces.convert_line('a	b', 5))
        self.assertEqual('a' + '     b', convert_tabs_spaces.convert_line('a	b', 6))
        self.assertEqual('a' + '      b', convert_tabs_spaces.convert_line('a	b', 7))
        self.assertEqual('a' + '       b', convert_tabs_spaces.convert_line('a	b', 8))
        self.assertEqual('a' + '        b', convert_tabs_spaces.convert_line('a	b', 9))
        self.assertEqual('a' + '         b', convert_tabs_spaces.convert_line('a	b', 10))
        self.assertEqual('aa' + ' bb', convert_tabs_spaces.convert_line('aa	bb', 1))
        self.assertEqual('aa' + '  bb', convert_tabs_spaces.convert_line('aa	bb', 2))
        self.assertEqual('aa' + ' bb', convert_tabs_spaces.convert_line('aa	bb', 3))
        self.assertEqual('aa' + '  bb', convert_tabs_spaces.convert_line('aa	bb', 4))
        self.assertEqual('aa' + '   bb', convert_tabs_spaces.convert_line('aa	bb', 5))
        self.assertEqual('aa' + '    bb', convert_tabs_spaces.convert_line('aa	bb', 6))
        self.assertEqual('aa' + '     bb', convert_tabs_spaces.convert_line('aa	bb', 7))
        self.assertEqual('aa' + '      bb', convert_tabs_spaces.convert_line('aa	bb', 8))
        self.assertEqual('aa' + '       bb', convert_tabs_spaces.convert_line('aa	bb', 9))
        self.assertEqual('aa' + '        bb', convert_tabs_spaces.convert_line('aa	bb', 10))

    def test_code(self):
        self.assertEqual('    for (auto it(s.begin());    it != s.end();  ++it) {', convert_tabs_spaces.convert_line('	for (auto it(s.begin());	it != s.end();	++it) {', 4))
        self.assertEqual('        str += *it + " ";', convert_tabs_spaces.convert_line('		str += *it + " ";', 4))
        self.assertEqual('    };', convert_tabs_spaces.convert_line('	};', 4))

if __name__ == '__main__':
    unittest.main()