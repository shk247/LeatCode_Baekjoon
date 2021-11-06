def mysolution(n):
    if n==0:
        print(0)
        return

    list = [0, 1]
    for _ in range(n-1):
        list.append(list[-1]+list[-2])
    print(list[-1])

def solution(n):
    if n<=1:
        return n
    return solution(n-1) + solution(n-2)

    
if __name__=="__main__":
    n = int(input())
    mysolution(n)
    print(solution(n))