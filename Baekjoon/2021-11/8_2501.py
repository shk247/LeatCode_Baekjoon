def mysolution(n, k):
    nums = []
    for i in range(1, n+1):
        if n%i == 0:
            nums.append(i)
        if len(nums) == k:
            return nums[-1]
    return 0 

def solution(n, k):
    ans = []
    for i in range(1, n+1):
        if n%i==0:
            ans.append(i)

    if len(ans)>=k:
        return ans[k-1]
    else:
        return 0 

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    print(mysolution(n, k))