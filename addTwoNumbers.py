# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = ListNode((l1.val + l2.val) % 10)
        if (l1.next is None and l2.next is None):
            if ((l1.val + l2.val)>=10):
                r.next = ListNode(1)
            return r
        if (l1.next is None and l2.next is not None):
            l1.next = ListNode(0)
        elif (l2.next is None and l1.next is not None):
            l2.next = ListNode(0)
        if (l1.val + l2.val) >= 10:
            l1.next.val += 1
        r.next = self.addTwoNumbers(l1.next,l2.next)
        return r
        
