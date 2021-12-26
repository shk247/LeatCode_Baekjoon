import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    dict = {}
    for _ in range(n):
        a, b, c = input().split()
        dict[a] = [b, c]
    
    def preorder(n):
        print(n,end='')
        left, right = dict[n]
        if left != '.':
            preorder(left)
        if right != '.':
            preorder(right)
            
    def inorder(n):
        left, right = dict[n]
        if left != '.':
            inorder(left)
        else:
            print(n,end='')
            return
        print(n,end='')
        if right != '.':
            inorder(right)
        else:
            print(n,end='')
            return
            
    preorder('A')
    print()
    inorder('A')
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    dict = {}
    for _ in range(n):
        a, b, c = input().split()
        dict[a] = [b, c]
    
    def preorder(root):
        if root != '.':
            print(root, end='')
            preorder(dict[root][0])
            preorder(dict[root][1])
    
    def inorder(root):
        if root != '.':
            preorder(dict[root][0])
            print(root, end='')
            preorder(dict[root][1])
    
    def postorder(root):
        if root != '.':
            preorder(dict[root][0])
            preorder(dict[root][1])
            print(root, end='')        
            
    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')

if __name__=='__main__':
    mysolution()