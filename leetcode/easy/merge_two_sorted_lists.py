# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        while l1:
            res.append(l1.val)
            l1 = l1.next
        while l2:
            res.append(l2.val)
            l2 = l2.next
        res = sorted(res, reverse=True)
        l3 = None
        while len(res)>0:
            node = ListNode(res[0], l3)
            l3 = node
            res.pop(0)
        return l3
            
s = Solution()
l1 = ListNode(val=1, next=ListNode(val=2,next=ListNode(val=4)))
l2 = ListNode(val=1, next=ListNode(val=3,next=ListNode(val=4)))
l3 = s.mergeTwoLists(l1,l2)
while l3:
    print(l3.val)
    l3 = l3.next