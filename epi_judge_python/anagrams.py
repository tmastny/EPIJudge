from typing import List

from test_framework import generic_test, test_utils

from collections import defaultdict

def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)
    for word in dictionary:
        key = "".join(sorted(word))
        anagrams[key].append(word)

    return [words for words in anagrams.values() if len(words) > 1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
