from test_framework import generic_test


def power(x: float, y: int) -> float:
    positive = y >= 0
    y = abs(y)
    
    pow = 1
    while y:
        if y & 1:
            pow *= x
        x *= x
        y >>= 1

    return pow if positive else 1 / pow


if __name__ == "__main__":
    generic_test.generic_test_main("power_x_y.py", "power_x_y.tsv", power)
