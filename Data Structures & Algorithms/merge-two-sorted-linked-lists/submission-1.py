# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Brute force
        # Merge and sort them
        # O ( n + m). log (n + m)
        # if list1 == None and list2== None:
        #     return None
        
        # if list1 and list2 == None:
        #     return list1

        # if list2 and list1 == None:
        #     return list2

        # merged = []

        # curr = list1
        # while curr:
        #     merged.append(curr.val)
        #     curr = curr.next

        # curr = list2
        # while curr:
        #     merged.append(curr.val)
        #     curr = curr.next

        # sortedLL = sorted(merged)
        # curr = ListNode(sortedLL[0])
        # head = curr
        # for i in range(1, len(sortedLL)):
        #     new_node = ListNode(sortedLL[i])
        #     curr.next = new_node
        #     curr = new_node
        
        # return head


        # Optimal
        if not list1:
            return list2
        if not list2:
            return list1

        # Select the initial head node
        head = list1 if list1.val <= list2.val else list2
        curr = head
        
        # Advance the pointer of the list that was selected as head
        if head == list1:
            list1 = list1.next
        else:
            list2 = list2.next

        # Merge the two lists
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next  # Advance the current pointer
        
        # Attach remaining elements
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return head

        
