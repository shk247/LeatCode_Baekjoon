import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    books = defaultdict(int)
    
    for _ in range(n):
        books[input().strip()] += 1
    
    books = [k for k,v in books.items() if max(books.values())==v]
    
    if len(books)!=1:
        books.sort()
        
    print(books[0])
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()