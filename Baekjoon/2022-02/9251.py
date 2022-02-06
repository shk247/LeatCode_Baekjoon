import sys 

def mysolution():
    input = sys.stdin.readline
    a = input().strip()
    b = input().strip()
    answer = 0 
    
    def check(a, b):
        nonlocal answer
        for i in range(1, len(a)):
            temp = a[:i]
            for j in range(0, len(b)-i+1):
                if temp == b[j:j+i]:
                    answer = max(answer, len(temp))
    
    check(a, b)
    check(b, a)
    
    print(answer)
    
def solution():
    input = sys.stdin.readline
    a = input().strip()
    b = input().strip()
    len_a = len(a)
    len_b = len(b)
    
    cache = [[0]*(len_a+1) for _ in range(len_b+1)]
    for i in range(1, len_b+1):
        for j in range(1, len_a+1):
            if a[j-1] == b[i-1]:
                cache[i][j] = cache[i-1][j-1]+1
            else:
                cache[i][j] = max(cache[i-1][j], cache[i][j-1])
    print(cache)
    print(cache[len_b][len_a])

def solution2():
    input = sys.stdin.readline
    a = input().strip()
    b = input().strip()
    len_a = len(a)
    len_b = len(b)
    
    cache = [[0]*(len_b+1)]*(len_a+1)
    for i in range(1, len_a+1):
        for j in range(1, len_b+1):
            if a[i-1] == b[j-1]:
                cache[i][j] = cache[i-1][j-1]+1
            else:
                cache[i][j] = max(cache[i-1][j], cache[i][j-1])
    
    print(cache)
    print(cache[-1][-1])
    
if __name__=='__main__':
    solution()