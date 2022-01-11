import sys 

def mysolution():
    input = sys.stdin.readline
    while True:
        n = int(input())
        
        if n==0:
            break
        words = {}
        for _ in range(n):
            word = input().strip()
            words[word.lower()] = word
        
        words = sorted(words.items(),key=lambda item:item[0])
        
        print(words[0][1])
    
def solution():
    input = sys.stdin.readline
    while True:
        n = int(input())
        
        if n==0:
            break
        
        words = [input().strip() for _ in range(n)]
        
        words.sort(key=lambda word:word.lower())
        
        print(words[0])

if __name__=='__main__':
    mysolution()