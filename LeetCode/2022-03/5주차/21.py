from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(-1)
        answer = head 
        
        while list1 and list2:
            if list1.val>list2.val:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next
            head = head.next 
                
        if not list1:
            head.next = list2
        else:
            head.next = list1
        
        return answer.next
    
    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            if list1.val<list2.val:
                list1.next = self.mergeTwoLists2(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists2(list1, list2.next)
                return list2

if __name__=='__main__':
    Solution()