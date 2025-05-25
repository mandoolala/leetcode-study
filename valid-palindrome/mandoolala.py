import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        preprocessed_str = re.sub(r'[^a-z0-9]', '', s.lower())
        left_p = 0
        right_p = len(preprocessed_str) - 1
        while left_p < right_p:
            if preprocessed_str[left_p] != preprocessed_str[right_p]:
                return False
            left_p += 1
            right_p -= 1
        return True
