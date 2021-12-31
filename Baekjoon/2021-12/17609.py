import sys 


def check(word, left, right):
    while left<right:
        if word[left] != word[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        word = input().strip()
        left, right = 0, len(word)-1
        while left<right:
            if word[left] != word[right]:
                a = check(word, left, right-1)
                b = check(word, left+1, right)
                if a==False and b==False:
                    print(2)
                    break
                else:
                    print(1)
                    break
            else:
                left += 1
                right -= 1
        else:
            print(0)
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()