import sys

def mysolution():
    input = sys.stdin.readline
    while True:
        line = input()
        if line == "END\n":
            break
        else:
            print(line[::-1])

def solution():
    return

if __name__=='__main__':
    mysolution()