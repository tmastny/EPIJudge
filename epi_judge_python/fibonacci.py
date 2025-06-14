from test_framework import generic_test


def fibonacci_space_n(n: int) -> int:
    dp = [0] * ((n + 1) + 2)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    
    prev = 0
    curr = 1
    for i in range(2, n + 1):
        next_prev = curr
        curr += prev
        prev = next_prev
         
    return curr



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
