import sys

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input().strip())
    words = list(set(words))
    words.sort()
    words.sort(key=lambda x:len(x))

    for w in words:
        print(w)

def solution():
    input = sys.stdin.readline
    return

if __name__=='__main__':
    mysolution()