def even_int(l): #1
    """
    Return the number of even integers in the list
    :param l: a list
    :return: nr(int) - the number of even integers in the list
    """
    if not isinstance(l, list):
        raise TypeError('l is not a list')
    nr = 0
    for i in l:
        if i % 2 == 0:
            nr = nr + 1
    return nr

l = []

def read_list(): #2
    """
    Read a list of integers and return it
    :return: l - the list of integers
    """
    l = input().split()
    l = [int(i) for i in l]
    return l

def sum_list(l): #3
    """
    Compute the sum of integer numbers given as a list
    :param l: the list of integers
    :return: s(int) - the sum of integers
    """
    return sum(i for i in l if i != 12)

def min_max(l): #4
    """
    Find the minimum and the maximum of a list
    :param l: the list of integers
    :return: min(int) - the minimum of the list, max(int) - the maximum of the list
    """
    return min(l), max(l)

def array_to_list(l): #5
    """
    Convert an array of integers to a set
    :param l: the array of integers
    :return: s(set) - the set
    """
    return set(l)

def sum_div(n):
    """
    Compute the sum of divisors of a number
    :param n: the integer number
    :return: s(int) - the sum of divisors
    """
    s = 0
    for i in range(1, n):
        if(n % i == 0):
            s = s + i
    return s

def friends(x,y): #6
    """
    Verify if two numbers are friends
    :param x: the first integer number
    :param y: the second integer number
    :return: True if the two numbers are friends, False otherwise
    """
    return x == sum_div(y) and y == sum_div(x)

def array(n): #7
    """
    Compute the array 1,2,2,3,3,3,... given the length of the array
    :param n: the length of the array
    :return: the array
    """
    a = []
    nr = 1
    while (n):
        for i in range(nr):
            a.append(nr)
            n = n - 1
            if(n == 0): break
        nr = nr + 1
    return a

if __name__ == '__main__':
    #l = [1,2,3,4,5,6]
    #print(even_int(l))
    #l = read_list()
    #print(sum_list(l))
    #print(min_max(l))
    #print(array_to_list(l))
    #x = int(input())
    #y = int(input())
    #print(friends(x,y))
    #n = int(input())
    #a = array(n)
    #print(a)
    pass