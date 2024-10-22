l_undo = []

def add(l:list, value:int|float):
    """
    Add the value as the last element of the list.
    :param l: the list where the value will be added.
    :param value: the value to be added to the list.
    :return list: the list with the added value.
    :raises: TypeError
    """
    if not isinstance(value, int) and not isinstance(value, float) or not isinstance(l, list):
        raise TypeError("Incorrect input data for list and value")
    global l_undo
    l_undo = l.copy()
    l.append(value)
    return l

def insert(l:list, index:int, value:int|float):
    """
    Insert the value on the index position in the list.
    :param l: The list where the value will be inserted.
    :param index: The position where the value will be inserted.
    :param value: The value to be inserted in the list on the index position.
    :return l: The list with the inserted value.
    :raises: TypeError
    """
    if not isinstance(value, int) and not isinstance(value, float) or not isinstance(l, list) or not isinstance(index, int) or index < 0:
        raise TypeError("Incorrect input data for list, index and value")
    global l_undo
    l_undo = l.copy()
    l.insert(index,value)
    return l

def remove(l:list, index:int):
    """
    Remove the value at the index position in the list.
    :param l: The list where the value will be removed from.
    :param index: The position of the value to be removed.
    :return l: The list with the removed value.
    :raises: TypeError
    """
    if not isinstance(index, int) or not isinstance(l, list) or index > len(l) or index < 0:
        raise TypeError("Incorrect input data for list and index")
    global l_undo
    l_undo = l.copy()
    l.remove(index)
    return l

def remove_range(l:list, index_start:int, index_end:int):
    """
    Remove the values from the index_start position in the list to the index_end position in the list.
    :param l: The list where the values will be removed from.
    :param index_start: The position of the first value to be removed.
    :param index_end: The position of the last value to be removed.
    :return l: The list with the removed values.
    :raises: TypeError
    """
    if not isinstance(index_start, int) or not isinstance(index_end, int) or not isinstance(l, list) or index_start < 0 or index_end > len(l):
        raise TypeError("Incorrect input data for list, index_start and index_end")
    global l_undo
    l_undo = l.copy()
    for i in range(index_start, index_end + 1):
        l.pop(index_start)
    return l

def replace(l:list, old_value:int|float|list, new_value:int|float|list):
    """
    Replace every instance of the old value in the list with the new value.
    :param l: The list where the values will be replaced.
    :param old_value: The value to be replaced.
    :param new_value: The value replacing the old value.
    :return l: The list with the replaced values.
    """
    if not isinstance(old_value, int) and not isinstance(old_value, float) and not isinstance(old_value, list) or not isinstance(new_value, int) and not isinstance(new_value, float) and not isinstance(new_value, list) or not isinstance(l, list):
        raise TypeError("Incorrect input data for list, old_value and new_value")
    global l_undo
    l_undo = l.copy()
    if isinstance(old_value, list) and isinstance(new_value, list):
        for i in range(len(l)):
            if l[i:i+len(old_value)] == old_value:
                l[i:i + len(old_value)] = new_value
    else:
        for i in range(len(l)):
            if l[i] == old_value:
                l[i] = new_value
    return l

def prim(x:int):
    """
    Compute if a number is prime
    :param x: The number tested
    :return: True if the number is prime and False otherwise
    :raises: TypeError
    """
    if not isinstance(x, int):
        raise TypeError("Incorrect input data")
    if x<2: return False
    if x==2: return True
    if x%2==0: return False
    for i in range(3,x,2):
        if x % i == 0:
            return False
    return True

def prime(l:list, index_start:int, index_stop:int):
    """
    Return the prime numbers from the position index_start in the list to the position index_stop in the list.
    :param l: The list to be tested
    :param index_start: The start position in the list
    :param index_stop: The stop position in the list
    :return res: The array with all the prime numbers from the index_start position to the index_stop position
    :raises: TypeError
    """
    res = []
    if not isinstance(l,list) or not isinstance(index_start,int) or not isinstance(index_stop,int) or index_start < 0 or index_stop > len(l):
        raise TypeError("Incorrect input data")
    for i in range(index_start, index_stop + 1):
        if prim(l[i]):
            res.append(l[i])
    return res

