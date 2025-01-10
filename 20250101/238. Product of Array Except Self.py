class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = 1
        post = 1
        ans =[1]*len(nums)
        for i in range(len(nums)):
            ans[i] = pre
            pre *=nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= post
            post *= nums[i]

    
        return ans
            #[1,1,2,6]
            #[24,12,4,1]


        

      
        


            
        