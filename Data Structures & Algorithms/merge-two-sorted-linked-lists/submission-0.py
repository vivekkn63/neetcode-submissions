# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1, temp2 = list1, list2
        dummyNode = ListNode(-1)
        final_node = dummyNode
        while temp1 and temp2:
            if temp1.val < temp2.val:
                final_node.next = ListNode(temp1.val)
                final_node = final_node.next
                temp1 = temp1.next
            else:
                final_node.next = ListNode(temp2.val)
                final_node = final_node.next
                temp2 = temp2.next
        while temp1:
            final_node.next = ListNode(temp1.val)
            final_node = final_node.next
            temp1 = temp1.next

        while temp2:
            final_node.next = ListNode(temp2.val)
            final_node = final_node.next
            temp2 = temp2.next
        
        return dummyNode.next

