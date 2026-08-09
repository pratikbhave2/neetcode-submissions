# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Brute force --> O(2n)
        # vals = []
        # if head == None:
        #     return head
        
        # if head.next == None:
        #     return head

        # curr = head
        # while curr != None:
        #     vals.append(curr.val)
        #     curr = curr.next
        
        # # Create a linked list using a list
        # curr_node = ListNode(vals[-1])
        # head = curr_node
        # for i in range(len(vals) - 2, -1, -1):
        #     new_node = ListNode(vals[i])
        #     curr_node.next = new_node
        #     curr_node = new_node

        # return head
            
            
        # Two pointers
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
