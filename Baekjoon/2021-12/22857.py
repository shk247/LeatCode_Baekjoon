import sys 

def mysolution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    
    if len(s) == k:
        print(0)
        
    
    
def solution():
    input = sys.stdin.readline
    input = sys.stdin.readline
    s, n = map(int, input().split())
    arr = list(map(int, input().split()))
    
    idx, ans, odd, even = 0, 0, 0, 0
    
    for i in range(s):
        start = i 
        
        while idx<s and odd<=n:
            if arr[idx]%2 == 0:
                even += 1
            else:
                odd += 1
            idx += 1
            if start == 0 and idx == s:
                ans = even
                break
    
    if odd == n+1:
        ans = max(ans, even)
    if arr[start]%2 == 1:
        odd -= 1
    else:
        even -= 1
        
    print(ans)

if __name__=='__main__':
    mysolution()