# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # so we probably need two pointers to track the curr node for each list
        p1 = list1
        p2 = list2

        # the resulting linked list (start it with a dummy node)
        res = ListNode(0, None)
        curr = res

        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                curr = curr.next
                p1 = p1.next
            else:
                curr.next = p2
                curr = curr.next
                p2 = p2.next
        
        # once one of the lists has been exhausted, we append the rest of the nodes from the other list
        curr.next = p1 if p1 else p2
        return res.next
        