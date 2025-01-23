class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLength = 0
        char_set = set() #Can also be written as char_set = {}
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            maxLength = max(maxLength , r-l+1)
        return maxLength