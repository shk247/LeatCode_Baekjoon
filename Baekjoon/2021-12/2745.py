import sys 

def mysolution():
    input = sys.stdin.readline
    n, b = input().split()
    dictionary = dict()
    for i in range(10,36):
        dictionary[chr(55+i)] = i
    answer = 0
    size = len(n)
    for i in range(size):
        if n[i].isalpha():
            num = dictionary[n[i]]
        else:
            num = n[i]
        answer += (int(b)**(size-i-1))*int(num)
        
    print(answer)
    
    
def solution():
    input = sys.stdin.readline
    n, b = input().split()
    n = ''.join(reversed(n))
    b = int(b)
    
    number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    result = 0 
    
    for x in range(len(n)-1, -1, -1):
        result += number.index(n[x])*(b**x)
        
    print(result)
    
    

if __name__=='__main__':
    mysolution()