import sys 

def mysolution():
    input = sys.stdin.readline
    while True:
        try:
            s, t = map(list, input().split())
            s_idx = 0 
            t_idx = 0
            if len(s)>len(t):
                print('NO')
                continue
            while len(t)>t_idx and len(s)>s_idx:
                tmp = t[t_idx:]
                if str(tmp).find(s[s_idx]) != -1:
                    t_idx += tmp.index(s[s_idx])
                    s_idx += 1
                else:
                    print('NO')
                    break
            else:
                print('Yes')
        except:
            break
    
def solution():
    input = sys.stdin.readline
    while True:
        try:
            s, t = input().split()
            s_idx=0
            for i in t:
                if s[s_idx] == i:
                    s_idx+=1
                    if s_idx == len(s):
                        print('Yes')
                        break
            else:
                print('No')
        except: 
            break

if __name__=='__main__':
    mysolution()