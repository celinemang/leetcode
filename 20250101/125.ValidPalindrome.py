class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()

        ans = ""
        for i in range(len(s)):
            if s[i].isalnum():
                ans += s[i]

        return ans == ans[::-1]