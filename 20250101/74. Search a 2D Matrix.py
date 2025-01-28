class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        top = 0
        bot = len(matrix)-1

        while top<=bot:
            mid = (top+bot)//2

            if matrix[mid][0]< target and target>matrix[mid][-1]:
                break
            if matrix[mid][0]>target:
                bot = mid-1
            if matrix[mid][0]<target:
                top = mid+1
            
        row = (top+bot)//2
        l=0
        r=len(matrix[row])-1
        while l<=r:
            mid = (l+r)//2

            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                r = mid -1
            else:
                l = mid + 1
            
        return False
