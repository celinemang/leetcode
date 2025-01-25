class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        stack = []
        for pos, v in sorted(zip(position, speed),reverse = True):

            dist = target - pos
            time = dist / v 
            
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)

        return len(stack)
        