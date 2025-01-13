class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pt1 = 0
        pt2 = len(numbers)-1

        while pt1<pt2:
            if numbers[pt1]+numbers[pt2] == target:
                return [pt1+1,pt2+1]
            elif numbers[pt1]+numbers[pt2]>target:
                pt2 -= 1
            else:
                pt1+=1
        return[]
        