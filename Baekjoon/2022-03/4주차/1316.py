import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    words = [input().rstrip() for _ in range(n)]
    answer = 0 
    
    for word in words:
        tmp = []
        for i in word:
            if i not in tmp:
                tmp.append(i)
            elif tmp[-1] != i:
                break
        else:
            answer+=1
        
    print(answer)
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    result = n
    
    for _ in range(n):
        word = input().rstrip()
        for j in range(0, len(word)-1):
            if word[j] == word[j+1]:
                pass
            if word[j] in word[j+1:]:
                result-=1
                break
    
    print(result)

if __name__=='__main__':
    mysolution()