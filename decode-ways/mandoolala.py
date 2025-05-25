class Solution:
    def numDecodings(self, s: str) -> int:
        # memo[start_idx] = number of ways to decode s[start_idx:]
        memo = {}

        def backtracking(start_idx):
            if start_idx == len(s):
                return 1
            if s[start_idx] == '0':
                return 0
            if start_idx in memo:
                return memo[start_idx]

            total = backtracking(start_idx + 1)

            if start_idx + 1 < len(s):
                two_digit = s[start_idx:start_idx + 2]
                if 10 <= int(two_digit) <= 26:
                    total += backtracking(start_idx + 2)
            memo[start_idx] = total
            return total

        return backtracking(0)
