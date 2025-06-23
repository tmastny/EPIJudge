from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(
    final_score: int, individual_play_scores: List[int]
) -> int:
    dp = [
        [0 for _ in range(final_score + 1)] 
        for _ in range(len(individual_play_scores))
    ]
    
    for r in range(len(dp)):
        dp[r][0] = 1
        
    for total_score in range(len(dp[0])):
        play_score = individual_play_scores[0]
        if total_score >= play_score:
            dp[0][total_score] = dp[0][total_score - play_score]
    
    for r in range(len(dp)):
        play_score = individual_play_scores[r]
        for total_score in range(len(dp[0])):
            dp[r][total_score] = dp[r - 1][total_score]
            if total_score >= play_score:
                dp[r][total_score] += dp[r][total_score - play_score]
    
    return dp[-1][-1]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "number_of_score_combinations.py",
            "number_of_score_combinations.tsv",
            num_combinations_for_final_score,
        )
    )
