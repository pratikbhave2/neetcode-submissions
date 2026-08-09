# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # step 1: reverse the second half of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Now, slow is at the midpoint, so reverse the list startign from slow.next
        prev = None
        curr = slow.next
        slow.next = None # v v v important to splt into two
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        

        # Merge the two halfs alternatively
        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
