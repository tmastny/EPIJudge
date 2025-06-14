from test_framework import generic_test

coins = [100, 50, 25, 10, 5, 1]

def change_making(cents: int) -> int:
    change = 0
    for coin in coins:
        n = cents // coin
        cents -= n * coin

        change += n

    return change


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('making_change.py', 'making_change.tsv',
                                       change_making))
