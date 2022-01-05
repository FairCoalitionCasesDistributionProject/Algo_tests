from division import Division
from fairpy.items.bounded_sharing import *
from political_party import Political_party
from util import *
from division_item import Division_item


def main():
    # div = Division(
    #     [Political_party("A", 10), Political_party("B", 7), Political_party("C", 7), Political_party("D", 5)],
    #     [Division_item("Item 1"), Division_item("Item 2"), Division_item("Item 3"), Division_item("Item 4"),
    #      Division_item("Item 5")])
    # div.set_party_preferences("A", [25, 10.11, 15.311, 15.11, 35])
    # div.set_party_preferences("B", [10, 40, 5, 20.41, 25])
    # div.set_party_preferences("C", [25, 10, 15, 15, 35])
    # div.set_party_preferences("D", [25, 10, 15, 15, 35])
    #
    # print(div.divide())
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
        [20, 14, 10, 8, 7, 9, 5, 8, 8, 5, 8, 7, 5, 3, 7, 5, 4, 2, 4, 2, 3, 4, 1, 4, 7, 3, 2, 2, 3]))
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
        [3, 10, 6, 4, 5, 6, 7, 8, 9, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    div.set_party_preferences("רעמ", normalize(
        [1, 4, 8, 4, 5, 6, 7, 8, 9, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

    print([party.getpreferences() for party in div.get_parties()])
    print(div.divide())


if __name__ == '__main__':
    main()
