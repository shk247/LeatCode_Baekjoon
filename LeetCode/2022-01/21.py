from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        answer = node 
        while list1 != None or list2 != None:
            if not list1:
                node.next = list2
                list2 = list2.next
                node = node.next
                continue
            elif not list2:
                node.next = list1
                list1 = list1.next
                node = node.next
                continue
            
            if list1.val<list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
                
            node = node.next
        
        return answer.next
    
    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val<list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1 
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2 
        
    def mergeTwoLists3(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)
        prev = prehead
        
        while list1 and list2:
            if list1.val<list2.val:
                prev.next = list1 
                list1 = list1.next
            else:
                prev.next = list2 
                list2 = list2.next
            prev = prev.next
        
        if list1 is not None:
            prev.next = list1
        elif list2 is not None:
            prev.next = list2
            
        return prehead.next

if __name__=='__main__':
    Solution()