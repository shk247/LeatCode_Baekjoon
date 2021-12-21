import sys 
from itertools import permutations 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(str, input().split()))
    plus, minus, multi, divide = map(int, input().split())
    opers = ['+']*plus + ['-']*minus + ['*']*multi + ['//']*divide
    opers = set(permutations(opers, n-1))
    max_num, min_num = -1e9, 1e9
    for oper in opers:
        tmp = eval(nums[0]+oper[0]+nums[1])
        for i in range(1, len(oper)):
            if oper[i]=='//' and tmp<0:
                tmp *= -1
                tmp = eval(str(tmp)+oper[i]+nums[i+1])
                tmp *= -1
            else:
                tmp = eval(str(tmp)+oper[i]+nums[i+1])
        max_num = max(max_num, tmp)
        min_num = min(min_num, tmp)

    print(max_num)
    print(min_num)
    
def solution():
    input = sys.stdin.readline
    N = int(input())
    num = list(map(int, input().split()))
    op = list(map(int, input().split()))  # +, -, *, //

    global maximum, minimum
    maximum, minimum = -1e9, 1e9
    
    def dfs(depth, total, plus, minus, multiple, divide):
        global maximum, minimum
        if depth == N:
            maximum = max(maximum, total)
            minimum = min(minimum, total)
            return
        
        if plus:
            dfs(depth+1, total+num[depth], plus-1, minus, multiple, divide)
        if minus:
            dfs(depth+1, total-num[depth], plus, minus-1, multiple, divide)
        if multiple:
            dfs(depth+1, total*num[depth], plus, minus, multiple-1, divide)
        if divide:
            dfs(depth+1, int(total/num[depth]), plus, minus, multiple, divide-1)
            
    dfs(1, num[0], op[0], op[1], op[2], op[3])
    print(maximum)
    print(minimum)


if __name__=='__main__':
    solution()