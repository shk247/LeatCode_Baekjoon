import sys 

def mysolution():
    input = sys.stdin.readline
    dict = {1:['  *', '  *', '  *', '  *', '  *'], 2:['***', '  *', '***', '*  ', '***'],
            3:['***', '  *', '***', '  *', '***'], 4:['* *', '* *', '***', '  *', '  *'],
            5:['***', '*  ', '***', '  *', '***'], 6:['***', '*  ', '***', '* *', '***'],
            7:['***', '  *', '  *', '  *', '  *'], 8:['***', '* *', '***', '* *', '***'],
            9:['***', '* *', '***', '  *', '***'], 0:['***', '* *', '* *', '* *', '***']}
    nums = []
    for _ in range(5):
        line = input().replace('\n',' ')
        nums.append([line[i:i+4] for i in range(0, len(line), 4)])
        
    cnt = len(nums[0])
    answer = []
    for i in range(cnt):
        tmp = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        for j in range(10):
            for k in range(5):
                if nums[k][i][:-1] != dict[j][k]:
                    tmp.remove(j)
                    break
        if not tmp:
            print('BOOM!!')
            return
        else:
            answer.append(list(tmp)[0])
    answer =  int(''.join(map(str, answer)))
    if answer%6 == 0:
        print('BEER!!')
    else:
        print('BOOM!!')
        
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()