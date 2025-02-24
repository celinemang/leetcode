class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        sub = []
        
        def subset(i):
            if i == len(nums):
                res.append(sub[:])
                return
            sub.append(nums[i])
            subset(i+1)

            sub.pop()
            subset(i+1)

        subset(0)
        return res