# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return 
        
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
            
        
        temp = sorted(temp, reverse=True)
        
        head = ListNode(temp.pop())
        temp2 = head
        
        while temp:
            temp2.next = ListNode(temp.pop())
            temp2 = temp2.next
            
        return head
            
            