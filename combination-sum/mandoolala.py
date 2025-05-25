from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        combination = []

        def backtracking(start_idx, cur_sum):
            if cur_sum > target:
                return
            if cur_sum == target:
                return output.append(list(combination))

            for i in range(start_idx, len(candidates)):
                combination.append(candidates[i])
                backtracking(i, cur_sum + candidates[i])
                combination.pop()

        backtracking(0, 0)
        return output
