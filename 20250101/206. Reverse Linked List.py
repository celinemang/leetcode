# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]

        """
        '''
        1 2 3 4 5
        p c n
        '''
        node = None  

        while head:
            curr = head.next
            head.next = node
            node = head
            head = curr
            
        return node

        