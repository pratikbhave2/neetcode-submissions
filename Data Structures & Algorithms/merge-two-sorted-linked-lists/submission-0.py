# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Brute force
        # Merge and sort them
        if list1 == None and list2== None:
            return None
        
        if list1 and list2 == None:
            return list1

        if list2 and list1 == None:
            return list2

        merged = []

        curr = list1
        while curr:
            merged.append(curr.val)
            curr = curr.next

        curr = list2
        while curr:
            merged.append(curr.val)
            curr = curr.next

        sortedLL = sorted(merged)
        print(sortedLL)
        curr = ListNode(sortedLL[0])
        head = curr
        for i in range(1, len(sortedLL)):
            new_node = ListNode(sortedLL[i])
            curr.next = new_node
            curr = new_node
        
        return head
