# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rea = []
        
        while head:
            rea.append(head.val)
            head = head.next
            
        return rea==rea[::-1]