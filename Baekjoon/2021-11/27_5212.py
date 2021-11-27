import sys, copy

def mysolution():
    input = sys.stdin.readline
    r, c = list(map(int, input().split()))
    board = [['.']*(c+2)]

    for _ in range(r):
        tmp = '.'+input().strip()+'.'
        tmp = list(tmp)
        board.append(tmp)
        
    board.append(['.']*(c+2))
        
    minX, minY = 11, 11
    maxX, maxY = -1, -1 
    
    answer = copy.deepcopy(board)
    
    for i in range(1, r+1):
        for j in range(1, c+1):
            if board[i][j] == 'X':
                cnt = 0 
                if board[i-1][j] == '.':
                    cnt += 1
                if board[i+1][j] == '.':
                    cnt += 1    
                if board[i][j-1] == '.':
                    cnt += 1    
                if board[i][j+1] == '.':
                    cnt += 1    
                
                if cnt>2:
                    answer[i][j] = '.' 
                else:
                    minX, minY, maxX, maxY = min(minX, j), min(minY, i),  max(maxX, j), max(maxY, i)
    
    for i in range(minY, maxY+1):
        tmp = ''
        for j in range(minX, maxX+1):
            tmp += answer[i][j]
        print(tmp)
    
                 

def solution():
    input = sys.stdin.readline
    r, c = map(int, input().split())

    graph = []
    for i in range(r):
        graph.append(list(input()))
    new_graph = copy.deepcopy(graph)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for x in range(r):
        for y in range(c):
            if graph[x][y] == '.':
                continue
            cnt = 0 
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx<0 or nx>=r or ny<0 or ny>=c:
                    cnt += 1
                elif graph[nx][ny] == '.':
                    cnt += 1
            if cnt >= 3:
                new_graph[i][j] = '.'
                
    start_row = 0
    start_col = 0
    end_row = 0
    end_col = 0
    min_index = c-1
    max_index = 0
    
    for i in range(r):
        if 'X' in new_graph[i]:
            start_row = i
            break

    for i in range(r-1, -1, -1):
        if 'X' in new_graph[i]:
            end_row = i
            break
    
    for i in range(start_row,  end_row+1):
        tmp = [i for i, value in enumerate(new_graph[i]) if value == 'X']
        if not tmp:
            continue
        min_tmp = tmp[0]
        max_tmp = tmp[-1]
        min_index = min(min_index, min_tmp)
        max_index = max(max_index, max_tmp)

    for i in range(start_row, end_row+1):
        for j in range(min_index, max_index+1):
            print(new_graph[i][j], end='')  
        print()
    
if __name__=='__main__':
    mysolution()