class MinStack(object):

    def __init__(self):
        self.s = []
        self.m = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.s.append(val)
        self.m.append(val if not self.m else min(val, self.m[-1]))

        
        

    def pop(self):
        """
        :rtype: None
        """
        self.s.pop()
        self.m.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.m[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()