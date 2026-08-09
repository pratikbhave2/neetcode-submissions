# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # ez solution
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1

        
        # since we need to remove the nth element from behind, find it first
        remove_index = length - n
        # print(remove_index)
        if remove_index == 0:
            return head.next

        # traverse till (remove_index - 1)th index
        i = 1
        curr = head
        # while i != (remove_index - 1):
        for _ in range(remove_index - 1):
            curr = curr.next
            i += 1

        curr.next = curr.next.next

        return head

        

