def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.
    :param n: The position in the Fibonacci sequence.
    :return: The nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    :param n: The number to calculate the factorial of.
    :return: The factorial of the number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def f_n_3(n):
    """
    Calculate the sum of the first n multiples of 3 using recursion.
    :param n: The number of terms to sum.
    :return: The sum of the first n multiples of 3.
    """
    if n == 0:
        return 0
    else:
        return 3 + f_n_3(n-1)

def recursive_sum(n):
    """
    Calculate the sum of the first n natural numbers using recursion.
    :param n: The number of terms to sum.
    :return: The sum of the first n natural numbers.
    """
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n-1)

def pascal_triangle(n):
    """
    Generate the nth row of Pascal's triangle using recursion.
    :param n: The row number to generate.
    :return: A list representing the nth row of Pascal's triangle.
    """
    if n == 0:
        return [1]
    else:
        prev = pascal_triangle(n-1)
        result = [1]
        for i in range(1, n):
            result.append(prev[i-1] + prev[i])
        result.append(1)
        return result

def print_pascal_triangle(n):
    """
    Print the first n rows of Pascal's triangle.
    :param n: The number of rows to print.
    """
    for i in range(n):
        print(pascal_triangle(i))

def min_recursion(lst):
    """
    Find the minimum value in a list from 0 to n using recursion.
    :param lst: The list.
    :return: The minimum value in the list.
    """
    n = len(lst)
    if n == 0:
        return 1000000000
    else:
        return min(lst[0], min_recursion(lst[1:]))

def max_recursion(lst):
    """
    Find the maximum value in a list using recursion.
    :param lst: The list.
    :return: The maximum value in the list.
    """
    n = len(lst)
    if n == 0:
        return 0
    else:
        return max(lst[0], max_recursion(lst[1:]))

def recursive_min(lst):
    """
    Find the minimum value in a nested list using recursion.
    :param lst: The nested list to search.
    :return: The minimum value in the list.
    """
    if len(lst) == 0:
        return 1000000000
    else:
        if isinstance(lst[0], list):
            return min(recursive_min(lst[0]), recursive_min(lst[1:]))
        else:
            return min(lst[0], recursive_min(lst[1:]))

def number_of_occurrences(lst, n):
    """
    Count the number of occurrences of a value in a nested list using recursion.
    :param lst: The nested list to search.
    :param n: The value to count.
    :return: The number of occurrences of the value in the list.
    """
    if len(lst) == 0:
        return 0
    else:
        if isinstance(lst[0], list):
            return number_of_occurrences(lst[0], n) + number_of_occurrences(lst[1:], n)
        else:
            if lst[0] == n:
                return 1 + number_of_occurrences(lst[1:], n)
            else:
                return number_of_occurrences(lst[1:], n)

def sequential_search_recursive(lst, n):
    """
    Perform a sequential search for a value in a list.
    :param lst: The list to search.
    :param n: The value to search for.
    :return: The index of the value if found, otherwise -1.
    """
    if len(lst) == 0:
        return -1
    elif lst[0] == n:
        return 0
    else:
        result = sequential_search_recursive(lst[1:], n)
        if result == -1:
            return -1
        else:
            return 1 + result

def binary_search_recursive(lst, n, left=0, right=None):
    """
    Perform a binary search for a value in a sorted list using recursion.
    :param lst: The sorted list to search.
    :param n: The value to search for.
    :param left: The left boundary of the search range.
    :param right: The right boundary of the search range.
    :return: The index of the value if found, otherwise -1.
    """
    if right is None:
        right = len(lst) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if lst[mid] == n:
        return mid
    elif lst[mid] < n:
        return binary_search_recursive(lst, n, mid + 1, right)
    else:
        return binary_search_recursive(lst, n, left, mid - 1)
