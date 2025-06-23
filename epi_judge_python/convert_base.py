from test_framework import generic_test

def convert_char(char: str) -> int:
    k = ord(char) - ord('0')
    return k if k <= 9 else k - 7

def convert_int(k: int) -> str:
    if k > 9:
        k += 7

    return chr(k + ord('0'))

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    start = 0
    if num_as_string[0] == "-":
        start = 1
    
    n = 0
    for i in range(start, len(num_as_string)):
        n *= b1
        n += convert_char(num_as_string[i])

    num = []
    while True:
        num.append(convert_int(n % b2))
        n //= b2
        if n == 0:
            break

    if start:
        num.append("-")
    
    num.reverse()
    return "".join(num)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
