import sys 

def check(arr, size):
    for k in range(size):
        tmp = arr[k:]
        for i in range(1, size//2+1):
            if tmp[:i] == tmp[i:i+i]:
                return False
    return True
    
def make_arr(arr, size, n):
    if not check(arr, size):
        return -1
    if size==n:
        print(''.join(map(str, arr)))
        return 0
    
    for i in range(1, 4):
        arr.append(i)
        if make_arr(arr, size+1, n) == 0:
            return 0
        arr.pop()
         
def mysolution():
    input = sys.stdin.readline
    n = int(input())
    make_arr([], 0, n)
    
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()