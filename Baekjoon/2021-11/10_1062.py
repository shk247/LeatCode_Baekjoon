

def solution(k, words):
    alphabet = ['a', 'n', 't', 'i', 'c']
    k -= 5
    
    if k<0:
        return 0 

    new = []
    for word in words:
        word = list(word)
        w = set(w for w in word if w not in alphabet)
        if len(w)<=k:
            new.append(w)      
            
    if not new:
        return len(words)
    
    
    new.sort(key=lambda x : len(x))  

from itertools import combinations

def solution():
    n, k = list(map(int, input().split()))
    if k<5:
        return 0
    else:
        k-=5
        nece_chars = {'a', 'n', 't', 'i', 'c'}
        alpha = {kv:v for v, kv in enumerate(set(map(chr, range(ord('a'), ord('z')+1))) - nece_chars)}
        input_chars = []
        for _ in range(n):
            tmp = 0 
            for c in set(input()) - nece_chars:
                tmp |= (1<<alpha[c])
            input_chars.append(tmp)
        print('input_chars=',input_chars)
        power_by_2 = (2**i for i in range(21))
        
        cnt = 0
        for com in combinations(power_by_2, k):
            test = sum(com)
            ct = 0 
            for ch in input_chars:
                if test & ch == ch:
                    ct += 1
            cnt = max(cnt, ct)
        return cnt
    
if __name__ == '__main__':
    solution()
    
    n, k = list(map(int, input().split()))
    words = [input() for _ in range(n)]
    print(solution(k, words))