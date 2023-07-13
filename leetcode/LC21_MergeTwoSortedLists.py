# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # base cases:
        if list1 == None and list2 == None:
            return None
        
        if list1 == None and list2 != None:
            return list2
        
        if list1 != None and list2 == None:
            return list1

        # compare the two "input heads"
            # assign head as whatever's smaller
            # recursively call on "other list" and list minus head

        if list1.val < list2.val:
            head = list1
            head.next = self.mergeTwoLists(list1.next, list2)

            
        else:
            head = list2
            head.next = self.mergeTwoLists(list1, list2.next)

        return head

            

        # return head

        # compare list1Curr and list2Curr and add them to the combined list

        # return head of merged linked list

