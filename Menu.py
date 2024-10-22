from Functions import *

def menu(array:list):
    """
    The menu for the user to access all the functions.
    :param array: an empty list
    """
    print("Possible operations:")
    print("1. Add a number (type 1 or add)")
    print("2. Insert a number (type 2 or insert)")
    print("3. Remove a number (type 3 or remove)")
    print("4. Remove a range of numbers (type 4 or remove range)")
    print("5. Replace a value or a range of values (type 5 or replace)")
    print("6. Print all the primes from a range (type 6 or primes)")
    print("7. Print all the odd numbers from a range (type 7 or odd)")
    print("8. Print the sum of numbers from a range (type 8 or sum)")
    print("9. Print the greatest common divisor of the numbers from a range (type 9 or greatest common divisor)")
    print("10. Print the maximum number from a range (type 10 or max)")
    print("11. Filter all the primes (type 11 or filter primes)")
    print("12. Filter all the negatives (type 12 or filter negatives)")
    print("13. Undo the last operation (type 13 or undo)")
    print("14. Print the array (type 14 or print)")
    print("15. Stop (type stop)")
    print()
    while True:
        user_input = input()
        if user_input == "stop":
            break
        elif user_input == "1" or user_input == "add":
            print("Enter the number:")
            x = int(input())
            array = add(array,x)
            print(array)
        elif user_input == "2" or user_input == "insert":
            print("Enter the index: ")
            x = int(input())
            print("Enter the number: ")
            y = int(input())
            array = insert(array, x, y)
            print(array)
        elif user_input == "3" or user_input == "remove":
            print("Enter the index: ")
            x = int(input())
            array = remove(array, x)
            print(array)
        elif user_input == "4" or user_input == "remove range":
            print("Enter the start index: ")
            x = int(input())
            print("Enter the stop index: ")
            y = int(input())
            array = remove_range(array, x, y)
            print(array)
        elif user_input == "5" or user_input == "replace":
            print("Enter the value to be replaced: ")
            str_x = input().split(" ")
            x = []
            for i in str_x:
                try:
                    i = int(i)
                    x.append(i)
                except ValueError: pass
            print("Enter the new value: ")
            str_y = input().split(" ")
            y = []
            for i in str_y:
                try:
                    i = int(i)
                    y.append(i)
                except ValueError:
                    pass
            array = replace(array, x, y)
            print(array)
        elif user_input == "6" or user_input == "primes":
            print("Enter the start index: ")
            x = int(input())
            print("Enter the stop index: ")
            y = int(input())
            print(prime(array, x, y))
        elif user_input == "7" or user_input == "odd":
            print("Enter the start index: ")
            x = int(input())
            print("Enter the stop index: ")
            y = int(input())
            print(odd(array, x, y))
        elif user_input == "8" or user_input == "sum":
            print("Enter the start index: ")
            x = int(input())
            print("Enter the stop index: ")
            y = int(input())
            print(sum_s(array, x, y))
        elif user_input == "9" or user_input == "greatest common divisor":
            print("Enter the start index: ")
            x = int(input())
            print("Enter the stop index: ")
            y = int(input())
            print(gcd(array, x, y))
        elif user_input == "10" or user_input == "max":
            print("Enter the start index: ")
            x = int(input())
            print("Enter the stop index: ")
            y = int(input())
            print(max_x(array, x, y))
        elif user_input == "11" or user_input == "filter primes":
            print(filter_prime(array))
        elif user_input == "12" or user_input == "filter negatives":
            print(filter_negatives(array))
        elif user_input == "13" or user_input == "undo":
            array = undo(array)
            print(array)
        elif user_input == "14" or user_input == "print":
            print(array)
        else: print("Wrong input")

if __name__ == "__main__":
    array = []
    menu(array)