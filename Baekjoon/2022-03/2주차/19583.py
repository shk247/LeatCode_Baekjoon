from datetime import datetime
import sys 

def mysolution():
    input = sys.stdin.readline
    start, end, streaming_end = input().split()
    start = datetime.strptime(start, '%H:%M')
    end = datetime.strptime(end, '%H:%M')
    streaming_end = datetime.strptime(streaming_end, '%H:%M')
    
    checkin = set()
    checkout = set()
    try:
        while True:
            time, nickname = input().split()    
            time = datetime.strptime(time, '%H:%M')
            
            if start>=time:
                checkin.add(nickname)
                
            if end<=time<=streaming_end:
                checkout.add(nickname)
    except:
        print(len(checkin&checkout))
        exit()
    
    
def solution():
    input = sys.stdin.readline
    start, end, streaming_end = input().split()
    start = datetime.strptime(start, '%H:%M')
    end = datetime.strptime(end, '%H:%M')
    streaming_end = datetime.strptime(streaming_end, '%H:%M')
    
    answer = 0 
    checkin = set()
    try:
        while True:
            time, nickname = input().split()    
            time = datetime.strptime(time, '%H:%M')
            
            if start>=time:
                checkin.add(nickname)
                
            if end<=time<=streaming_end and nickname in checkin:
                checkin.remove(nickname)
                answer+=1
    except:
        print(answer)
        exit()
        
if __name__=='__main__':
    mysolution()