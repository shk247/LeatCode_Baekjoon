def mysolution(n, nums):
    maxnum = max(nums)
    answer = [False, False] + [True]*(maxnum-1)

    for i in range(2, maxnum+1):
        if answer[i] == True:
            for j in range(i+i, maxnum+1, i):
                answer[j] = False
    return len([answer[a] for a in range(len(answer)) if answer[a]==True and a in nums])

def solution(n, nums):
    answer = 0 
    for num in nums:
        error = 0 
        if num > 1:
            for i in range(2, num):
                if num%i == 0:
                    error += 1
            if error == 0:
                answer += 1
    return answer


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print(mysolution(n, nums))