class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        
        def recursion(low, high, target):
            if low > high:  # Base case: target is not found
                return -1
            
            mid = (low + high) // 2 
            
            if target == nums[mid]:  
                return mid
            
            if target < nums[mid]:  
                return recursion(low, mid - 1, target)
            else: 
                return recursion(mid + 1, high, target)
        
        return recursion(0,len(nums)-1, target)
        
