import sys 

def mysolution():
    input = sys.stdin.readline
    s = list(input().strip())
    answer = []
    tag_start = 0 
    i = 0  
    while s:
        print('i=',i, 's=',s, 'answer=',answer)
        if s[i] == '<':
            tag_start = i 
            i+=1
        elif s[i] == '>':
            answer.append(s[tag_start:i+1])
            s = s[i+1:]
            i,tag_start = 0, tag_start
        elif s[i] == ' ' and tag_start !=0 :
            answer.append(s[:i+1])
            s = s[i+1:]
            i = 0 
        else:
            i+=1
    print('answer = ', answer)
            
            
def solution():
    input = sys.stdin.readline
    word = list(input().rstrip())
    i, start = 0, 0
    while i<len(word):
        if word[i] == '<':
            i += 1
            while word[i] != '>':
                i += 1
            i+=1
        elif word[i].isalnum():
            start = i
            while i<len(word) and word[i].isalnum():
                i += 1
            tmp = word[start:i]
            tmp.reverse()
            word[start:i] = tmp
        else:
            i += 1 
            
    print(''.join(word))

if __name__=='__main__':
    mysolution()