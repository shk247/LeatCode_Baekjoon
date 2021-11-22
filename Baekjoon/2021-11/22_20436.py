def mysolution():
    left, right = input().split(' ')
    dict = {'q':[0,0], 'w':[0,1], 'e':[0,2], 'r':[0,3], 't':[0,4], 'y':[0,5], 'u':[0,6], 'i':[0,7], 'o':[0,8], 'p':[0,9],
            'a':[1,0], 's':[1,1], 'd':[1,2], 'f':[1,3], 'g':[1,4], 'h':[1,5], 'j':[1,6], 'k':[1,7], 'l':[1,8],
            'z':[2,0], 'x':[2,1], 'c':[2,2], 'v':[2,3], 'b':[2,4], 'n':[2,5], 'm':[2,6]}
    vowel = ['y','u','i','o','p','h','j','k','l','b','n','m']
    
    line = input()
    
    time = 0 
    left = dict[left]
    right = dict[right]
    
    for l in line:
        next = dict[l]
        if l in vowel:
            time += abs(right[0]-next[0])+abs(right[1]-next[1]) + 1
            right = next
        else:
            time += abs(left[0]-next[0])+abs(left[1]-next[1]) + 1
            left = next
    
    print(time)

def solution():    
    return

if __name__=='__main__':
    mysolution()