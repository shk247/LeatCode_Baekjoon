

def solution():
    n, k = list(map(int, input().split()))
    nums = [i for i in range(1,n+1)]
    idx = 0 
    answer = []

    for _ in range(n):
        idx += k-1
        if idx>=len(nums):
            idx = idx%len(nums)
        answer.append(nums.pop(idx))
        
    print("<", ', '.join(str(i) for i in answer), ">", sep = '')
                
if __name__=='__main__':
    solution()