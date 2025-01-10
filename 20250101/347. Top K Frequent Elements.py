class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n,0)
        
        freq = [[] for _ in range(len(nums)+1)]
        for n, f in counter.items():
            freq[f].append(n)
        res = []

        for i in range(len(freq) -1,-1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
         




        