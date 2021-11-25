import sys 

def mysolution():
    input = sys.stdin.readline
    check = ['a','e','i','o','u']
    while True:
        word = input().strip()
        
        if word == 'end':
            break
        
        word = list(word)
        
        consonant_cnt, vowel_cnt = 0, 0
        vowel_check = False
        
        for i in range(len(word)):
            if word[i] in check:
                vowel_check = True
                vowel_cnt += 1
                consonant_cnt = 0 
                if vowel_cnt == 3:
                    print('<'+''.join(word)+'> is not acceptable.')
                    break
            else:
                consonant_cnt += 1
                vowel_cnt = 0 
                if consonant_cnt == 3:
                    print('<'+''.join(word)+'> is not acceptable.')
                    break
            if i>0 and word[i]==word[i-1]:
                tmp = ''.join(word[i-1:i+1])
                if tmp == 'ee' or tmp == 'oo':
                    continue
                else:
                    print('<'+''.join(word)+'> is not acceptable.')
                    break
        else:
            if vowel_check:
                print('<'+''.join(word)+'> is acceptable.')
            else:
                print('<'+''.join(word)+'> is not acceptable.')
                
        
def solution():
    input = sys.stdin.readline
    l = 'aeiou'
    while True:
        s = input().strip()
        if s == 'end':
            break
        chk, chk2 = 0, 0 
        for i in s:
            if i in l:
                chk2 = 1
                break
        for i in range(1, len(s)):
            if s[i] == s[i-1] and s[i] not in 'eo':
                chk = 1
        for i in range(len(s)-2):
            if s[i] in l and s[i+1] in l and s[i+2] in l:
                chk = 1
            elif s[i] not in l and s[i+1] not in l and s[i+2] not in l:
                chk = 1
        if chk == 1 or chk2 == 0:
                print('<'+s+'> is not acceptable.')
        else:
                print('<'+s+'> is acceptable.')

if __name__=='__main__':
    solution()