class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0, len(nums)-1
        min_num = nums[0]

        while l<=r:
            min_num = min(nums[l],nums[r],min_num)
            l+=1
            r-=1
        return min_num
        