def mysolution(stations):
    answer = -1e9
    total = 0
    for station in stations:
        total -= station[0]
        total += station[1]
        if total>answer:
            answer = total
    print(answer)

def solution(stations):
    passenger = 0 
    max_passenger = 0
    for station in stations:
        passenger += (station[0]-station[1])
        max_passenger = max(max_passenger, passenger)
    print(max_passenger)
        
    

if __name__ == '__main__':
    stations = [list(map(int, input().split())) for _ in range(10)]
    print(mysolution(stations))