# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        listLen = 0
        currNode = head

        while currNode != None:
            listLen += 1
            currNode = currNode.next

        if listLen % 2 == 0:
            listLen += 1

        for i in range((listLen // 2)):
            head = head.next
        
        return head



        # assign a current node
        # assign double the current node (2 steps at a time)
        # when the double reaches the last node, just show current


        


