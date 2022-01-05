def normalize(lst: list):
    s = sum(lst)
    return [round(100 * i / s, 2) for i in lst]
