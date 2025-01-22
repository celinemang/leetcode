class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        ans = []

        def backtrack(self,current_string,open,close):
            if len(current_string) == 2*n:
                ans.append(current_string)
            
            if open < n :
                backtrack(self,current_string+"(", open+1,close)
            if close < open:
                backtrack(self,current_string+")",open,close+1)

        backtrack(self,"",0 , 0) 
        return ans

       
        