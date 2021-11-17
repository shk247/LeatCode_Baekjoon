from collections import deque

def mysolution():
    card = deque([i for i in range(1, int(input())+1)])
    while len(card)>2:
        card.popleft()
        card.append(card.popleft())
    print(card[-1])
    
def solution():
    return

if __name__=='__main__':
    mysolution()