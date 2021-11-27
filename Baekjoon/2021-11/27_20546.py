import sys 

def mysolution():
    input = sys.stdin.readline
    money = int(input())
    jun_money, jun_stock = money, 0
    sung_money, sung_stock = money, 0 
    prices = list(map(int, input().split()))
    
    
    for i in range(14):
        price = prices[i]
        
        if price<=jun_money:
            stock = jun_money//price
            jun_money -= stock*price
            jun_stock += stock
    
    for i in range(1,12):
        if prices[i-1]<prices[i]<prices[i+1]<prices[i+2]:
            sung_money += prices[i+2]*sung_stock
            sung_stock = 0 
        elif prices[i-1]>prices[i]>prices[i+1]>prices[i+2]:
            stock = sung_money//prices[i+2]
            sung_money -= stock*prices[i+2]
            sung_stock += stock
        
    jun = jun_money + jun_stock*price
    sung = sung_money + sung_stock*price
    
    if jun>sung:
        print("BNP")
    elif jun<sung:
        print("TIMING")
    else:
        print("SAMESAME")
        
        
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()