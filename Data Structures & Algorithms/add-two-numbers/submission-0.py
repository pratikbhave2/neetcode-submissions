# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current=l1
        i = 0
        num1 = 0
        while current is not None:
            num1 += ((10 ** i) * current.val)
            current = current.next
            i += 1

        current=l2
        i = 0
        num2 = 0
        while current is not None:
            num2 += ((10 ** i) * current.val)
            current = current.next
            i += 1

        final_val = str(num1 + num2)
        # Reverse this
        final_val = final_val[::-1]

    
        head = ListNode(int(final_val[0]))
        current = head

        for i in range(1, len(final_val)):
            current.next = ListNode(int(final_val[i]))
            current = current.next

        return head
