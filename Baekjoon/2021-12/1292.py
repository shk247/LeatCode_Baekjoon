import sys 

def mysolution():
    input = sys.stdin.readline
    a, b = map(int, input().split())
    nums = []
    for i in range(1, b//2+2):
        for j in range(i):
            nums.append(i)
    print(sum(nums[a-1:b]))
    
def solution():
    input = sys.stdin.readline
    a, b = map(int, input().split())
    arr = [0]
    for i in range(1,46):
        for j in range(i):
            arr.append(i)
    print(sum(arr[a:b+1]))


if __name__=='__main__':
    mysolution()