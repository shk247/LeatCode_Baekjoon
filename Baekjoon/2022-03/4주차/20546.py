import sys 

def mysolution():
    input = sys.stdin.readline
    money = int(input())
    days = list(map(int, input().split()))
    
    jun = sung = money
    jun_stock = sung_stock = 0 
    before = days[0]
    up = down = 0 
    
    for day in days:
        if day<=jun:
            stock = jun//day
            jun -= day*stock
            jun_stock += stock
        
        if before>day:
            up = 0 
            down +=1 
        elif before<day:
            up += 1
            down = 0 
            
        if up == 3:
            sung += sung_stock*day
            sung_stock = 0 
        elif down == 3:
            stock = sung//day
            sung -= day*stock
            sung_stock += stock

        before = day
    
    sung += sung_stock*days[-1]
    jun += jun_stock*days[-1]

    if sung>jun:
        print('TIMING')
    elif sung<jun:
        print('BNP')
    else:
        print('SAMESAME')
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()