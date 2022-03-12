import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    new = input().strip()
    answer = 0 
    
    for _ in range(n):
        old = input().strip()
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    new = input().strip()
    
    def check(old, new): 
        len_old = len(old)
        len_new = len(new)
        for start_idx in range(len_old):
            if old[start_idx] == new[0]:
                for end_idx in range(start_idx+1, len_old):
                    if old[end_idx] == new[-1]:
                        inter = (end_idx-start_idx)//(len_new-1)
                        cnt = 0 
                        idx = start_idx
                        while idx<len_old:
                            if old[idx]==new[cnt]:
                                idx+=inter
                                cnt+=1
                            else:
                                break
                            if cnt == len_new:
                                return 1
        return 0
     
    answer = 0 
    for _ in range(n):
        old = input().strip()
        answer += check(old, new)
        
    print(answer)    

if __name__=='__main__':
    solution()