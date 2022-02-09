import unittest
from algo_side.division_item import Division_item
from algo_side.political_party import Political_party


class MyTestCase(unittest.TestCase):
    def test_item(self):
        self.assertEqual(Division_item("Test"), 'Test')
        self.assertEqual(1, [Division_item("a"), Division_item("b"), Division_item("c")].index('b'))
        self.assertEqual(4, Division_item("new_item").getid())
        self.assertEqual(5, Division_item("new_item").getid())
        self.assertEqual("Hey", Division_item("Hey").getname())
        it = Division_item("T")
        it.setname("Test")
        self.assertEqual("Test", it)

    def test_political_party(self):
        party = Political_party("A", 5)
        self.assertEqual("A", party)
        self.assertEqual(5, party.getmandates())
        self.assertEqual([], party.getpreferences())
        party.setpreferences([1, 2, 3])
        self.assertEqual([1, 2, 3], party.getpreferences())
        party.setpreferences([2, 3, 4])
        self.assertEqual([2, 3, 4], party.getpreferences())
        self.assertEqual(2, [Political_party("A", 3), Political_party("B", 5), Political_party("C", 10)].index("C"))


if __name__ == '__main__':
    unittest.main()
