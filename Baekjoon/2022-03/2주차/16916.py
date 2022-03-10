import sys 

def mysolution():
    input = sys.stdin.readline
    s = input().strip()
    p = input().strip()
    
    if p not in s:
        print(0)
    else:
        print(1)
    
def make_table(pattern):
    length = len(pattern)
    table = [0]*length
    j=0
    
    for i in range(1, length):
        while j>0 and pattern[i]!=pattern[j]:
            j = table[j-1]
            
        if pattern[i]  == pattern[j]:
            j += 1
            table[i] = j
        
    return table 
    
def kmp(parent, pattern):
    table = make_table(pattern)
    parent_len = len(parent)
    pattern_len = len(pattern)
    
    j=0 
    for i in range(parent_len):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]

        if parent[i] == pattern[j]:
            if j == pattern_len - 1:
                return 1
            else:
                j += 1

    return 0
 
def solution():
    input = sys.stdin.readline
    s = input().strip()
    p = input().strip()     
    print(kmp(s, p))
    
if __name__=='__main__':
    mysolution()