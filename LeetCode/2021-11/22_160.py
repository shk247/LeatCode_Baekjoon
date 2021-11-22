class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        nodes = set()
        
        while headB:
            nodes.add(headB)
            headB = headB.next
            
        while headA:
            if headA in nodes:
                return headA
            headA = headA.next
            
        return None

    def getIntersectionNode2(self, headA, headB):
        a = headA
        b = headB
        
        while a!=b:
            a = headB if a else a.next
            b = headA if b else b.next
            print('a=',a.val,'b=',b.val)
        return a     
        