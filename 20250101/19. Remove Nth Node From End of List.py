# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        curr = ListNode(0,head)
        tmp = curr
        
   
        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            tmp = tmp.next
        
        tmp.next = tmp.next.next

        
        return curr.next
            


        

        