# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Handle the edge case where the list has only one node
        if not head or not head.next:
            return None

        # Step 1: Get the length of the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Step 2: Calculate the target index from the start (0-based)
        index = length - n

        # Step 3: Handle edge case where the head node is removed
        if index == 0:
            return head.next

        # Step 4: Traverse to the node before the target node
        i = 0
        curr = head
        while i < index - 1:
            curr = curr.next
            i += 1

        # Step 5: Remove the target node
        if curr and curr.next:
            curr.next = curr.next.next

        return head