
def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b // gcd(a, b)

def mysolution(n, m):
    print(gcd(n,m))
    print(lcm(n,m))

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    mysolution(n, m)
