def mysolution():
    n = int(input())
    datas = [input() for _ in range(n)]
    for data in datas:
        num = 0 
        for i in list(data):
            if i == '(':
                num += 1
            else:
                num -= 1
            if num<0:
                print('NO')
                break
        else:
            if num == 0:    
                print('YES')
            else:
                print('NO')

def solution():
    num = int(input())

    for i in range(num):
        input_data = input()
        bracket = []
        
        for j in input_data:
            if j == '(':
                bracket.append(j)
            elif j==')':
                if len(bracket) != 0 and bracket[-1] == '(':
                    bracket.pop()
                else:
                    bracket.append(j)
                    break
        if len(bracket)==0:
            print('YES')
        else:
            print('NO')
            
if __name__=='__main__':
    mysolution()