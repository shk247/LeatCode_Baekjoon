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
        answer += (int(b)**(size-i-1))*num
        
    print(answer)
    
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()