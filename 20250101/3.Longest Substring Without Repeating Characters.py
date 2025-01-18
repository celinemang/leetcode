class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 0
        longest = 0
        char_set = set()

        while r < len(s):
            if s[r] not in char_set:
                char_set.add(s[r])
                longest = max(longest, r - l + 1)
                r += 1
            else:
                char_set.remove(s[l])
                l += 1
        
        return longest