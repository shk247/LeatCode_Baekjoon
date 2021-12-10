from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0)
        head = answer
        plus = 0 
        while l1 or l2 or plus:
            if l1 and l2:
                total = l1.val + l2.val + plus
                l1 = l1.next
                l2 = l2.next
            elif l1:
                total = l1.val + plus
                l1 = l1.next
            elif l2:
                total = l2.val + plus
                l2 = l2.next
            else:
                total = plus
            
            if total >= 10:
                plus = 1
                total -= 10
            else:
                plus = 0  
                
            answer.next = ListNode(total)
            answer = answer.next
            
        return head.next

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resultNode = tempNode = ListNode()
    
        carry = 0 
        while l1 or l2 or carry:
            total = 0 
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
                
            total += carry
            
            tempNode.next = ListNode(total%10)
            tempNode = tempNode.next
            carry = total//10
        return resultNode.next
                
if __name__=='__main__':
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(9)
    l1.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next.next = ListNode(9)
    
    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    l2.next.next.next = ListNode(9)
    
    print(Solution().addTwoNumbers(l1,l2))