import sys 

def mysolution():
    input = sys.stdin.readline
    # 학생 수, 졸고 있는 학생 수, 코드 보낼 학생 수, 주어질 구간 수
    n, k, q, m = map(int, input().split())
    k_list = list(map(int, input().split()))
    q_list = list(map(int, input().split()))
    students = [0]*(n+3)
    
    for i in k_list:
        students[i]=-1
        
    for i in q_list:
        if students[i]!=-1:
            for j in range(i, n+3, i):
                if students[j]!=-1:
                    students[j]=1
                    
    not_attendance = [0]*(n+3)
    
    for i in range(3, n+3):
        if students[i] == 0 or students[i] == -1:
            not_attendance[i] = not_attendance[i-1]+1
        else: 
            not_attendance[i] = not_attendance[i-1]
               
    for _ in range(m):
        a, b = map(int, input().split())
        print(not_attendance[b]-not_attendance[a-1])  
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()