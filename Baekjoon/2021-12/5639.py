import sys 

def mysolution():
    input = sys.stdin.readline
    total = []
    while True:
        try:
            total.append(int(input().strip()))
        except:
            break
    root = []
    left = []
    right = []
    root.append(total.pop())
    while total:
        while root[-1]>total[0]:
            left.append(total.pop())
        
def getPostorder(nums):            
    length = len(nums)
    
    if length <= 1:
        return nums
    
    for i in range(1, length):
        if nums[i]>nums[0]:
            return getPostorder(nums[1:i]) + getPostorder(nums[i:]) + nums[0]
    
    return getPostorder(nums[1:]) + nums[0]
            
    
def solution():
    sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    nums = []
    while True:
        try:
            nums.append(int(input().strip()))
        except:
            break
    nums = getPostorder(nums)
    for n in nums:
        print(n)
        
        
def solution2():
    sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    nums = []
    while True:
        try:
            nums.append(int(input().strip()))
        except:
            break
        
    def f(start, end):
        if start>end:
            return
        else:
            root = nums[start]
            div = end+1
            for pos in range(start+1, end+1):
                if root < nums[pos]:
                    div = pos
                    break
            f(start+1, div-1)
            f(div, end)
            print(root)
    
    f(0, len(nums)-1)
    
if __name__=='__main__':
    mysolution()