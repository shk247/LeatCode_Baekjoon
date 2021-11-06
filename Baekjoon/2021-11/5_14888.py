from itertools import permutations
import math

def div(num1, num2):
    return -((-num1)//num2) if num1<0 else num1//num2

def mysolution():
    n = int(input())
    nums = list(map(int, input().split()))
    operations = map(int, input().split())

    maxnum, minnum = -math.inf, math.inf
    a, b, c, d = operations
    operations = list('+'*a + '-'*b + '*'*c + '/'*d)
    operations = set(permutations(operations, len(operations)))
    for operation in operations:
        total = div(nums[0], nums[1]) if operation[0] == '/' else eval(str(nums[0])+operation[0]+str(nums[1]))
        for idx in range(1,len(operation)):
            total = div(total, nums[idx+1]) if operation[idx] == '/' else eval(str(total) + operation[idx] + str(nums[idx+1]))
        maxnum = max(maxnum, total)
        minnum = min(minnum, total)
    
    print(maxnum)
    print(minnum)

def solution():
    N = int(input())
    num = list(map(int, input().split()))
    op = list(map(int, input().split()))
    
    global maximum, minimum
    maximum = -1e9
    minimum = 1e9

    def dfs(depth, total, plus, minus, multiply, divide):
        global maximum, minimum
        if depth == N:
            maximum = max(total, maximum)
            minimum = min(total, minimum)
            return

        if plus:
            dfs(depth+1, total+num[depth], plus-1, minus, multiply, divide)
        if minus:
            dfs(depth+1, total-num[depth], plus, minus-1, multiply, divide)
        if multiply:
            dfs(depth+1, total*num[depth], plus, minus, multiply-1, divide)
        if divide:
            dfs(depth+1, int(total/num[depth]), plus, minus, multiply, divide-1)

    dfs(1, num[0], op[0], op[1], op[2], op[3])
    print(maximum)
    print(minimum)
        

if __name__ == '__main__':
    # mysolution()
    solution()



