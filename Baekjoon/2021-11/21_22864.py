def mysolution():
    a, b, c, m = map(int, input().split())
    
    if a>=m:
        print(0)
        return
    
    time = 0 
    tired = 0 
    work = 0 
    while time<24:
        time += 1
        if tired+a>=m:
            tired -= c
            if tired<0:
                tired=0
            continue
        else:
            work += b
            tired += a
    
    print(work)

if __name__=='__main__':
    mysolution()