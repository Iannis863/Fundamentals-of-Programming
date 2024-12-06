def ex1(n):
    if n % 9 == 0:
        return 9
    return n % 9


def ex5(k):
    x = 1
    while (k >= x):
        k = k - x
        x = x + 1
    if (k == 0):
        return x - 1
    return x

def ex9():
    for i in range(100):
        if (i * i % 10 == i % 10):
            print(i, " ")


def nrcif(n):
    nr = 0
    while (n):
        nr = nr + 1
        n = int(n / 10)
    return nr

def pow(n):
    p = 1
    while(n):
        p = p*10
        n = n - 1
    return p

def prime(n):
    if(n<2): return False
    if(n==2): return True
    if(n%2==0): return False
    for i in range(3,n,2):
        if(n%i==0): return False
    return True

def ex11(n):
    p = int(pow(n)/10)
    for i in range(p,p*10):
        c = i
        while(i != 1):
            if(prime(i) == False):
                break
            i = int(i/10)
        if(i == 0):
            print(c)

def ex13(n):
    p = 1
    digit = nrcif(n)
    nr = 0
    while (n):
        if (digit % 2 == 1):
            nr = (n % 10) * p + nr
            p = p * 10
        digit = digit - 1
        n = int(n / 10)
    return nr


def sumdig(n):
    s = 0
    while (n):
        s = s + n % 10
        n = int(n / 10)
    return s


def ex17(n):
    for i in range(n, n - 9 * nrcif(n), -1):
        if (n == i + sumdig(i)):
            return True
    return False


if __name__ == "__main__":
    n = int(input())
    # print(ex1(n))
    # k = int(input())
    # print(ex5(k))
    # ex9()
    # print(ex13(n))
    # print(ex17(n))
    ex11(n)
    pass