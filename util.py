def normalize(lst: list):
    s = sum(lst)
    return [round(100 * i / s, 2) for i in lst]


def bundle_to_matrix(allocation):
    return [list(bundle.enumerate_fractions()) for bundle in allocation]
