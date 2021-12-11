import sys 

def mysolution():
    input = sys.stdin.readline
    word = input().strip().replace('c-','@').replace('dz=','#').replace('d-','$').replace('lj','%').replace('nj','&').replace('s=','*').replace('z=','(')
    print(len(word))
    
def solution():
    input = sys.stdin.readline
    a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    b = input().strip()
    for i in a:
        b = b.replace(i, 'a')
    print(len(b))

if __name__=='__main__':
    mysolution()