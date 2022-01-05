import sys 

def mysolution():
    input = sys.stdin.readline
    mo_check = 'aeiou'
    while True:
        word = input().strip()
        if word =='end':
            break
        mo = False
        pre = ''
        mo_cnt = 0 
        ja_cnt = 0 
        for w in word:
            if w in mo_check:
                mo = True
            if w != pre:
                pre = w
            else:
                pre += w
            if w in mo_check:
                mo_cnt += 1
                ja_cnt = 0 
            else:
                ja_cnt += 1
                mo_cnt =0 
            if mo_cnt == 3 or ja_cnt == 3:
                print('<'+word+'> is not acceptable.')   
                break 
            if len(pre) == 2 and pre == pre[::-1]:
                if pre!='ee' and pre!='oo':
                    print('<'+word+'> is not acceptable.')    
                    break
        else:
            if mo == False:
                print('<'+word+'> is not acceptable.')   
            else:
                print('<'+word+'> is acceptable.')    
                
        
def solution():
    input = sys.stdin.readline
    l = 'aeiou'
    while True:
        s = input().strip()
        if s == 'end':
            break
        che, che2 = 0, 0
        for i in s:
            if i in l:
                che2 = 1 
        for i in range(1, len(s)):
            if s[i]==s[i-1] and s[i] not in 'eo':
                che = 1
        for i in range(len(s)-2):
            if s[i] in l and s[i+1] in l and s[i+2] in l:
                che = 1
            elif s[i] not in l and s[i+1] not in l and s[i+2] not in l:
                che = 1 
        if che == 1 and che2 == 0:
            print("<" + s + "> is not acceptable." )
        else: 
            print("<" + s + "> is acceptable." )
            
    

if __name__=='__main__':
    mysolution()