from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        left = 0 
        right = len(nums)-1
        
        while left<right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1
        
        return True
    
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)
        
        first = head
        second = second_half_start
        while second is not None:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next 
            
        first_half_end.next = self.reverse_list(second_half_start)
        
        return True
        
    def end_of_first_half(self, head):
        fast = head 
        slow = head
        
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        return slow
    
    def reverse_list(self, head):
        pre = None
        curr = head
        
        while curr is not None:
            next = curr.next 
            curr.next = pre 
            pre = curr 
            curr = next 
        
        return pre