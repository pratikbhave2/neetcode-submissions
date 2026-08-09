# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowp, fastp = head, head

        while fastp and fastp.next:
            slowp = slowp.next
            fastp = fastp.next.next

            if slowp == fastp:
                return True

        return False