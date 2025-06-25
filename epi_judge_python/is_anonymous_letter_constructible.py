from test_framework import generic_test

from collections import Counter

def is_letter_constructible_from_magazine(letter_text: str, magazine_text: str) -> bool:
    letter_freq = Counter(letter_text)
    magazine_freq = Counter(magazine_text)
    
    for letter, count in letter_freq.items():
        if letter in magazine_freq and magazine_freq[letter] >= count:
            continue
        
        return False
    
    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_anonymous_letter_constructible.py",
            "is_anonymous_letter_constructible.tsv",
            is_letter_constructible_from_magazine,
        )
    )
