import sys 
import re

def mysolution():
    input = sys.stdin.readline
    s = input().strip()
    words = []
    if '<' in s:
        i = 0 
        start = 0 
        while i<len(s):
            if s[i] == '<':
                i+=1 
                while s[i] != '>':
                    i+=1
                i+=1
            elif s[i] == ' ':
                i+=1
                
    else:
        words.extend(s.split())
        for i in range(len(words)):
            words[i] = words[i][::-1]
        print(' '.join(words))
    
def solution():
    input = sys.stdin.readline
    s = list(input().strip())
    i = 0 
    start = 0 
    while i<len(s):
        if s[i] == '<':
            i+=1 
            while s[i] != '>':
                i+=1
            i+=1
        elif s[i] == ' ':
            i+=1
        else:
            start = i 
            while i<len(s) and s[i].isalnum():
                i+=1
            tmp = s[start:i]
            tmp.reverse()
            s[start:i] = tmp
    print(''.join(s))
            

if __name__=='__main__':
    solution()