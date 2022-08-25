class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rea = []
        
        while head:
            rea.append(head.val)
            head = head.next
            
        return rea==rea[::-1]