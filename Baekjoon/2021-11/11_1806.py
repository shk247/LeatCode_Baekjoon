
def mysolution():
    n, s = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    answer = 1e9
    for i in range(n):
        sum = nums[i]
        for j in range(i+1, n):
            sum += nums[j]
            if sum >= s:
                answer = min(answer, j-i+1)
                if answer == 2:
                    print(answer)
                    return 
                break
    print(answer)
    
def solution():
    n, s = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    sum_a = [0] * (n+1)
    for i in range(1, n+1):
          sum_a[i] = sum_a[i-1] + a[i-1]
    
    answer = 1e9
    start = 0 
    end = 1
    
    while start != n:
        if sum_a[end] - sum_a[start] >= s:
            if end - start < answer:
                answer = end - start
            start += 1
        else:
            if end != n:
                end += 1
            else: 
                start += 1
    
    if answer != 1e9:
        print(answer)
    else:
        print(0)
          
if __name__ == '__main__':
    solution()