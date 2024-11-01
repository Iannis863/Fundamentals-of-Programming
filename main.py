from Menu import menu

f = open("input.txt","rt")

def read_from_file(l:list):
    """
    Read from a file into a list
    :param l: The list where the input should be read
    :return l: The list
    :raises TypeError: If the input is not a list
    """
    if not isinstance(l, list):
        raise TypeError('Input is not a list')
    l = f.read()
    return l

def str_to_int(l_str:list):
    """
    Convert a list of strings into a list of integers
    :param l_str: The list of strings
    :return l: The list of integers
    """
    l = []
    for i in range(len(array_str)):
        l.append(int((array_str[i])))
    return l

if __name__ == "__main__":
    array_str = read_from_file([]).split()
    array = str_to_int(array_str)
    menu(array)
    f.close()