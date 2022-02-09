import unittest
from algo_side.division import Division
from algo_side.political_party import Political_party
from algo_side.division_item import Division_item


class MyTestCase(unittest.TestCase):
    def test_creation(self):
        div = Division()
        self.assertEqual([], div.items)
        self.assertEqual([], div.parties)
        self.assertEqual(0, div.num_of_items)
        self.assertEqual(0, div.num_of_parties)
        self.assertEqual(0, div.number_of_mandates)
        div = Division([Political_party("A", 5), Political_party("B", 7)], ["Item 1", "Item 2"])
        self.assertEqual(["Item 1", "Item 2"], div.items)
        self.assertEqual(["A", "B"], div.parties)
        self.assertEqual([Political_party("A", 5), Political_party("B", 7)], div.parties)
        self.assertEqual(2, div.num_of_items)
        self.assertEqual(2, div.num_of_parties)
        self.assertEqual(12, div.number_of_mandates)
        with self.assertRaises(Exception):
            div = Division([Political_party("A", 121)])

    def test_item_addition_removal(self):
        div = Division()
        div.add_item("Item 1")
        div.add_item("Item 2")
        self.assertEqual(["Item 1", "Item 2"], div.items)
        self.assertEqual(2, div.num_of_items)
        div.remove_item("Item 2")
        div.remove_item("Item 3")
        self.assertEqual(["Item 1"], div.items)
        self.assertEqual(1, div.num_of_items)
        div.add_items(["Item 1", "Item 2", "Item 3"])
        self.assertEqual(["Item 1", "Item 2", "Item 3"], div.items)
        self.assertEqual(3, div.num_of_items)
        div.remove_items(["Item 2", "Item 3", "Item 4"])
        self.assertEqual(["Item 1"], div.items)
        self.assertEqual(1, div.num_of_items)

    def test_political_party_addition_removal(self):
        div = Division([Political_party("A", 5), Political_party("B", 7)])
        div.add_party("C", 6)
        self.assertEqual(["A", "B", "C"], div.parties)
        self.assertEqual(3, div.num_of_parties)
        self.assertEqual(18, div.number_of_mandates)
        div.add_party("A", 5)
        self.assertEqual(3, div.num_of_parties)
        self.assertEqual(18, div.number_of_mandates)
        div.add_parties([("A", 5), ("D", 5), ("E", 5)])
        self.assertEqual(["A", "B", "C", "D", "E"], div.parties)
        self.assertEqual(5, div.num_of_parties)
        self.assertEqual(28, div.number_of_mandates)
        div.remove_party("F")
        div.remove_party("C")
        self.assertEqual(["A", "B", "D", "E"], div.parties)
        self.assertEqual(4, div.num_of_parties)
        self.assertEqual(22, div.number_of_mandates)
        div.remove_parties(["D", "E", "F"])
        self.assertEqual(["A", "B"], div.parties)
        self.assertEqual(2, div.num_of_parties)
        self.assertEqual(12, div.number_of_mandates)
        with self.assertRaises(Exception):
            div.add_party("G", 121)

    def test_setting_parties_preference(self):
        div = Division([Political_party("A", 5), Political_party("B", 7)], [Division_item("Item 1"), Division_item("Item 2")])
        div.set_party_preferences("C", [5, 6])
        div.set_party_preferences("A", [1, 2])
        self.assertEqual(1, div.parties[0].getpreferences()[0])
        self.assertEqual(2, div.parties[0].getpreferences()[1])
        with self.assertRaises(Exception):
            div.set_party_preferences("A", [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
