from collections import deque

def mysolution():
    n = int(input())
    inputs = deque([int(input()) for _ in range(n)])
    answer = []
    nums = []
    num = 0 
    while inputs:
        if num<inputs[0]:
            num += 1
            nums.append(num)
            answer.append('+')
        else:
            if nums[-1]<inputs[0]:
                print('NO')
                return
            nums.pop()
            inputs.popleft()
            answer.append('-')
    return [print(a) for a in answer]


def solution():
    n = int(input())
    cnt = 0 
    stack = []
    result = []
    
    for _ in range(n):
        x = int(input())
        
        while cnt < x:
            cnt += 1
            stack.append(cnt)
            result.append('+')
            
        if stack[-1] == x:
            stack.pop()
            result.append('-')
        else:
            print('NO')
            return
    
    print('\n'.join(result))

if __name__=='__main__':
    mysolution()