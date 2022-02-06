import sys 
from collections import deque

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    
    pl, mi, mu, di = map(int, input().split())
    
    max_answer = -1e9
    min_answer = 1e9
    
    def check(depth, total, plus, minus, multiple, divide):
        nonlocal max_answer
        nonlocal min_answer
        
        if (plus+minus+multiple+divide)==0:
            max_answer = max(max_answer, total)
            min_answer = min(min_answer, total)
            return
    
        if plus:
            check(depth+1, total+nums[depth], plus-1, minus, multiple, divide)
        if minus:
            check(depth+1, total-nums[depth], plus, minus-1, multiple, divide)
        if multiple:
            check(depth+1, total*nums[depth], plus, minus, multiple-1, divide)
        if divide:
            check(depth+1, int(total/nums[depth]), plus, minus, multiple, divide-1)    
            
    check(1, nums[0], pl, mi, mu, di)
    print(max_answer)
    print(min_answer)
    
def solution():
    input = sys.stdin.readline
    N = int(input())
    num = list(map(int, input().split()))
    op = list(map(int, input().split()))  # +, -, *, //

    maximum = -1e9
    minimum = 1e9

    def dfs(depth, total, plus, minus, multiply, divide):
        nonlocal maximum, minimum
        if depth == N:
            maximum = max(total, maximum)
            minimum = min(total, minimum)
            return

        if plus:
            dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
        if minus:
            dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
        if multiply:
            dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
        if divide:
            dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


    dfs(1, num[0], op[0], op[1], op[2], op[3])
    print(maximum)
    print(minimum)
    
if __name__=='__main__':
    mysolution()