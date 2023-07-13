# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # base case: if the inputted head is None 
        if head == None or head.next == None:
            return head

        # recurse all the way down to the the base case (end of linked list)
        nextNode = self.reverseList(head.next)

        # do work
        # assign .next's next node as current node
        head.next.next = head
        # assign current node's next as previous layer of abstraction's head
        head.next = None # this will be returned in the base case, and will go back up (i think)
        return nextNode