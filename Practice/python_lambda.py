# mypy: ignore-errors
# pylint: disable=C3001, C0114, C0116, W0621, C0103
from functools import reduce
from datetime import datetime
import re

############################################################################################
# sum of two numbers
print("sum of two numbers")
def sum_of_two(x, y):
    return x + y

sum_of_two_lambda = lambda x, y: x + y
print(sum_of_two_lambda(1, 40))

############################################################################################
# square of all the nums in the list
print("\nsquare of all the nums in the list")
def square_all(nums):
    # results = []
    # for item in nums:
    #     results.append(item ** 2)
    # return results
    return list(x**2 for x in nums)

nums = [48, 6, 9, 21, 1]
square_all_lambda = list(map(lambda num: num**2, nums))
print(square_all_lambda)

############################################################################################
# echo copies of word1
print("\necho copies of word1")
def echo_word(word1, echo):
    """Concatenate echo copies of word1."""
    words = word1 * echo
    return words

echo_word_lambda = lambda word1, echo: word1 * echo
# echo_word_lambda = lambda word1, echo: "".join(word1 for _ in range(echo))
print(echo_word_lambda("hey", 3))

############################################################################################
# get even numbers in a list
print("\nget even numbers in a list")
def is_even(nums):
    results = []
    for item in nums:
        if item % 2 == 0:
            results.append(item)
    return results

nums = [2, 99, 10, 78]
evens_by_lambda = list(filter(lambda num: num % 2 == 0, nums))
print(evens_by_lambda)

############################################################################################
# sort a list of numbers in descending order
print("\nsort a list of numbers in descending order")
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
def sort_desc(nums):
    # uses selection sort
    for left_index, _ in enumerate(nums):
        highest_index = left_index
        for index in range(left_index + 1, len(nums)):
            if nums[highest_index] < nums[index]:
                highest_index = index
        nums[left_index], nums[highest_index] = nums[highest_index], nums[left_index]
    return nums

sort_desc_lambda = sorted(nums, key=lambda x: -x)
print(sort_desc_lambda)

############################################################################################
# sum of all numbers in the list
print("\nsumming numbers")
nums = [1, 2, 3, 4, 5]
def sum_of_all(nums):
    result = 0
    for item in nums:
        result += item
    return result


def sum_of_all_recursively(current_total, index):
    if index >= len(nums):
        return current_total

    current_total += nums[index]

    return sum_of_all_recursively(current_total, index + 1)

sum_of_all_lambda = reduce(lambda x, y: x + y, nums)
# print(sum_of_all(nums))
# print(sum_of_all_recursively(0, 0))
print(sum_of_all_lambda)

############################################################################################
# sort a list of dictionaries by a specific key
print("\nsort a list of dictionaries by a specific key")

employees = [
    {"name": "John", "age": 32},
    {"name": "Jane", "age": 27},
    {"name": "Jim", "age": 40},
]

sorted_employeed_by_age = sorted(employees, key=lambda x: x["age"])
print(sorted_employeed_by_age)

############################################################################################
# find the employee with the highest salary in a list of employees
print("\nfind the employee with the highest salary in a list of employees")

employees = [
    {"name": "John", "salary": 50000},
    {"name": "Jane", "salary": 55000},
    {"name": "Jim", "salary": 60000},
]
highest_salary_employee = max(employees, key=lambda x: x["salary"])
print(highest_salary_employee)

############################################################################################
# implement this calculation using lambda: result = (x + 3) * 5 / 2
print("\nimplement this calculation using lambda")

def calc(x):
    return (x + 3) * 5 / 2

result = (lambda x: (x + 3) * 5 / 2)(3)
print(result)
# print(calc(3))

############################################################################################
# concat all the words in a strings list
my_list = ["Real", "Python", "test"]
def func(x):
    return " ".join(x)

# print(func(my_list))
print(reduce(lambda x, y: x + " "+ y, my_list))

############################################################################################

# EXERCISES
# https://www.w3resource.com/python-exercises/lambda/index.php

############################################################################################
# 01. Write a Python program to create a function that takes one argument, and that argument
# will be multiplied with an unknown given number.
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75
print("\nexercise 01")

def solution(unknown_num):
    return lambda given_num: given_num * unknown_num

result = solution(2)
print(result(15))

############################################################################################
# 02. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
print("\nexercise 02")
input_list = [("English", 88), ("Science", 90), ("Maths", 97), ("Social sciences", 82)]
# result = sorted(input, key=lambda x: x[1])
input_list.sort(key=lambda x: x[1])
print(input_list)

############################################################################################
# 03. Write a Python program to sort a list of dictionaries using Lambda.
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
# {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
# {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
# {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
# {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
print("\nexercise 03")
input_dict = [
    {"make": "Nokia", "model": 216, "color": "Black"},
    {"make": "Mi Max", "model": "2", "color": "Gold"},
    {"make": "Samsung", "model": 7, "color": "Blue"},
]
input_dict.sort(key=lambda x: x["color"])
print(input_dict)

############################################################################################
# 04. Write a Python program to filter a list of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]
print("\nexercise 04")
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Even: {list(filter(lambda x: x % 2 == 0, input_list))}")
print(f"Odd: {list(filter(lambda x: x % 2 != 0, input_list))}")

############################################################################################
# 05. Write a Python program to square and cube every number in a given list of integers
# using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
print("\nexercise 05")
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"square: {list(map(lambda x: x ** 2, input_list))}")
print(f"cube: {list(map(lambda x: x ** 3, input_list))}")

############################################################################################
# 06. Write a Python program to find if a given string starts with a given character using Lambda.
print("\nexercise 06")
input_str = "legend"
is_starts_with = lambda given_str, given_char: given_str[0] == given_char
print(is_starts_with(input_str, "a"))
print(is_starts_with(input_str, "l"))

############################################################################################
# 07. Write a Python program to extract year, month, date and time using Lambda.
print("\nexercise 07")
now = datetime.now()
print(f"year: {(lambda x: (now.year, now.month, now.day, now.strftime('%H:%M:%S.%f')))(input_str)}")

############################################################################################
# 08. Write a Python program to check whether a given string is a number or not using Lambda.
print("\nexercise 08")
is_number = lambda x: (
    True if re.fullmatch(r"^-?\d+", x.replace(".", "", 1)) else False
)
print(is_number('test76'))
print(is_number("76"))
print(is_number("76.90"))

############################################################################################
# 09. Write a Python program to create Fibonacci series up to n using Lambda.
# Fibonacci series upto 2:
# [0, 1]
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]
# Fibonacci series upto 6:
# [0, 1, 1, 2, 3, 5]
# Fibonacci series upto 9:
# [0, 1, 1, 2, 3, 5, 8, 13, 21]
print("\nexercise 09")

def generate_fibonacci(n):
    result = [0, 1]
    for _ in range(n-2):
        result.append(result[-1] + result[-2])
    return result

generate_fibonacci_lambda = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
print(generate_fibonacci_lambda(9))
