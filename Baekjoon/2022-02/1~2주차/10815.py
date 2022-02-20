import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    mycards = list(map(int, input().split()))
    mycards.sort()
        
    m = int(input())
    cards = list(map(int, input().split()))
    
    answer = [0]*m
    
    def search(num):
        left = 0
        right = len(mycards)-1
        
        while left<=right:
            mid = (left+right)//2
            if mycards[mid]==num:
                return True
            if mycards[mid]<num:
                left = mid+1
            else:
                right = mid-1
        return False    
        
    for i in range(len(cards)):
        if search(cards[i]):
            answer[i] = 1
            
    print(' '.join(list(map(str, answer))))
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    mycards = list(map(int, input().split()))
    mycards.sort()
        
    m = int(input())
    cards = list(map(int, input().split()))
    
    def binary_search(target, left, right):
        while left<=right:
            mid = (left+right)//2
            
            if mycards[mid] == target:
                return True
            elif mycards[mid] > target:
                left = mid -1 
            else:
                right = mid + 1
        return False
    
    for i in range(m):
        if binary_search(cards[i], 0, n-1):
            print(1, end=' ')
        else:
            print(0, end=' ')
            
if __name__=='__main__':
    mysolution()