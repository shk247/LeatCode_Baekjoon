import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    seats = 20
    trains = [[0]*seats for _ in range(n)]
    for _ in range(m):
        l = list(map(int, input().split()))
        if l[0] == 1:
            train, seat = l[1]-1, l[2]-1
            trains[train][seat] = 1
        elif l[0] == 2:
            train, seat = l[1]-1, l[2]-1
            trains[train][seat] = 0
        elif l[0] == 3:
            train = l[1]-1
            tmp = 0
            for i in range(seats-1, 0, -1):
                trains[train][i] = trains[train][i-1] 
            trains[train][0] = 0 
        elif l[0] == 4:
            train = l[1]-1
            for i in range(0, seats-2):
                trains[train][i] = trains[train][i+1] 
            trains[train][seats-1] = 0 
    
    l = set()
    for i in range(n):
        tmp = ''.join(map(str, [j for j in range(seats) if trains[i][j]==1]))
        if tmp not in l:
            l.add(tmp)
            
    print(len(l))
    
def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    trains = [set() for _ in range(n)]
    
    for _ in range(m):
        op = list(map(int, input().split()))
        if op[0]==1:
            train, seat = op[1]-1, op[2]
            trains[train].add(seat)
        elif op[0]==2:
            train, seat = op[1]-1, op[2]
            trains[train].discard(seat)
        elif op[0]==3:
            train = op[1]-1
            tmp = set()
            for t in list(trains[train]):
                if t==20:
                    continue
                tmp.add(t+1)
            trains[train] = tmp
        elif op[0]==4:
            train = op[1]-1
            tmp = set()
            for t in list(trains[train]):
                if t==1:
                    continue
                tmp.add(t-1)
            trains[train] = tmp
    
    answer = set()
    for train in trains:
        answer.add(tuple(sorted(train)))
        
    print(len(answer))

if __name__=='__main__':
    solution()