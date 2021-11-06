
def mysolution(s):
    dict = {'(':')', '{':'}', '[':']'}
    stack = []
    for i in s:
        if i=='(' or i=='{' or  i=='[':
            stack.append(i)
        else:
            if not stack or dict[stack.pop()] != i:
                return False
    return False if stack else True


def solution(s):
    stack = []
    mapping = {")":"(", "}":"{", "]":"["}
    for c in s:
        if c in mapping:
            top = stack.pop() if stack else '#'

            if mapping[c] != top:
                return False
        else:
            stack.append(c)

    return not stack

if __name__ == '__main__':
    print(mysolution("{"))