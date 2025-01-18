class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        freq = defaultdict(int)
        result = 0
        i = 0

        for j in range(len(s)):
            freq[s[j]] +=1
            max_freq = max(freq.values())
            curLen = j-i+1
            if curLen - max_freq > k:
                freq[s[i]] -=1
                i+=1
            result = max(result, j-i+1)
        return result




        