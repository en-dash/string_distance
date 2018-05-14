import numpy as np
from edit_distance import levenshtein

def test(source, target):
    n, m = len(source), len(target)

    table = np.zeros([2, m + 1])

    table[0, 0] = 0

    for j in range(1, m + 1):
        table[0, j] = table[0, j -1] + 1

    for i in range(1, n + 1):
        index = i % 2
        if index == 1:
            offset = -1
        else:
            offset = 1
        table[index, 0] = table[index + offset, 0] + 1

        for j in range(1, m + 1):
            sub = 0 if source[i - 1] == target[j - 1] else 1
            table[index, j] = min(
                table[index + offset, j] + 1,
                table[index, j - 1] + 1,
                table[index + offset, j - 1] + sub
            )

    return table[n % 2, m]

if __name__ == "__main__":
    from operator import mul
    from functools import reduce
    from itertools import combinations
    import requests
    from tqdm import tqdm
    from bs4 import BeautifulSoup
    urls = [
        'https://en.wikipedia.org/wiki/Levenshtein_distance',
        'https://en.wikipedia.org/wiki/Physics',
        'https://en.wikipedia.org/wiki/Stanford_University',
        'https://en.wikipedia.org/wiki/Carnegie_Mellon_University',
        'https://en.wikipedia.org/wiki/Neuroscience',
    ]

    for url in urls:
        text = BeautifulSoup(requests.get(url).text, 'html.parser').text.split()

        for source, target in tqdm(list(combinations(text, 2))):
            try:
                new = test(source, target)
                old = levenshtein(source, target)
                assert new == old
            except AssertionError as e:
                print(source, target)
                print(new, old)
                raise e
    print("Asserts Passed!")
