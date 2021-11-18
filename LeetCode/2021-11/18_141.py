class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        visited = []
        while head:
            if head in visited:
                return True
            visited.append(head)
            head = head.next
        return False
        
if __name__ == "__main__":
    node = ListNode(3)
    node.next = ListNode(2)
    node.next.next = ListNode(0)
    node.next.next.next = ListNode(4)
    
    sol = Solution()
    print(sol.hasCycle(node))
        
        