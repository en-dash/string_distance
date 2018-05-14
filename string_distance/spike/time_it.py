import requests
from bs4 import BeautifulSoup

source = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/Levenshtein_distance').text, 'html.parser').text
target = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/Physics').text, 'html.parser').text

from edit_distance import levenshtein, levenshtein_small

import time

t0 = time.time()
levenshtein(source, target)
print(time.time() - t0)

t0 = time.time()
levenshtein_small(source, target)
print(time.time() - t0)
