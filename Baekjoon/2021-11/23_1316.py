import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    cnt = 0 
    for _ in range(n):
        word = input().strip()
        temp = []
        for w in word:
            if len(temp)>0 and temp[-1]==w:
                continue
            temp.append(w)
        if len(temp) == len(set(temp)):
            cnt += 1
    print(cnt)

def solution():
    input = sys.stdin.readline
    n = int(input())
    answer = n 
    for _ in range(0, n):
        word = input().strip()
        for j in range(0, len(word)-1):
            if word[j] == word[j+1]:
                pass
            elif word[j] in word[j+1:]:
                answer -= 1
                break
    print(answer)

if __name__=='__main__':
    mysolution()