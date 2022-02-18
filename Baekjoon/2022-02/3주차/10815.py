import sys 

def mysolution():
    input = sys.stdin.readline
    
    n = int(input())
    s_cards = list(map(int, input().split()))
    s_cards.sort()
    m = int(input())
    t_cards = list(map(int, input().split()))
    
    def search(left, right, cards, target):
        while left<=right:
            mid = (left+right)//2
            if cards[mid]==target:
                return True
            elif cards[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return False

    left, right = 0, n-1
    
    for t in t_cards:
        if search(left, right, s_cards, t):
            print(1, end=' ')
        else:
            print(0, end=' ')
            
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()