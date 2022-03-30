# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k==0:
            return head
        
        left = head
        right = head
        
        count = 0
        
        while right:
            count +=1
            right = right.next
        
        k = k%count
        
        if k == 0:
            return head
        
        
        print(k)
        right = head
        for i in range(k):
            right = right.next
            
            
        while right.next:
            right = right.next
            left = left.next
        
        temp = left.next
        
        left.next = None
        
        right.next = head
        
        return temp
        