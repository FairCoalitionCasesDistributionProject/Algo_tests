import unittest
from algo_side.division import Division
from algo_side.political_party import Political_party

class MyTestCase(unittest.TestCase):
    def test_creation(self):
        div = Division()
        self.assertEqual([], div.parties)
        self.assertEqual(0, div.num_of_items)
        self.assertEqual(0, div.num_of_parties)
        self.assertEqual(0, div.number_of_mandates)
        div = Division([Political_party(1, 5), Political_party(2, 7)],2)
        self.assertEqual([1, 2], div.parties)
        self.assertEqual([Political_party(1, 5), Political_party(2, 7)], div.parties)
        self.assertEqual(2, div.num_of_items)
        self.assertEqual(2, div.num_of_parties)
        self.assertEqual(12, div.number_of_mandates)


    def test_political_party_addition_removal(self):
        div = Division([Political_party(1, 5), Political_party(2, 7)])
        div.add_party(3, 6)
        self.assertEqual([1, 2, 3], div.parties)
        self.assertEqual(3, div.num_of_parties)
        self.assertEqual(18, div.number_of_mandates)
        div.add_party(1, 5)
        self.assertEqual(3, div.num_of_parties)
        self.assertEqual(18, div.number_of_mandates)
        div.add_parties([(1, 5), (4, 5), (5, 5)])
        self.assertEqual([1, 2, 3, 4, 5], div.parties)
        self.assertEqual(5, div.num_of_parties)
        self.assertEqual(28, div.number_of_mandates)
        div.remove_party(6)
        div.remove_party(3)
        self.assertEqual([1, 2, 4, 5], div.parties)
        self.assertEqual(4, div.num_of_parties)
        self.assertEqual(22, div.number_of_mandates)
        div.remove_parties([4, 5, 6])
        self.assertEqual([1, 2], div.parties)
        self.assertEqual(2, div.num_of_parties)
        self.assertEqual(12, div.number_of_mandates)

    def test_setting_parties_preference(self):
        div = Division([Political_party(1, 5), Political_party(2, 7)], 2)
        div.set_party_preferences(3, [5, 6])
        div.set_party_preferences(1, [1, 2])
        self.assertEqual(1, div.parties[0].getpreferences()[0])
        self.assertEqual(2, div.parties[0].getpreferences()[1])
        with self.assertRaises(Exception):
            div.set_party_preferences(1, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
