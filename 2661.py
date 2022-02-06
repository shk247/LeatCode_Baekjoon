import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    answer = [] 
    
    def check(cnt):
        for i in range(cnt):
            tmp = answer[i:]
            for j in range(1, len(tmp)//2+1):
                if tmp[:j] == tmp[j:j+j]:
                    return False
        return True
        
    def backtracking(cnt):
        if not check(cnt):
            return False
        if cnt==n:
            print(*answer, sep='')
            return True
        for i in range(1, 4):
            answer.append(i)
            if backtracking(cnt+1):
                return True
            answer.pop()
        
    backtracking(0)
    
if __name__=='__main__':
    mysolution()