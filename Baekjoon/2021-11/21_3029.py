def mysolution():
    start = list(map(int, input().split(':')))
    end = list(map(int, input().split(':')))
    
    s = end[2]-start[2]
    if s<0:
        s += 60
        end[1] -= 1
    
    m = end[1]-start[1]
    if m<0:
        m += 60
        end[0] -= 1
        
    h = end[0]-start[0]
    
    if h<0:
        h += 24
        
    if h==0 and m==0 and s==0:
        print('24:00:00')
    else:
        answer = str(h).zfill(2)+':'+str(m).zfill(2)+':'+str(s).zfill(2)
        print(answer)
        
def solution():
    h1, m1, s1 = map(int, input().split(':'))
    h2, m2, s2 = map(int, input().split(':'))
    
    t1 = h1*60*60 + m1*60 + s1
    t2 = h2*60*60 + m2*60 + s2
   
    t = t2-t1 if t2>t1 else t2-t1+24*60*60 
    
    h = t//60//60
    m = t//60%60 
    s = t%60
    
    print("%02d:%02d:%02d"%(h,m,s))
    
    

if __name__=='__main__':
    mysolution()