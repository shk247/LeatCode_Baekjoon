
def mysolution():
    t = int(input())
    nums = [int(input()) for _ in range(t)]
    answer = []
    
    for num in nums:
        binary = ''
        while num != 0:            
            r = num % 2
            num //= 2
            binary = str(r) + binary
        binary = binary[::-1]
        answer.extend([str(i) for i in range(len(binary)) if binary[i]=='1'])
        
    print(' '.join(answer))

def solution():
    t = int(input())
    nums = [int(input()) for _ in range(t)]
    for num in nums:
        i=0
        while num>0:
            if num%2 == 1:
                print(i, end=' ')
            num //= 2
            i += 1

if __name__ == "__main__":
    mysolution()