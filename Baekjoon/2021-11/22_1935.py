import re

def mysolution():
    n = int(input())
    line = list(input())
    char = []
    oper = []
    
    for l in line:
        if l.isalpha():
            char.append(l)
        else:
            oper.append(l)

    dict = {}
    for i in range(n):
        dict[char[i]] = input()
    
    answer = ''
    oper_idx = 0 
    for i in range(0,len(char),2):
        pass
        
    print(answer)
    print(eval(answer))
        

def solution():
    n = int(input())
    line = list(input())

    dict = {}
    for i in range(n):
        dict[chr(65+i)] = input()

    stack = []
    
    for l in line:
        if l.isalpha():
            stack.append(dict[l])
        else:
            s2 = stack.pop()
            s1 = stack.pop()
            stack.append(str(eval(s1+l+s2)))
            
    print('%.2f' %float(stack[0]))
            
if __name__=='__main__':
    solution()