from itertools import combinations

def mysolution(kids):
    com = list(combinations(kids, 7))
    answer = [c for c in com if sum(c)==100]
    
    for a in sorted(answer[-1]):
        print(a)

def solution(kids):
    total = sum(kids)

    for i in range(8):
        for j in range(i+1, 9):
            if total-(kids[i]+kids[j]) == 100:
                num1, num2 = kids[i], kids[j]
                
                kids.remove(num1)
                kids.remove(num2)

                kids.sort()

                for k in kids:
                    print(k)
                break
        if j != 8:
            break

if __name__ == '__main__':
    kids = [int(input()) for _ in range(9)]
    solution(kids)
