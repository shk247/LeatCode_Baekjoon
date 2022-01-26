from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre = 0 
        answer = ListNode()
        node = answer
        
        while l1 or l2:
            num = pre 

            if not l1:
                num += l2.val
                l2 = l2.next
            elif not l2:
                num += l1.val
                l1 = l1.next
            else:
                num += (l1.val + l2.val)
                l1 = l1.next
                l2 = l2.next
                                
            if num>=10:
                pre = 1
                num -= 10
            else:
                pre = 0
            node.next = ListNode(num)
            node = node.next
        
        if pre != 0:
            node.next = ListNode(pre)
            node = node.next
        
        return answer.next
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        result_tail = result 
        carry = 0 
        
        while l1 or l2 or carry:
            a = l1.val if l1 else 0 
            b = l2.val if l2 else 0 
            carry, out = divmod(a+b+carry, 10)
            
            result_tail.next = ListNode(out)
            result_tail = result_tail.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return result.next
                     

if __name__=='__main__':
    l1 = ListNode(0)
    # l1.next = ListNode(4)
    # l1.next .next  = ListNode(3)
    
    l2 = ListNode(0)
    # l2.next = ListNode(6)
    # l2.next .next  = ListNode(4)
    
    answer = Solution().addTwoNumbers(l1, l2)