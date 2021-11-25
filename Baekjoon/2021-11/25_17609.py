import sys 
                
def wordcheck(word, left, right):
    while left<right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return 2
    return 1
                
def mysolution():
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        word = input().strip()
        left, right = 0, len(word)-1
        while left < right:
            if word[left] == word[right]:
                left += 1
                right -= 1
            else:
                l_check = wordcheck(word, left+1, right)
                r_check = wordcheck(word, left, right-1)
                if l_check == r_check == 2:
                    print(2)
                    break
                else:
                    print(1)
                    break
        else:
            print(0)       
            
def second_check(word, left, right):
    while left<right:
        if word[left] == word[right]:
            left += 1
            right -= 1 
        else:
            return False
    return True
            
def first_check(word, left, right):
    while left<right:
        if word[left] == word[right]:
            left += 1
            right -= 1 
        else:
            check1 = second_check(word, left+1, right)
            check2 = second_check(word, left, right-1)
            
            if check1 or check2:
                return 1
            else:
                return 2
    return 0 
               
def solution():
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        word = input().strip()
        left, right = 0, len(word)-1
        ans = first_check(word, left, right)
        print(ans)         
        

if __name__=='__main__':
    solution()