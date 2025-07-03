from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    dp = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]

    for r in range(len(dp)):
        dp[r][0] = r

    for c in range(len(dp[0])):
        dp[0][c] = c

    for r in range(1, len(dp)):
        for c in range(1, len(dp[0])):
            dp[r][c] = min(
                dp[r][c - 1] + 1,
                dp[r - 1][c] + 1,
                dp[r - 1][c - 1] + (0 if B[r - 1] == A[c - 1] else 1)
            )

    return dp[-1][-1]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "levenshtein_distance.py", "levenshtein_distance.tsv", levenshtein_distance
        )
    )
