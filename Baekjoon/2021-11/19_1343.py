def mysolution():
    board = input().split('.')
    answer = []
    for b in board:
        if len(b)%2==1:
            print(-1)
            return
        
        tmp = ''
        if b == '':
            answer.append('.')
        
        while b:
            if len(b)%4==0:
                tmp += 'AAAA'
                b = b[4:]
            elif len(b)%2==0:
                tmp += 'BB'
                b = b[2:]
        answer.append(tmp)
        answer.append('.')
    
    print(''.join(answer)[:-1])
                
def solution():
    board = input()
    board = board.replace('XXXX','AAAA')
    board = board.replace('XX','BB')
    if 'X' in board:
        print(-1)
    else:
        print(board)

if __name__=='__main__':
    mysolution()