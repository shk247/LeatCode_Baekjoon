import sys 

def mysolution():
    input = sys.stdin.readline
    k = int(input())
    
    five_max = k//5
    
    for i in range(five_max, 0, -1):
        n = k 
        n -= 5*i
        if n==0:
            return i
        elif n%3==0:
            return i+(n//3)
        
    three_max = k//3

    for i in range(three_max, 0, -1):
        n = k 
        n -= 3*i
        if n==0:
            return i
        
    return -1 

def solution():
    input = sys.stdin.readline
    sugar = int(input())
    bag = 0 
    
    while sugar>=0:
        if sugar%5==0:
            bag += (sugar//5)
            return bag
        sugar -= 3
        bag += 1
    else: 
        return -1 

if __name__=='__main__':
    print(mysolution())