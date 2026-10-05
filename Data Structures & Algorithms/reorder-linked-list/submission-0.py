# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first we use slow and fast pointer to find the midpoint of the list
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # now we have found the middle node, and the next node will become the head of the second_half list
        second_half = slow.next
        prev = slow.next = None
        # the approach is to reverse the second half, and then alternate adding the nodes in the second half to the first half
        while second_half:
            tmp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = tmp

        # now we merge the two lists
        first_half, second_half = head, prev
        while second_half:
            tmp1 = first_half.next
            tmp2 = second_half.next
            first_half.next = second_half
            second_half.next = tmp1
            first_half, second_half = tmp1, tmp2

