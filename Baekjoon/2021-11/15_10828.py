def mysolution():
    n = int(input())
    str = [input() for _ in range(n)]
    stack = []
    for s in str:
        if 'push' in s:
            num = s.split()[1]
            stack.append(num)
        elif 'pop' in s:
            print(-1 if not stack else stack.pop())
        elif 'size' in s:
            print(len(stack))
        elif 'empty' in s:
            print(1 if not stack else 0)
        elif 'top' in s:
            print(-1 if not stack else stack[-1])

if __name__=='__main__':
    mysolution()