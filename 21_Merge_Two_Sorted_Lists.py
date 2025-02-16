'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # For our output linked list, create a dummy node to prevent
        # oddities related to edge cases where the list is empty, etc
        fake = ListNode()
        tail = fake

        # While both list1 and list2 are not null, compare the values 
        # at the first position of the two
        while list1 and list2:
            if list1.val < list2.val:
                # Tail.next will now point to that value
                tail.next = list1
                # Move on to the next value in the list for 
                # later comparison 
                list1 = list1.next
                # Move tail to next position
                tail = tail.next
            else:
                # Tail.next will now point to that value 
                tail.next = list2
                # Move on to the next value in the list for 
                # later comparison 
                list2 = list2.next
                # Move tail to next position
                tail = tail.next
            
        # There will be times where either one list is longer than the other or
        # one list is empty.  In those cases, we need to have our tail.next point
        # to the remainder of the list that contains valid values
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # Return the first vallue that came after our dummy node, which would be
        # our head value
        return fake.next
