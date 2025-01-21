class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []

        for i in tokens:
           
            if i == "+":
                top = s.pop()
                s.append(s.pop()+top)
            elif i == "-":
                top = s.pop()
                s.append(s.pop() - top)
            elif i == "*":
                top = s.pop()
                s.append(s.pop() * top)
            elif i == "/":
                top = s.pop()
                s.append(int(s.pop() / float(top)))
  
            else:
                s.append(int(i))
        return s[0]  
        