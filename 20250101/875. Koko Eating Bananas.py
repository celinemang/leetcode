class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def canEat(m):
            hours = 0
            for i in piles:
                hours += -(-i//m)
            return hours<h
        
        l,r = 1,max(piles)
        while l<r:
            mid = (l+r)//2
            if canEat(mid):
                r = mid
            else:
                l = mid+1
        return l


      