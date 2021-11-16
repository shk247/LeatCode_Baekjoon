def mysolution():
    n, m = list(map(int, input().split()))
    str_dict = {}
    num_dict = {}
    
    for i in range(1, n+1):
        s = input()
        str_dict[s] = i
        num_dict[str(i)] = s
    
    answer = []
    for _ in range(m):
        search = input()
        if search.isalpha():
            answer.append(str_dict[search])
        else:
            answer.append(num_dict[search])
    
    for a in answer:
        print(a)

def solution():
    return

if __name__=='__main__':
    mysolution()