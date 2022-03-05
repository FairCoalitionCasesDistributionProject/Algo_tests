import unittest
from algo_side.division import Division
from algo_side.util import *

def get_utility(preferences: list, allocation: list):
    return sum([preferences[i]*allocation[i] for i in range(len(preferences))])

class MyTestCase(unittest.TestCase):        
    def test_allocation1(self):
        # parties_names = ["יש עתיד", "כחול לבן", "העבודה", "ימינה", "ישראל ביתנו", "מרצ", "תקווה חדשה", "רעמ"]
        # items = ["משרד ראש הממשלה", "משרד הביטחון", "משרד האוצר", "משרד החוץ", "משרד הכלכלה והתעשייה", "משרד החינוך",
        #          "משרד התרבות והספורט", "משרד הבריאות", "משרד הפנים", "משרד המשפטים", "המשרד לביטחון הפנים",
        #          "משרד הרווחה והביטחון החברתי", "משרד התחבורה והבטיחות בדרכים", "המשפרד לפיתוח הפריפריה, הנגב והגליל",
        #          "משרד התקשורת", "משרד הבינוי והשיכון", "משרד האנרגיה", "המשרד להגנת הסביבה", "משרד התיירות",
        #          "משרד החקלאות ופיתוח הכפר", "משרד העלייה והקליטה", "המשרד לשוויון חברתי", "המשרד לשירותי דת",
        #          "משרד החדשנות, המדע והטכנולוגיה", "המשרד המודיעין", "משרד ירושלים ומורשת", "המשרד לשיתוף פעולה אזורי",
        #          "משרד התפוצות", "משרד ההתיישבות"]

        mandates = [17, 8, 7, 7, 7, 6, 6, 4]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(number_of_items=29)
        div.add_parties(parties)
        div.set_party_preferences(0,[27, 14, 10, 8, 7, 9, 5, 8, 8, 5, 8, 7, 5, 3, 7, 5, 4, 2, 4, 2, 3, 4, 1, 4, 7, 3, 2, 2, 3])
        div.set_party_preferences(1, [10, 15, 10, 7, 5, 8, 3, 6, 10, 7, 12, 1, 3, 3, 8, 6, 2, 1, 4, 1, 7, 2, 2, 7, 10, 2, 3, 4, 4])
        div.set_party_preferences(2, [1, 5, 10, 5, 4, 9, 9, 10, 9, 10, 10, 9, 7, 6, 7, 4, 8, 8, 7, 4, 3, 8, 1, 8, 3, 4, 3, 5, 4])
        div.set_party_preferences(3, [19, 10, 7, 8, 7, 8, 2, 6, 10, 5, 10, 3, 2, 3, 5, 4, 3, 2, 2, 1, 4, 2, 7, 7, 9, 7, 2, 1, 1])
        div.set_party_preferences(4, [5, 15, 13, 9, 2, 4, 2, 4, 9, 3, 9, 6, 2, 3, 7, 4, 2, 2, 4, 2, 12, 2, 1, 4, 9, 3, 1, 7, 3])
        div.set_party_preferences(5, [1, 3, 7, 3, 5, 10, 7, 8, 9, 8, 6, 7, 5, 4, 7, 6, 7, 6, 6, 3, 4, 7, 1, 7, 5, 5, 3, 6, 4])
        div.set_party_preferences(6, [3, 10, 6, 7, 6, 7, 4, 7, 10, 4, 10, 7, 2, 3, 7, 7, 5, 4, 3, 7, 1, 7, 4, 7, 10, 7, 3, 2, 4])
        div.set_party_preferences(7, [1, 4, 8, 2, 4, 8, 3, 7, 7, 6, 5, 4, 5, 7, 8, 6, 4, 7, 2, 7, 2, 8, 1, 2, 4, 6, 7, 2, 2])
        bun_allo = div.divide()
        print(div.divide())
        mat_allo = bundle_to_matrix(bun_allo)
        # Check that everyone party i got at least mandates[i] * n / sum_j(mandates[j])
        for i in range(len(mandates)):
            self.assertGreaterEqual(get_utility(mat_allo[i], div.get_preferences()[i]), (sum(div.get_preferences()[i])*mandates[i])/div.number_of_mandates)


    def test_allocation2(self):
    #     parties = [("הליכוד", 36), ("כחול לבן", 15), ("שס", 9), ("יהדות התורה", 7), ("העבודה", 3), ("דרך ארץ", 2),
    #                ("גשר", 1), ("הבית היהודי", 1)]
    #     items = ["משרד ראש הממשלה", "חינוך", "הגנת הסביבה", "שיתוף פעולה איזורי", "בריאות", "בינוי ושיכון", "רווחה",
    #              "פיתוח הנגב ןהגליל", "תחבורה", "ביטחון פנים", "אנרגיה ומים", "מדע טכנולוגיה וחלל", "המשרד לשירותי דת"]
        mandates = [36, 15, 9, 7, 3, 2, 1, 1]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(13)
        div.add_parties(parties)
        div.set_party_preferences(0, [20, 8, 1, 6, 8, 8, 6, 4, 7, 10, 4, 3, 2])
        div.set_party_preferences(1, [8, 8, 3, 8, 7, 8, 10, 4, 7, 8, 3, 4, 2])
        div.set_party_preferences(2, [1, 10, 3, 5, 6, 5, 8, 4, 8, 3, 2, 2, 15])
        div.set_party_preferences(3, [1, 10, 3, 6, 8, 3, 5, 4, 8, 3, 2, 2, 15])
        div.set_party_preferences(4, [1, 10, 10, 8, 9, 6, 7, 9, 7, 3, 7, 7, 4])
        div.set_party_preferences(5, [1, 8, 3, 8, 7, 8, 9, 4, 6, 10, 3, 5, 4])
        div.set_party_preferences(6, [1, 10, 9, 10, 8, 8, 8, 7, 6, 5, 8, 7, 2])
        div.set_party_preferences(7, [1, 9, 3, 7, 6, 8, 7, 4, 9, 9, 4, 4, 8])
        bun_allo = div.divide()
        print(div.divide())
        mat_allo = bundle_to_matrix(bun_allo)
        for i in range(len(mandates)):
            self.assertGreaterEqual(get_utility(mat_allo[i], div.get_preferences()[i]), (sum(div.get_preferences()[i])*mandates[i])/div.number_of_mandates)


    def test_allocation3(self):
        # parties = [("הליכוד", 30), ("כולנו", 10), ("הבית היהודי", 8), ("שס", 7), ("יהדות התורה", 6), ("ישראל ביתנו", 6)]
        # items = ["משרד ראש הממשלה", "חינוך", "הגנת הסביבה", "שיתוף פעולה איזורי", "בריאות", "בינוי ושיכון", "רווחה",
        #          "פיתוח הנגב ןהגליל", "תחבורה", "ביטחון פנים", "אנרגיה ומים", "מדע טכנולוגיה וחלל", "המשרד לשירותי דת"]
        mandates = [30, 10, 8, 7, 6, 6]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(13)
        div.add_parties(parties)
        div.set_party_preferences(0, [20, 8, 1, 6, 8, 8, 6, 4, 7, 10, 4, 3, 2])
        div.set_party_preferences(1, [2, 8, 2, 8, 5, 8, 10, 8, 8, 5, 3, 4, 5])
        div.set_party_preferences(2, [1, 9, 3, 7, 6, 8, 7, 4, 9, 9, 4, 4, 8])
        div.set_party_preferences(3, [1, 10, 3, 5, 6, 5, 8, 4, 8, 3, 2, 2, 15])
        div.set_party_preferences(4, [1, 10, 3, 6, 8, 3, 5, 4, 8, 3, 2, 2, 15])
        div.set_party_preferences(5, [1, 7, 3, 9, 8, 8, 10, 7, 8, 10, 3, 3, 1])
        bun_allo = div.divide()
        print(div.divide())
        mat_allo = bundle_to_matrix(bun_allo)
        for i in range(len(mandates)):
            self.assertGreaterEqual(get_utility(mat_allo[i], div.get_preferences()[i]), (sum(div.get_preferences()[i])*mandates[i])/div.number_of_mandates)


    def test_random_allocation1(self):
        mandates = [30, 15, 7]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(10)
        div.add_parties(parties)
        div.set_party_preferences(0, [11, 11, 5, 8, 11, 6, 15, 19, 12, 2])
        div.set_party_preferences(1, [8, 17, 13, 8, 15, 6, 7, 4, 13, 9])
        div.set_party_preferences(2, [11, 4, 10, 14, 3, 6, 10, 19, 13, 10])
        bun_allo = div.divide()
        print(div.divide())
        mat_allo = bundle_to_matrix(bun_allo)
        for i in range(len(mandates)):
            self.assertGreaterEqual(get_utility(mat_allo[i], div.get_preferences()[i]), (sum(div.get_preferences()[i])*mandates[i])/div.number_of_mandates)


    def test_random_allocation2(self):
        mandates = [30, 15, 7, 5, 5, 1]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(15)
        div.add_parties(parties)
        div.set_party_preferences(0, [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences(1, [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences(2, [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])
        div.set_party_preferences(3, [7, 15, 3, 1, 5, 8, 2, 10, 10, 13, 1, 7, 6, 9, 3])
        div.set_party_preferences(4, [8, 6, 1, 2, 8, 1, 5, 15, 3, 5, 18, 9, 13, 2, 4])
        div.set_party_preferences(5, [15, 17, 1, 3, 4, 1, 1, 4, 4, 2, 20, 1, 5, 14, 8])
        bun_allo = div.divide()
        print(div.divide())
        mat_allo = bundle_to_matrix(bun_allo)
        for i in range(len(mandates)):
            self.assertGreaterEqual(get_utility(mat_allo[i], div.get_preferences()[i]), (sum(div.get_preferences()[i])*mandates[i])/div.number_of_mandates)


    def test_random_allocation3(self):
        mandates = [30, 15, 7, 5, 5, 4, 3, 1]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(17)
        div.add_parties(parties)
        div.set_party_preferences(0, [1, 1, 24, 1, 15, 20, 1, 1, 6, 1, 10, 9, 1, 1, 2, 5, 1])
        div.set_party_preferences(1, [14, 9, 7, 1, 2, 3, 2, 12, 7, 15, 6, 2, 2, 7, 3, 3, 5])
        div.set_party_preferences(2, [1, 1, 20, 1, 6, 1, 7, 1, 8, 18, 4, 1, 1, 19, 8, 2, 1])
        div.set_party_preferences(3, [1, 1, 2, 1, 3, 5, 25, 1, 6, 3, 10, 15, 11, 3, 3, 1, 9])
        div.set_party_preferences(4, [7, 19, 21, 9, 4, 1, 1, 1, 2, 1, 3, 1, 1, 1, 6, 13, 9])
        div.set_party_preferences(5, [6, 10, 10, 2, 15, 2, 6, 1, 5, 5, 2, 4, 3, 2, 5, 11, 11])
        div.set_party_preferences(6, [4, 5, 6, 16, 1, 3, 1, 4, 7, 3, 6, 17, 7, 2, 6, 11, 1])
        div.set_party_preferences(7, [1, 1, 20, 1, 2, 10, 1, 7, 25, 1, 1, 11, 3, 1, 1, 13, 1])
        bun_allo = div.divide()
        print(div.divide())
        mat_allo = bundle_to_matrix(bun_allo)
        for i in range(len(mandates)):
            self.assertGreaterEqual(get_utility(mat_allo[i], div.get_preferences()[i]), (sum(div.get_preferences()[i])*mandates[i])/div.number_of_mandates)

        
    def test_small_allocation1(self):
        mandates  = [30, 15]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(5)
        div.add_parties(parties)
        div.set_party_preferences(0, [50, 5, 15, 15, 15])
        div.set_party_preferences(1, [5, 50, 15, 15, 15])
        allo = div.divide()

        # As we can see A should get item 1, B should get most of item 2
        allocation_matrix = bundle_to_matrix(allo)
        self.assertEqual(1., allocation_matrix[0][0])
        self.assertGreaterEqual(allocation_matrix[1][1], 0.9)
        
        # A has the most mandates, therefore it should get most of 3,4 and 5
        self.assertGreaterEqual(allocation_matrix[0][3] + allocation_matrix[0][4],
                                allocation_matrix[1][3] + allocation_matrix[1][4])

    def test_small_allocation2(self):
        mandates = [30, 15, 7]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(5)
        div.add_parties(parties)

        div.set_party_preferences(0, [50, 5, 5, 20, 20])
        div.set_party_preferences(1, [5, 50, 5, 20, 20])
        div.set_party_preferences(2, [5, 5, 50, 20, 20])

        allo = div.divide()

        print(allo)
        # As we can see A should get item 1 and B should get most of item 2
        allocation_matrix = bundle_to_matrix(allo)
        self.assertEqual(1., allocation_matrix[0][0])
        self.assertGreaterEqual(allocation_matrix[1][1], 0.9)

        # A has the most mandates, therefore it should get a greater share of items 4 and 5
        self.assertGreaterEqual(allocation_matrix[0][3] + allocation_matrix[0][4],
                                allocation_matrix[1][3] + allocation_matrix[1][4])
        self.assertGreaterEqual(allocation_matrix[0][3] + allocation_matrix[0][4],
                                allocation_matrix[2][3] + allocation_matrix[2][4])

        # B has more mandates than C therefore, it should get a greater share of items
        self.assertGreaterEqual(allocation_matrix[1][3] + allocation_matrix[1][4],
                                allocation_matrix[2][3] + allocation_matrix[2][4])

    def test_small_allocation3(self):
        mandates = [30, 15, 10, 5]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(6)
        div.add_parties(parties)
        div.set_party_preferences(0, [50, 0, 0, 0, 25, 25])
        div.set_party_preferences(1, [0, 50, 0, 0, 25, 25])
        div.set_party_preferences(2, [0, 0, 50, 0, 25, 25])
        div.set_party_preferences(3, [0, 0, 0, 50, 25, 25])
        allo = div.divide()

        print(allo)
        # As we can see A should get item 1, B should get item 2, C should get item 3 and D should get item 4
        allocation_matrix = bundle_to_matrix(allo)
        self.assertEqual(1., allocation_matrix[0][0])
        self.assertEqual(1., allocation_matrix[1][1])
        self.assertEqual(1., allocation_matrix[2][2])
        self.assertEqual(1., allocation_matrix[3][3])

        # A has the most mandates, therefore it should get a greater share of item 5
        self.assertGreaterEqual(allocation_matrix[0][4] + allocation_matrix[0][5], allocation_matrix[1][4] + allocation_matrix[1][5])
        self.assertGreaterEqual(allocation_matrix[0][4] + allocation_matrix[0][5], allocation_matrix[2][4] + allocation_matrix[2][5])
        self.assertGreaterEqual(allocation_matrix[0][4] + allocation_matrix[0][5], allocation_matrix[3][4] + allocation_matrix[3][5])

        # B has more mandates than C and D therefore, it should get a greater share of items
        self.assertGreaterEqual(allocation_matrix[1][4] + allocation_matrix[1][5], allocation_matrix[2][4] + allocation_matrix[2][5])
        self.assertGreaterEqual(allocation_matrix[1][4] + allocation_matrix[1][5], allocation_matrix[3][4] + allocation_matrix[3][5])

        # C has more mandates than D therefore, it should get a greater share of item 5
        self.assertGreaterEqual(allocation_matrix[2][4] + allocation_matrix[2][5], allocation_matrix[3][4] + allocation_matrix[3][5])

    def test_algo_exceptions_less_items(self):
        mandates = [30, 15, 7, 5, 5, 1]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(6)
        div.add_parties(parties)

        div.set_party_preferences(0, [10, 10, 7, 1, 12, 5])
        div.set_party_preferences(1, [2, 10, 11, 2, 12, 2])
        div.set_party_preferences(2, [3, 1, 3, 20, 6, 4])
        div.set_party_preferences(3, [7, 15, 3, 1, 5, 8])
        div.set_party_preferences(4, [8, 6, 1, 2, 8, 1])
        div.set_party_preferences(5, [15, 17, 1, 3, 4, 1])
        print(div.divide())

    def test_algo_exceptions_equal_mandates(self):
        mandates = [10, 10, 10, 10, 10, 10]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(15)
        div.add_parties(parties)

        div.set_party_preferences(0, [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences(1, [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences(2, [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])
        div.set_party_preferences(3, [7, 15, 3, 1, 5, 8, 2, 10, 10, 13, 1, 7, 6, 9, 3])
        div.set_party_preferences(4, [8, 6, 1, 2, 8, 1, 5, 15, 3, 5, 18, 9, 13, 2, 4])
        div.set_party_preferences(5, [15, 17, 1, 3, 4, 1, 1, 4, 4, 2, 20, 1, 5, 14, 8])

        print(div.divide())

    def test_algo_exceptions_not_big_difference_in_mandates(self):
        mandates = [10, 9, 8, 7, 6, 5]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(15)
        div.add_parties(parties)

        div.set_party_preferences(0, [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences(1, [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences(2, [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])
        div.set_party_preferences(3, [7, 15, 3, 1, 5, 8, 2, 10, 10, 13, 1, 7, 6, 9, 3])
        div.set_party_preferences(4, [8, 6, 1, 2, 8, 1, 5, 15, 3, 5, 18, 9, 13, 2, 4])
        div.set_party_preferences(5, [15, 17, 1, 3, 4, 1, 1, 4, 4, 2, 20, 1, 5, 14, 8])

        print(div.divide())

    def test_algo_exceptions_mid_difference_in_mandates(self):
        mandates = [10, 5, 5, 5, 1, 1]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(15)
        div.add_parties(parties)

        div.set_party_preferences(0, [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences(1, [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences(2, [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])
        div.set_party_preferences(3, [7, 15, 3, 1, 5, 8, 2, 10, 10, 13, 1, 7, 6, 9, 3])
        div.set_party_preferences(4, [8, 6, 1, 2, 8, 1, 5, 15, 3, 5, 18, 9, 13, 2, 4])
        div.set_party_preferences(5, [15, 17, 1, 3, 4, 1, 1, 4, 4, 2, 20, 1, 5, 14, 8])

        print(div.divide())

    def test_algo_exceptions_mid_difference_in_mandates2(self):
        mandates = [10, 5, 5, 5, 2, 1]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(15)
        div.add_parties(parties)

        div.set_party_preferences(0, [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences(1, [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences(2, [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])
        div.set_party_preferences(3, [7, 15, 3, 1, 5, 8, 2, 10, 10, 13, 1, 7, 6, 9, 3])
        div.set_party_preferences(4, [8, 6, 1, 2, 8, 1, 5, 15, 3, 5, 18, 9, 13, 2, 4])
        div.set_party_preferences(5, [15, 17, 1, 3, 4, 1, 1, 4, 4, 2, 20, 1, 5, 14, 8])


    def test_algo_exception_small_number_of_parties1(self):
        mandates = [19, 5, 5]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(15)
        div.add_parties(parties)

        div.set_party_preferences(0, [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences(1, [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences(2, [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])


    def test_algo_exception_small_number_of_parties2(self):
        mandates = [20, 5, 5]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(15)
        div.add_parties(parties)

        div.set_party_preferences(0, [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences(1, [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences(2, [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])


    def test_algo_exception_small_number_of_parties3(self):
        mandates = [4, 1, 1]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(15)
        div.add_parties(parties)

        div.set_party_preferences(0, [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences(1, [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences(2, [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])


    def test_algo_exception_small_number_of_parties4(self):
        mandates = [3, 1, 1]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(15)
        div.add_parties(parties)

        div.set_party_preferences(0, [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences(1, [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])
        div.set_party_preferences(2, [3, 1, 3, 20, 6, 4, 5, 10, 6, 7, 6, 5, 11, 7, 6])


    def test_algo_exception_2_parties(self):
        mandates = [119, 1]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(15)
        div.add_parties(parties)

        div.set_party_preferences(0, [10, 10, 7, 1, 12, 5, 3, 14, 5, 5, 6, 13, 2, 5, 2])
        div.set_party_preferences(1, [2, 10, 11, 2, 12, 2, 7, 9, 13, 2, 15, 1, 2, 4, 8])

        print(div.divide())

    def test_empty_allocation(self):
        mandates = [100, 10]
        parties = [(i, mandates[i]) for i in range(len(mandates))]
        div = Division(4)
        div.add_parties(parties)
        div.set_party_preferences(0, [0, 0, 0, 0])
        div.set_party_preferences(1, [1, 1, 1, 1])
        # As the first one doesn't want anything, the second one should get everything.
        self.assertEqual(bundle_to_matrix(div.divide())[1], [1.0, 1.0, 1.0, 1.0])

    def test_single_party(self):
        div = Division(4)
        div.add_party(0, 1)
        div.set_party_preferences(0, [1, 1, 1, 1])
        self.assertEqual(bundle_to_matrix(div.divide())[0], [1.0, 1.0, 1.0, 1.0])


if __name__ == '__main__':
    unittest.main()
