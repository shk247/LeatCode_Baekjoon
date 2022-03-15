import sys 

def mysolution():
    input = sys.stdin.readline
    dict = {')':'(', ']':'['}
    
    while True:
        strs = input().replace('\n','')
        if strs == '.':
            break
        q = []
        flag = False
        for s in strs:
            if s=='(' or s=='[':
                q.append(s)
            elif s==')' or s==']':
                if not q or dict[s]!=q[-1]:
                    flag = True
                    print('no')
                    break
                q.pop()
        if flag:
            continue

        if not q:
            print('yes')
        else:
            print('no')
                
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()