import sys 

def mysolution():
    input = sys.stdin.readline
    t = int(input())
    
    for _ in range(t):
        sounds = list(input().split())
        animals = set()
        while True:
            l = input().rstrip()
            if l=="what does the fox say?":
                break
            animals.add(l.split()[2])
        
        answer = []
        
        for sound in sounds:
            if sound not in animals:
                answer.append(sound)
                
        print(*answer)
                    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()