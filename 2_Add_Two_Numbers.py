'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
First we want to instantiate the output linked list.  From there we will have a head pointer for it,
l1, and l2.  

While l1 and l2 are both valid, add the value at l1 and l2 respectively.  If the sum is greater than
9, we want to put the ones place digit down and carry over the 1 to the next two numbers to be
added together
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode()
        hd = out
        # Create value that keeps track of the one 
        # we are carrying
        carOne = 0
        while l1 or l2 or carOne:
            h1 = l1.val if l1 else 0
            h2 = l2.val if l2 else 0
            # Add vals together
            value = h1 + h2 + carOne
            # Divide our carry one by 10 to 
            # get a 1 to carry
            carOne = value // 10
            # Get ones place digit to place into
            # our output linked list
            value = value % 10
            hd.next = ListNode(value)
            # Move pointers
            hd = hd.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return out.next
