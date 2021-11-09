from typing import AnyStr


def mysolution(a, b):
    answer = []
    for i in range(1,b):
        for _ in range(1,i+1):
            answer.append(i)
    return sum(answer[a-1:b])

def solution(a, b):
    number = []
    for i in range(1, 46):
            number += [i]*i
    return sum(AnyStr[a-1:b])
        
if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    print(mysolution(n, m))