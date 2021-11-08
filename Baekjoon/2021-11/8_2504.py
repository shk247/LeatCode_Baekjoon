
def mysolution(str):
    a_left, a_right = [], []
    b_left, b_right = [], []
    total = '' 

    for s in str:
        if s == '(':
            a_left.append(s)
        elif s == ')':
            a_right.append(s)
            if len(a_right) > len(a_left):
                return 0
            if len(a_right) != len(a_left):
                total += '+2'
            if len(a_right)//2>0 and len(a_left)//2>0:
                total += '+2'
            else:
                total += '*2'
        elif s == '[':
            b_left.append(s)
        elif s == ']':
            b_right.append(s)
            if len(b_right) > len(b_left):
                pass

def solution(str):
    stack = []
    for i in str:
        if i==')':
            t = 0 
            while len(stack)!= 0:
                top = stack.pop()
                if top == '(':
                    if t == 0:
                        stack.append(2)
                    else:
                        stack.append(2*t)
                    break
                elif top == '[':
                    return 0 
                else:
                    t += int(top)
        elif i == ']':
            t = 0 
            while len(stack) !=0:
                top = stack.pop()
                if top == '[':
                    if t == 0:
                        stack.append(3)
                    else:
                        stack.append(3*t)
                    print('] == ', stack)
                    break
                elif top == '(':
                    return 0
                else:
                    t += int(top)
        else:
            stack.append(i)
    answer = 0 
    for i in stack:
        if i == '(' or i == '[':
            return 0
        else:
            answer += i
    return answer


if __name__=='__main__':
    str = list(input())
    print(solution(str))