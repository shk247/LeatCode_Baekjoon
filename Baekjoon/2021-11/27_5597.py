import sys 

def mysolution():
    input = sys.stdin.readline
    total = [i for i in range(1,31)]
    students = []
    for _ in range(28):
        students.append(int(input()))
    answer = [t for t in total if t not in students]
    
    print(min(answer))
    print(max(answer))

def solution():
    input = sys.stdin.readline
    students = [i for i in range(1,31)]
    for _ in range(28):
        applied = int(input())
        students.remove(applied)    
    
    print(min(students))
    print(max(students))

if __name__=='__main__':
    mysolution()