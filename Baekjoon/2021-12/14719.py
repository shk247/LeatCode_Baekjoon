import sys 

def mysolution():
    input = sys.stdin.readline
    h, w = map(int, input().split())
    blocks = map(int, input().split())
    ans = 0 
    
def solution():
    input = sys.stdin.readline
    h, w = map(int, input().split())
    blocks = list(map(int, input().split()))
    ans = 0 
    for i in range(1, w-1):
        left = max(blocks[:i])
        right = max(blocks[i+1:])
        low = min(left, right)
        if blocks[i]<low:
            ans += low-blocks[i]
    print(ans)

if __name__=='__main__':
    solution()