from typing import AnyStr


def mysolution(building):
    return

def solution(buildings):
    total = 0 
    for i in range(len(buildings)):
        max_left = max(buildings[:i+1])
        max_right = max(buildings[i:])
        low = min(max_left, max_right)
        total += abs(buildings[i]-low)
    return total
        
if __name__ == '__main__':
    w, h = list(map(int, input().split()))
    buildings = list(map(int, input().split()))
    print(solution(buildings))