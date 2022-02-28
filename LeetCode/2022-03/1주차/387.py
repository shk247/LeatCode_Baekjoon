from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
            
        return vals == vals[::-1]
    
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        self.front_pointer = head 
        
        def recursive(current_node):
            if current_node is not None:
                if not recursive(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True
            
        return recursive(head)
    
    def isPalindrome3(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        
        first_helf_end = self.enf_of_first_heaf(head)
        second_half_start = self.reverse(first_helf_end.next)
        
        result = True
        first = head
        second = second_half_start
        while result and second is not None:
            if first.val != second.val:
                result = False
            first = first.next
            second = second.next
            
        first_helf_end.next = self.reverse(second_half_start)
        
        return result
        
        
    def enf_of_first_heaf(self, node):
        slow_pointer = node
        fast_pointer = node.next.next
        while fast_pointer is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = node.next.next
        return slow_pointer
    
    def reverse(self, node):
        prev = None
        current = node
        
        while current is not None:
            next_node = current.next 
            current.next = prev
            prev = current
            current = next_node
            
        return prev