from collections import Counter
import sys

def mysolution():
    input = sys.stdin.readline
    books = []
    n = int(input())
    for _ in range(n):
        books.append(input().rstrip())
    books = Counter(books).most_common()
    maximum = books[0][1]
    answer = []
    for book in books:
        if book[1]==maximum:
            answer.append(book[0])
    print(sorted(answer)[0])
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()