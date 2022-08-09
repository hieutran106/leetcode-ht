import re

def extract_data2(s):
    pattern = re.compile(r"""\|\s*                 # opening bar and whitespace
                             '(?P<name>.*?)'       # quoted name
                             \s*\|\s*(?P<n1>.*?)   # whitespace, next bar, n1
                             \s*\|\s*(?P<n2>.*?)   # whitespace, next bar, n2
                             \s*\|""", re.VERBOSE)
    match = pattern.match(s)

    name = match.group("name")
    n1 = float(match.group("n1"))
    n2 = float(match.group("n2"))

    return (name, n1, n2)

if __name__ == "__main__":
    tests = [
        "| 'TOMATOES_PICKED'                                  |       914 |       1397 |",
        "| 'TOMATOES_FLICKED'                                 |     32914 |       1123 |",
        "| 'TOMATOES_RIGGED'                                  |        14 |       1343 |",
        "| 'TOMATOES_PICKELED'                                |         4 |         23 |"]

    for test in tests:
        (name, n1, n2) = extract_data2(test)
        print(extract_data2(test))