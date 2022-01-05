import sys 
from collections import defaultdict
 
def mysolution():
    input = sys.stdin.readline
    n = int(input())
    dict = defaultdict(int)
    for _ in range(n):
        word = input().strip()
        dict[word[0]] += 1
    answer = [key for key, value in dict.items() if value>=5]
    if not answer:
        print("PREDAJA")
    else:
        answer.sort()
        print(''.join(answer))

def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()