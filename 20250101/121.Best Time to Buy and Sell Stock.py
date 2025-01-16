class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
    
        max_price = 0
        l = 0
        r = 1
        while r<len(prices):
            curr_price = prices[r]-prices[l]
            if prices[l] < prices[r]:
                max_price = max(max_price, curr_price)
            else:
                l=r
            r+=1
            
            

        return max_price

        


        
            
        