def odd(l:list, index_start:int, index_stop:int):
    """
    Return the odd numbers from the position index_start in the list to the position index_stop in the list.
    :param l: The list to be tested
    :param index_start: The start position in the list
    :param index_stop: The stop position in the list
    :return res: The array with all the odd numbers from the index_start position to the index_stop position
    :raises: TypeError
    """
    res = []
    if not isinstance(l,list) or not isinstance(index_start,int) or not isinstance(index_stop,int) or index_start < 0 or index_stop > len(l):
        raise TypeError("Incorrect input data")
    for i in range(index_start, index_stop + 1):
        if l[i] % 2 == 1:
            res.append(l[i])
    return res

def sum_s(l:list, index_start:int, index_stop:int):
    """
    Return the sum of numbers from the position index_start in the list to the position index_stop in the list.
    :param l: The list to be tested
    :param index_start: The start position in the list
    :param index_stop: The stop position in the list
    :return s: The sum of all the numbers from the index_start position to the index_stop position
    :raises: TypeError
    """
    s = 0
    if not isinstance(l,list) or not isinstance(index_start,int) or not isinstance(index_stop,int) or index_start < 0 or index_stop > len(l) + 1:
        raise TypeError("Incorrect input data")
    for i in range(index_start, index_stop + 1):
        s = s + l[i]
    return s

def euclid(x:int, y:int):
    """
    Compute the greatest common divisor of two numbers
    :param x: The first number
    :param y: The second number
    :return x: The greatest common divisor of x and y
    :raises: TypeError
    """
    if not isinstance(x,int) or not isinstance(y,int):
        raise TypeError("Incorrect input data")
    while x!=y:
        if x>y:
            x = x - y
        else:
            y = y - x
    return x

def gcd (l:list, index_start:int, index_stop:int):
    """
    Return the greatest common divisor of the numbers from the position index_start in the list to the position index_stop in the list.
    :param l: The list to be tested
    :param index_start: The start position in the list
    :param index_stop: The stop position in the list
    :return d: The greatest ccommon divisor of all the numbers from the index_start position to the index_stop position
    :raises: TypeError
    """
    d = l[index_start]
    if not isinstance(l,list) or not isinstance(index_start,int) or not isinstance(index_stop,int) or index_start < 0 or index_stop > len(l):
        raise TypeError("Incorrect input data")
    for i in range(index_start + 1, index_stop + 1):
        d = euclid(d,l[i])
    return d

def max_x(l:list, index_start:int, index_stop:int):
    """
    Return the maximum of the numbers from the position index_start in the list to the position index_stop in the list.
    :param l: The list to be tested
    :param index_start: The start position in the list
    :param index_stop: The stop position in the list
    :return s: The maximum of all the numbers from the index_start position to the index_stop position
    :raises: TypeError
    """
    if not isinstance(l,list) or not isinstance(index_start,int) or not isinstance(index_stop,int) or index_start < 0 or index_stop > len(l):
        raise TypeError("Incorrect input data")
    m = 0
    for i in range(index_start, index_stop + 1):
        if l[i] > m:
            m = l[i]
    return m

def filter_prime(l:list):
    """
    Filter the prime numbers from the list.
    :param l: The list to be filtered
    :return l: The filtered array.
    :raises: TypeError
    """
    res = []
    if not isinstance(l,list):
        raise TypeError("Incorrect input data")
    for i in range(len(l)):
        if prim(l[i]):
            res.append(l[i])
    l = res
    return l

def filter_negatives(l:list):
    """
    Filter the negative numbers from the list.
    :param l: The list to be filtered
    :return l: The filtered array.
    :raises: TypeError
    """
    res = []
    if not isinstance(l,list):
        raise TypeError("Incorrect input data")
    for i in range(len(l)):
        if l[i] < 0:
            res.append(l[i])
    l = res
    return l

def undo(l:list):
    l = l_undo
    return l

if __name__ == "__main__":
    array = []
