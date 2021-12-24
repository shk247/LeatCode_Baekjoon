import sys 

def mysolution():
    input = sys.stdin.readline
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    mininum = 1e9
    for i in range(len(nums)):
        if nums[i]>=s:
            break
        tmp = cnt = 0 
        for j in range(i, len(nums)):
            if tmp < s:
                tmp += nums[j]
                cnt += 1
            else:
                break
        else:
            if tmp<s:
                continue
        mininum = min(cnt, mininum)
    print(mininum)
    
def solution():
    input = sys.stdin.readline
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    
    left, right = 0, 0
    tmp_sum = 0 
    min_length = 1e9
    
    while True:
        if tmp_sum >= s:
            min_length = min(min_length, right-left)
            tmp_sum -= nums[left]
            left += 1
        elif right == n:
            break
        else:
            tmp_sum += nums[right]
            right += 1
    
    if min_length == 1e9:
        print(0)
    else:
        print(min_length)
    

if __name__=='__main__':
    mysolution()