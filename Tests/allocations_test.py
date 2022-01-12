import unittest
from division import Division
from util import *


class MyTestCase(unittest.TestCase):
    def test_allocation1(self):
        parties = [("יש עתיד", 17), ("כחול לבן", 8), ("העבודה", 7), ("ימינה", 7), ("ישראל ביתנו", 7), ("מרצ", 6),
                   ("תקווה חדשה", 6), ("רעמ", 4)]
        items = ["משרד ראש הממשלה", "משרד הביטחון", "משרד האוצר", "משרד החוץ", "משרד הכלכלה והתעשייה", "משרד החינוך",
                 "משרד התרבות והספורט", "משרד הבריאות", "משרד הפנים", "משרד המשפטים", "המשרד לביטחון הפנים",
                 "משרד הרווחה והביטחון החברתי", "משרד התחבורה והבטיחות בדרכים", "המשפרד לפיתוח הפריפריה, הנגב והגליל",
                 "משרד התקשורת", "משרד הבינוי והשיכון", "משרד האנרגיה", "המשרד להגנת הסביבה", "משרד התיירות",
                 "משרד החקלאות ופיתוח הכפר", "משרד העלייה והקליטה", "המשרד לשוויון חברתי", "המשרד לשירותי דת",
                 "משרד החדשנות, המדע והטכנולוגיה", "המשרד המודיעין", "משרד ירושלים ומורשת", "המשרד לשיתוף פעולה אזורי",
                 "משרד התפוצות", "משרד ההתיישבות"]
        div = Division()
        div.add_parties(parties)
        div.add_items(items)

        div.set_party_preferences("יש עתיד", normalize(
            [27, 14, 10, 8, 7, 9, 5, 8, 8, 5, 8, 7, 5, 3, 7, 5, 4, 2, 4, 2, 3, 4, 1, 4, 7, 3, 2, 2, 3]))
        div.set_party_preferences("כחול לבן", normalize(
            [10, 15, 10, 7, 5, 8, 3, 6, 10, 7, 12, 1, 3, 3, 8, 6, 2, 1, 4, 1, 7, 2, 2, 7, 10, 2, 3, 4, 4]))
        div.set_party_preferences("העבודה", normalize(
            [1, 5, 10, 5, 4, 9, 9, 10, 9, 10, 10, 9, 7, 6, 7, 4, 8, 8, 7, 4, 3, 8, 1, 8, 3, 4, 3, 5, 4]))
        div.set_party_preferences("ימינה", normalize(
            [19, 10, 7, 8, 7, 8, 2, 6, 10, 5, 10, 3, 2, 3, 5, 4, 3, 2, 2, 1, 4, 2, 7, 7, 9, 7, 2, 1, 1]))
        div.set_party_preferences("ישראל ביתנו", normalize(
            [5, 15, 13, 9, 2, 4, 2, 4, 9, 3, 9, 6, 2, 3, 7, 4, 2, 2, 4, 2, 12, 2, 1, 4, 9, 3, 1, 7, 3]))
        div.set_party_preferences("מרצ", normalize(
            [1, 3, 7, 3, 5, 10, 7, 8, 9, 8, 6, 7, 5, 4, 7, 6, 7, 6, 6, 3, 4, 7, 1, 7, 5, 5, 3, 6, 4]))
        div.set_party_preferences("תקווה חדשה", normalize(
            [3, 10, 6, 7, 6, 7, 4, 7, 10, 4, 10, 7, 2, 3, 7, 7, 5, 4, 3, 7, 1, 7, 4, 7, 10, 7, 3, 2, 4]))
        div.set_party_preferences("רעמ", normalize(
            [1, 4, 8, 2, 4, 8, 3, 7, 7, 6, 5, 4, 5, 7, 8, 6, 4, 7, 2, 7, 2, 8, 1, 2, 4, 6, 7, 2, 2]))

        print(div.divide())

    def test_allocation2(self):
        parties = [("הליכוד", 36), ("כחול לבן", 15), ("שס", 9), ("יהדות התורה", 7), ("העבודה", 3), ("דרך ארץ", 2),
                   ("גשר", 1), ("הבית היהודי", 1)]
        items = ["משרד ראש הממשלה", "חינוך", "הגנת הסביבה", "שיתוף פעולה איזורי", "בריאות", "בינוי ושיכון", "רווחה",
                 "פיתוח הנגב ןהגליל", "תחבורה", "ביטחון פנים", "אנרגיה ומים", "מדע טכנולוגיה וחלל", "המשרד לשירותי דת"]

        div = Division()
        div.add_parties(parties)
        div.add_items(items)
        div.set_party_preferences("הליכוד", normalize([20, 8, 1, 6, 8, 8, 6, 4, 7, 10, 4, 3, 2]))
        div.set_party_preferences("כחול לבן", normalize([8, 8, 3, 8, 7, 8, 10, 4, 7, 8, 3, 4, 2]))
        div.set_party_preferences("שס", normalize([1, 10, 3, 5, 6, 5, 8, 4, 8, 3, 2, 2, 15]))
        div.set_party_preferences("יהדות התורה", normalize([1, 10, 3, 6, 8, 3, 5, 4, 8, 3, 2, 2, 15]))
        div.set_party_preferences("העבודה", normalize([1, 10, 10, 8, 9, 6, 7, 9, 7, 3, 7, 7, 4]))
        div.set_party_preferences("דרך ארץ", normalize([1, 8, 3, 8, 7, 8, 9, 4, 6, 10, 3, 5, 4]))
        div.set_party_preferences("גשר", normalize([1, 10, 9, 10, 8, 8, 8, 7, 6, 5, 8, 7, 2]))
        div.set_party_preferences("הבית היהודי", normalize([1, 9, 3, 7, 6, 8, 7, 4, 9, 9, 4, 4, 8]))

        print(div.divide())

    def test_allocation3(self):
        parties = [("הליכוד", 30), ("כולנו", 10), ("הבית היהודי", 8), ("שס", 7), ("יהדות התורה", 6), ("ישראל ביתנו", 6)]
        items = ["משרד ראש הממשלה", "חינוך", "הגנת הסביבה", "שיתוף פעולה איזורי", "בריאות", "בינוי ושיכון", "רווחה",
                 "פיתוח הנגב ןהגליל", "תחבורה", "ביטחון פנים", "אנרגיה ומים", "מדע טכנולוגיה וחלל", "המשרד לשירותי דת"]

        div = Division()
        div.add_parties(parties)
        div.add_items(items)
        div.set_party_preferences("הליכוד", normalize([20, 8, 1, 6, 8, 8, 6, 4, 7, 10, 4, 3, 2]))
        div.set_party_preferences("כולנו", normalize([2, 8, 2, 8, 5, 8, 10, 8, 8, 5, 3, 4, 5]))
        div.set_party_preferences("הבית היהודי", normalize([1, 9, 3, 7, 6, 8, 7, 4, 9, 9, 4, 4, 8]))
        div.set_party_preferences("שס", normalize([1, 10, 3, 5, 6, 5, 8, 4, 8, 3, 2, 2, 15]))
        div.set_party_preferences("יהדות התורה", normalize([1, 10, 3, 6, 8, 3, 5, 4, 8, 3, 2, 2, 15]))
        div.set_party_preferences("ישראל ביתנו", normalize([1, 7, 3, 9, 8, 8, 10, 7, 8, 10, 3, 3, 1]))

        print(div.divide())

    def test_random_allocation1(self):
        parties = [("A", 30), ("B", 15), ("C", 7)]
        items = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        div = Division()
        div.add_parties(parties)
        div.add_items(items)

        div.set_party_preferences("A", [11, 11, 5, 8, 11, 6, 15, 19, 12, 2])
        div.set_party_preferences("B", [8, 17, 13, 8, 15, 6, 7, 4, 13, 9])
        div.set_party_preferences("C", [11, 4, 10, 14, 3, 6, 10, 19, 13, 10])

        print(div.divide())

    def test_random_allocation2(self):
        parties = [("A", 30), ("B", 15), ("C", 7), ("D", 5), ("E", 5), ("F", 1)]
        items = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
        div = Division()
        div.add_parties(parties)
        div.add_items(items)

        div.set_party_preferences("A", [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences("B", [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences("C", [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])
        div.set_party_preferences("D", [7, 15, 3, 1, 5, 8, 2, 10, 10, 13, 1, 7, 6, 9, 3])
        div.set_party_preferences("E", [8, 6, 1, 2, 8, 1, 5, 15, 3, 5, 18, 9, 13, 2, 4])
        div.set_party_preferences("F", [15, 17, 1, 3, 4, 1, 1, 4, 4, 2, 20, 1, 5, 14, 8])

        print(div.divide())

    def test_random_allocation3(self):
        parties = [("A", 30), ("B", 15), ("C", 7), ("D", 5), ("E", 5), ("F", 4), ("G", 3), ("H", 1)]
        items = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]
        div = Division()
        div.add_parties(parties)
        div.add_items(items)

        div.set_party_preferences("A", [1, 1, 24, 1, 15, 20, 1, 1, 6, 1, 10, 9, 1, 1, 2, 5, 1])
        div.set_party_preferences("B", [14, 9, 7, 1, 2, 3, 2, 12, 7, 15, 6, 2, 2, 7, 3, 3, 5])
        div.set_party_preferences("C", [1, 1, 20, 1, 6, 1, 7, 1, 8, 18, 4, 1, 1, 19, 8, 2, 1])
        div.set_party_preferences("D", [1, 1, 2, 1, 3, 5, 25, 1, 6, 3, 10, 15, 11, 3, 3, 1, 9])
        div.set_party_preferences("E", [7, 19, 21, 9, 4, 1, 1, 1, 2, 1, 3, 1, 1, 1, 6, 13, 9])
        div.set_party_preferences("F", [6, 10, 10, 2, 15, 2, 6, 1, 5, 5, 2, 4, 3, 2, 5, 11, 11])
        div.set_party_preferences("G", [4, 5, 6, 16, 1, 3, 1, 4, 7, 3, 6, 17, 7, 2, 6, 11, 1])
        div.set_party_preferences("H", [1, 1, 20, 1, 2, 10, 1, 7, 25, 1, 1, 11, 3, 1, 1, 13, 1])

        print(div.divide())

    def test_small_allocation1(self):
        parties = [("A", 30), ("B", 15)]
        items = ["1", "2", "3", "4", "5"]
        div = Division()
        div.add_parties(parties)
        div.add_items(items)

        div.set_party_preferences("A", [50, 5, 15, 15, 15])
        div.set_party_preferences("B", [5, 50, 15, 15, 15])

        allo = div.divide()

        print(allo)
        # As we can see A should get item 1, B should get item 2
        allocation_matrix = bundle_to_matrix(allo)
        self.assertEqual(1., allocation_matrix[0][0][1])
        self.assertEqual(1., allocation_matrix[1][1][1])

        # A has the most mandates, therefore it should get most of 3,4 and 5
        self.assertGreaterEqual(allocation_matrix[0][3][1] + allocation_matrix[0][4][1],
                                allocation_matrix[1][3][1] + allocation_matrix[1][4][1])

    def test_small_allocation2(self):
        parties = [("A", 30), ("B", 15), ("C", 7)]
        items = ["1", "2", "3", "4", "5"]
        div = Division()
        div.add_parties(parties)
        div.add_items(items)

        div.set_party_preferences("A", [50, 5, 5, 20, 20])
        div.set_party_preferences("B", [5, 50, 5, 20, 20])
        div.set_party_preferences("C", [5, 5, 50, 20, 20])

        allo = div.divide()

        print(allo)
        # As we can see A should get item 1, B should get item 2 and C should get item 3
        allocation_matrix = bundle_to_matrix(allo)
        self.assertEqual(1., allocation_matrix[0][0][1])
        self.assertEqual(1., allocation_matrix[1][1][1])
        self.assertEqual(1., allocation_matrix[2][2][1])

        # A has the most mandates, therefore it should get a greater share of items 4 and 5
        self.assertGreaterEqual(allocation_matrix[0][3][1] + allocation_matrix[0][4][1],
                                allocation_matrix[1][3][1] + allocation_matrix[1][4][1])
        self.assertGreaterEqual(allocation_matrix[0][3][1] + allocation_matrix[0][4][1],
                                allocation_matrix[2][3][1] + allocation_matrix[2][4][1])

        # B has more mandates than C therefore, it should get a greater share of items
        self.assertGreaterEqual(allocation_matrix[1][3][1] + allocation_matrix[1][4][1],
                                allocation_matrix[2][3][1] + allocation_matrix[2][4][1])

    def test_small_allocation3(self):
        parties = [("A", 30), ("B", 15), ("C", 10), ("D", 10)]
        items = ["1", "2", "3", "4", "5"]
        div = Division()
        div.add_parties(parties)
        div.add_items(items)

        div.set_party_preferences("A", [50, 0, 0, 0, 50])
        div.set_party_preferences("B", [0, 50, 0, 0, 50])
        div.set_party_preferences("C", [0, 0, 50, 0, 50])
        div.set_party_preferences("D", [0, 0, 0, 50, 50])

        allo = div.divide()

        print(allo)
        # As we can see A should get item 1, B should get item 2, C should get item 3 and D should get item 4
        allocation_matrix = bundle_to_matrix(allo)
        self.assertEqual(1., allocation_matrix[0][0][1])
        self.assertEqual(1., allocation_matrix[1][1][1])
        self.assertEqual(1., allocation_matrix[2][2][1])
        self.assertEqual(1., allocation_matrix[3][3][1])

        # A has the most mandates, therefore it should get a greater share of item 5
        self.assertGreaterEqual(allocation_matrix[0][4][1], allocation_matrix[1][4][1])
        self.assertGreaterEqual(allocation_matrix[0][4][1], allocation_matrix[2][4][1])
        self.assertGreaterEqual(allocation_matrix[0][4][1], allocation_matrix[3][4][1])

        # B has more mandates than C and D therefore, it should get a greater share of items
        self.assertGreaterEqual(allocation_matrix[1][4][1], allocation_matrix[2][4][1])
        self.assertGreaterEqual(allocation_matrix[1][4][1], allocation_matrix[3][4][1])

        # C has more mandates than D therefore, it should get a greater share of item 5
        self.assertGreaterEqual(allocation_matrix[2][4][1], allocation_matrix[3][4][1])

    def test_algo_exceptions_less_items(self):
        parties = [("A", 30), ("B", 15), ("C", 7), ("D", 5), ("E", 5), ("F", 1)]
        items = ["1", "2", "3", "4", "5", "6"]
        div = Division()
        div.add_parties(parties)
        div.add_items(items)

        div.set_party_preferences("A", [10, 10, 7, 1, 12, 5])
        div.set_party_preferences("B", [2, 10, 11, 2, 12, 2])
        div.set_party_preferences("C", [3, 1, 3, 20, 6, 4])
        div.set_party_preferences("D", [7, 15, 3, 1, 5, 8])
        div.set_party_preferences("E", [8, 6, 1, 2, 8, 1])
        div.set_party_preferences("F", [15, 17, 1, 3, 4, 1])

        print(div.divide())

    def test_algo_exceptions_equal_mandates(self):
        parties = [("A", 10), ("B", 10), ("C", 10), ("D", 10), ("E", 10), ("F", 10)]
        items = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
        div = Division()
        div.add_parties(parties)
        div.add_items(items)

        div.set_party_preferences("A", [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences("B", [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences("C", [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])
        div.set_party_preferences("D", [7, 15, 3, 1, 5, 8, 2, 10, 10, 13, 1, 7, 6, 9, 3])
        div.set_party_preferences("E", [8, 6, 1, 2, 8, 1, 5, 15, 3, 5, 18, 9, 13, 2, 4])
        div.set_party_preferences("F", [15, 17, 1, 3, 4, 1, 1, 4, 4, 2, 20, 1, 5, 14, 8])

        print(div.divide())

    def test_algo_exceptions_not_big_difference_in_mandates(self):
        parties = [("A", 10), ("B", 9), ("C", 8), ("D", 7), ("E", 6), ("F", 5)]
        items = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
        div = Division()
        div.add_parties(parties)
        div.add_items(items)

        div.set_party_preferences("A", [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences("B", [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences("C", [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])
        div.set_party_preferences("D", [7, 15, 3, 1, 5, 8, 2, 10, 10, 13, 1, 7, 6, 9, 3])
        div.set_party_preferences("E", [8, 6, 1, 2, 8, 1, 5, 15, 3, 5, 18, 9, 13, 2, 4])
        div.set_party_preferences("F", [15, 17, 1, 3, 4, 1, 1, 4, 4, 2, 20, 1, 5, 14, 8])

        print(div.divide())

    def test_algo_exceptions_mid_difference_in_mandates(self):
        parties = [("A", 10), ("B", 5), ("C", 5), ("D", 5), ("E", 1), ("F", 1)]
        items = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
        div = Division()
        div.add_parties(parties)
        div.add_items(items)

        div.set_party_preferences("A", [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences("B", [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences("C", [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])
        div.set_party_preferences("D", [7, 15, 3, 1, 5, 8, 2, 10, 10, 13, 1, 7, 6, 9, 3])
        div.set_party_preferences("E", [8, 6, 1, 2, 8, 1, 5, 15, 3, 5, 18, 9, 13, 2, 4])
        div.set_party_preferences("F", [15, 17, 1, 3, 4, 1, 1, 4, 4, 2, 20, 1, 5, 14, 8])

        print(div.divide())

    def test_algo_exceptions_mid_difference_in_mandates2(self):
        parties = [("A", 10), ("B", 5), ("C", 5), ("D", 5), ("E", 2), ("F", 1)]
        items = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
        div = Division()
        div.add_parties(parties)
        div.add_items(items)

        div.set_party_preferences("A", [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences("B", [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences("C", [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])
        div.set_party_preferences("D", [7, 15, 3, 1, 5, 8, 2, 10, 10, 13, 1, 7, 6, 9, 3])
        div.set_party_preferences("E", [8, 6, 1, 2, 8, 1, 5, 15, 3, 5, 18, 9, 13, 2, 4])
        div.set_party_preferences("F", [15, 17, 1, 3, 4, 1, 1, 4, 4, 2, 20, 1, 5, 14, 8])

        print(div.divide())

    def test_algo_exception_small_number_of_parties1(self):
        parties = [("A", 19), ("B", 5), ("C", 5)]
        items = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
        div = Division()
        div.add_parties(parties)
        div.add_items(items)

        div.set_party_preferences("A", [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences("B", [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences("C", [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])

        print(div.divide())

    def test_algo_exception_small_number_of_parties2(self):
        parties = [("A", 20), ("B", 5), ("C", 5)]
        items = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
        div = Division()
        div.add_parties(parties)
        div.add_items(items)

        div.set_party_preferences("A", [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences("B", [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences("C", [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])

        print(div.divide())

    def test_algo_exception_small_number_of_parties3(self):
        parties = [("A", 4), ("B", 1), ("C", 1)]
        items = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
        div = Division()
        div.add_parties(parties)
        div.add_items(items)

        div.set_party_preferences("A", [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences("B", [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences("C", [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])

        print(div.divide())

    def test_algo_exception_small_number_of_parties4(self):
        parties = [("A", 3), ("B", 1), ("C", 1)]
        items = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
        div = Division()
        div.add_parties(parties)
        div.add_items(items)

        div.set_party_preferences("A", [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences("B", [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences("C", [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])

        print(div.divide())

    def test_algo_exception_2_parties(self):
        parties = [("A", 119), ("B", 1)]
        items = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
        div = Division()
        div.add_parties(parties)
        div.add_items(items)

        div.set_party_preferences("A", [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences("B", [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])

        print(div.divide())


if __name__ == '__main__':
    unittest.main()
