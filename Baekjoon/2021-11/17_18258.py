from collections import deque
from sys import stdin

def mysolution():
    n = int(stdin.readline())
    answer = deque()
    for _ in range(n):
        line = stdin.readline().split()
        l = line[0]
        if l == 'push':
            answer.append(line[1])
        elif l == 'pop':
            print(answer.popleft()) if answer else print(-1)
        elif l == 'size':
            print(len(answer))
        elif l == 'empty':
            print(0) if answer else print(1)
        elif l == 'front':
            print(answer[0]) if answer else print(-1)
        elif l == 'back':
            print(answer[-1]) if answer else print(-1)

def solution():
    return

if __name__=='__main__':
    mysolution()