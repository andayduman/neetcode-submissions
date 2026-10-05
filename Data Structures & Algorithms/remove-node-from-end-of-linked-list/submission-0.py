# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0 # initialize the length of the list
        ref = head # refernce to head to return at the end

        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        # so now we will have how long the list is

        # now we calculate which node we need to remove
        target = length - n # so after traveling this many times through list we will reach our target node
        curr = head
        prev = None

        # Special case: removing the head node
        if target == 0:
            return head.next

        for i in range(0, target):
            prev = curr
            curr = curr.next
        # now curr is pointing to target node
        prev.next = curr.next
        return ref