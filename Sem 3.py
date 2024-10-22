import math

def read_to_list():
    l_str = str(input("List:")).split()
    l = []
    for i in l_str:
        try:
            i = int(i)
            l.append(i)
        except ValueError:
            print("Element " + i + " could not be added. Input value has to be a natural number.")
    return l

def list_to_string(l):
    return " ".join(str(l[i]) for i in range(len(l)))

def sum_pow_2(l):
    s = 0
    for i in l:
        c = i
        while i % 2 == 0:
            i /= 2
        if i == 1 and c != 1:
            s = s + c
    return s

# or
def sum_pow_2_2(l):
    s = 0
    for i in l:
        if i != 1 and i & i - 1 == 0:
            s = s + i
    return s

# or
def sum_pow_2_3(l):
    s = 0
    for i in l:
        if i != 1 and math.log2(i) == int(math.log2(i)):
            s = s + i
    return s

def filter_pow_2(l):
    lis = []
    for i in l:
        c = i
        while i % 2 == 0:
            i /= 2
        if i != 1 or c == 1:
            lis.append(c)
    return lis

def new_list(l):
    l1 = []
    l2 = []
    i = 0
    while l[i] % 2 == 1 and i < len(l):
        l1.append(l[i])
        i += 1
    i = len(l) - 1
    while l[i] % 2 == 1 and i < len(l):
        l2.append(l[i])
        i -= 1
    l2.reverse()
    return l1 + l2

def delete_even(l):
    for i in l:
        if i % 2 == 0:
            l.remove(i)
    return l

def longest_sequence_front(l):
    max_len = 0
    index = 0
    for i in range(len(l)):
        current_len = 0
        while l[i]%2 == 0:
            current_len += 1
            i += 1
        if current_len > max_len:
            max_len = current_len
            index = i
    return l[index - max_len : index] + l[:index - max_len] + l[index:]

if __name__ == "__main__":
    l = read_to_list()
    print(l)
    #string = list_to_string(l)
    #print(string)
    #print(sum_pow_2(l))
    #print(sum_pow_2_2(l))
    #print(sum_pow_2_3(l))
    #print(filter_pow_2(l))
    #print(new_list(l))
    #print(delete_even(l))
    #print(longest_sequence_front(l))