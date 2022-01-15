import sys 

def mysolution():
    mo = dict()
    m = 'aiyeou'
    for i in range(len(m)):
        mo[m[i]] = m[(i+3)%len(m)]
        mo[m[i].upper()] = m[(i+3)%len(m)].upper()
        
    ja = dict()
    j = 'bkxznhdcwgpvjqtsrlmf'
    for i in range(len(j)):
        ja[j[i]] = j[(i+10)%len(j)]
        ja[j[i].upper()] = j[(i+10)%len(j)].upper()
    
    while True:
        try:
            sentence = list(input())
        except:    
            break
    
        for s in range(len(sentence)):
            if sentence[s].lower() in m:
                sentence[s] = mo[sentence[s]] 
            elif sentence[s].lower() in j:
                sentence[s] = ja[sentence[s]] 
                
        print(''.join(sentence))
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()