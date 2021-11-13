def mysolution():
    n = int(input())
    nums = list(map(int, input().split()))
    _min = 1e9
    _max = -1e9 
    for num in nums:
        _min = min(_min, num)
        _max = max(_max, num)
        
    print(str(_min)+' '+str(_max))

if __name__=="__main__":
    mysolution()