import unittest
from algo_side.political_party import Political_party

class MyTestCase(unittest.TestCase):
    def test_political_party(self):
        party = Political_party(1, 5)
        self.assertEqual(1, party)
        self.assertEqual(5, party.getmandates())
        self.assertEqual([], party.getpreferences())
        party.setpreferences([1, 2, 3])
        self.assertEqual([1, 2, 3], party.getpreferences())
        party.setpreferences([2, 3, 4])
        self.assertEqual([2, 3, 4], party.getpreferences())
        self.assertEqual(2, [Political_party(1, 3), Political_party(2, 5), Political_party(3, 10)].index(3))


if __name__ == '__main__':
    unittest.main()
