def mysolution():
    n = int(input())
    cnt, num = 0, 0
    while True:
        num += 1
        if str(num) == ''.join(sorted(list(str(num)), reverse=True)):
            if num <=10:
                cnt += 1
            elif num>10 and len(set(str(num)))!=1:
                cnt += 1
            if cnt == n:
                return num

def solution():
    n = int(input())
    cnt, num = 0, 1
    
    if n==0:
        return 0 
    if n>=1023:
        return -1 
    
    while True:
        str_num = str(num)
        flag = True
        
        if len(str_num) == 1:
            pass
        else:
            for i in range(1, len(str_num)):
                if int(str_num[i]) < int(str_num[i-1]):
                    continue
                else:
                    start = str_num[:i-1]
                    mid = str(int(str_num[i-1])+1)
                    end = '0' + str_num[i+1:]
                    num = int(start+mid+end)
                    flag = False
                    break
        if flag:
            cnt += 1
            if cnt == n:
                return num
            num += 1 
            
if __name__ == '__main__':
    print(solution())