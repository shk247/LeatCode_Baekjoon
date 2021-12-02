import sys 

def mysolution():
    input = sys.stdin.readline
    for _ in range(3):
        start, end = input().split()
        answer =[]
        while True:
            if start.replace(':','') == end.replace(':',''):
                break
            answer.append(int(start.replace(':','')))
            sh, sm, ss = map(int, start.split(':'))
            if ss==59:
                ss=00
                sm+=1
                if sm == 60:
                    sm=00
                    sh+=1
                if sh == 24:
                    sh = 00
            else:
                ss+=1
                
            start = str(sh)+':'+str(sm)+':'+str(ss)
        print(answer)
        # print(len([a for a in answer if a%3==0]))
            
            
from datetime import datetime, timedelta
 
def solution():
    input = sys.stdin.readline
    
    for _ in range(3):
        s, e = input().split()
        sh, sm, ss = map(int, s.split(':'))
        eh, em, es = map(int, e.split(':'))

        stime = datetime(2021,1,1,sh,sm,ss)
        tmp_time = stime.strftime('%H%M%S')
        etime = datetime(2021,1,1,eh,em,es)
        etime = etime.strftime('%H%M%S')
        
        cnt = 0 
        
        while True:
            if int(tmp_time)%3==0:
                cnt += 1
                
            if tmp_time == etime:
                break
            
            stime = stime + timedelta(seconds=1)
            tmp_time = stime.strftime('%H%M%S')

        print(cnt)

def solution2():
    input = sys.stdin.readline
    
    for _ in range(3):
        s, e = input().split()
        sh, sm, ss = map(int, s.split(':'))
        eh, em, es = map(int, e.split(':'))
        
        cnt = 0
        
        while True:
            if ss>59:
                ss=0
                sm += 1
            if sm>59:
                sm=0
                sh+=1
            if sh>23:
                sh=0
            
            num = sh*10000 + sm*100 + ss

            if num%3==0:
                cnt += 1
                
            if sh==eh and sm==em and ss==es:
                break
            
            ss += 1
        print(cnt)

if __name__=='__main__':
    solution()