from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    num = 0
    for alpha in col:
        num *= 26
        num += ord(alpha) - ord("A") + 1

    return num


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
