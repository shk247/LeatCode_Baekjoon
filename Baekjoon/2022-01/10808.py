import sys 
from collections import Counter

def mysolution():
    input = sys.stdin.readline
    word = input().strip()
    word = Counter(word)
    for i in range(97, 123):
        if chr(i) in word.keys():
            print(word[chr(i)])
        else:
            print(0)
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()