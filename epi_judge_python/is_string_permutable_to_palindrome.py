from test_framework import generic_test

from collections import Counter

def can_form_palindrome(s: str) -> bool:
    letter_freq = Counter(s)
    
    odd = 0
    for freq in letter_freq.values():
        if freq % 2 == 1:
            odd += 1
       
    return odd <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
