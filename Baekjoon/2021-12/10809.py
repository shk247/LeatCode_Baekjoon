import sys 

def mysolution():
    input = sys.stdin.readline
    word = input().strip()
    dict = {}
    for i in range(97, 123):
        dict[chr(i)] = '-1' 
        
    for i in range(len(word)):
        if dict[word[i]] == '-1':
            dict[word[i]] = str(i) 
            
    print(' '.join(dict.values()))
    
    
def solution():
    input = sys.stdin.readline
    word = input().strip()
    alphabet = list(range(97, 123))
    
    for x in alphabet:
        print(word.find(chr(x)))

if __name__=='__main__':
    mysolution()