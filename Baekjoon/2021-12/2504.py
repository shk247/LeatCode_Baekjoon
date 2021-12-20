import sys 

def mysolution():
    input = sys.stdin.readline
    queue = []
    
    s = input().strip()
    
def check(s):
    stack = [] 
    
    for i in range(len(s)):
        if s[i] == '(' or s[i]=='[':
            stack.append(s[i])
        else:
            if s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            if s[i] == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
    if stack:
        return False
    else:
        return True

def cal(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i]=='[':
            stack.append(s[i])
        else:
            if s[i]==')':
                if stack[-1] == '(':
                    stack[-1] = 2
                else:
                    tmp = 0 
                    for idx in range(len(stack)-1, -1, -1):
                        if stack[idx] == '(':
                            stack[-1] = tmp*2
                            break
                        else:
                            tmp += stack.pop()
            elif s[i] == ']':
                if stack[-1] == '[':
                    stack[-1] = 3
                else:
                    tmp = 0 
                    for idx in range(len(stack)-1, -1, -1):
                        if stack[idx] == '[':
                            stack[-1] = tmp * 3
                            break
                        else:
                            tmp += stack.pop()
    return sum(stack)
    
def solution():
    input = sys.stdin.readline
    s = input().strip()
    if check(s):
        print(cal(s))
    else:
        print(0)
        
def solution2():
    input = sys.stdin.readline
    s = input().strip()
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i]=='[':
            stack.append(s[i])
        else:
            if not stack:
                return 0
            if s[i]==')':
                if stack[-1] == '[':
                    return 0
                
                if stack[-1] == '(':
                    stack[-1] = 2
                else:
                    tmp = 0 
                    for idx in range(len(stack)-1, -1, -1):
                        if stack[idx] == '(':
                            stack[-1] = tmp*2
                            break
                        else:
                            num = stack.pop()
                            if isinstance(num, int):
                                tmp += num
                            else:
                                return 0 
            elif s[i] == ']':
                if stack[-1] == '(':
                    return 0
                
                if stack[-1] == '[':
                    stack[-1] = 3
                else:
                    tmp = 0 
                    for idx in range(len(stack)-1, -1, -1):
                        if stack[idx] == '[':
                            stack[-1] = tmp * 3
                            break
                        else:
                            num = stack.pop()
                            if isinstance(num, int):
                                tmp += num
                            else:
                                return 0 
    if '(' in stack or '[' in stack:
        return 0
    else:
        return sum(stack)
    
if __name__=='__main__':
    print(solution())