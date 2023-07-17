from typing import List


# Given an array of integer values,
# return the array in reverse order
def flip_array(arr: List[int]) -> List[int]:
    return arr[::-1]


# Given an array of integer values,
# return the count of even integers in the array
def count_evens(arr: List[int]) -> List[int]:
    return len([i for i in arr if i % 2 == 0]) 


# Given 'n' Fibonacci index,
# return an array representing the fibonacci numbers inclusive
# 6 -> [0,1,2,3,5,8,13]
def generate_fibonacci(index: int) -> List[int]:
    sequence_fibonacci = [0,1]
    
    while len(sequence_fibonacci) <= index:
        sequence_fibonacci.append(sequence_fibonacci[-1] + sequence_fibonacci[-2]) 
        
    if index > 2:
        return sequence_fibonacci
    elif index <= 2:
        return sequence_fibonacci[:index + 1]

# Given an integer array,
# return the array with the duplicate values removed.
# [8, 13, 13, 9, 11, 12] → [8, 13, 9, 11, 12]
def array_deduplication(int_arr: List[int]) -> List[int]:
    return []


# Given an integer array,
# return the array sorted lowest to highest.
# CHALLENGE: Write a Sorting algorithm,
# don't use the sorted() function
# [8, 13, 9, 12] → [8, 9, 12, 13]
def array_sort(arr: List[int]) -> List[int]:
    return []


# Given 2 arrays A and B,
# return an array that is the intersection of A and B.
# [1, 3, 5], [1, 5, 7] → [1, 5]
# [1], [1, 5, 7] → [1]
# [1, 1, 1], [1, 5, 7] → [1]
# [], [] → []
def array_intersection(a: List[int], b: List[int]) -> List[int]:
    return []


# Given an integer value,
# return its corresponding roman numeral
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
def int_to_roman(num: int) -> str:
    return ''


# Given a roman numeral,
# return the corresponding integer value
def roman_to_int(roman: str) -> int:
    return 0


# Given an integer "n",
# return the count of trailing zeroes in "n!"
# Case 1
# Input: n = 5
# Output: 1
# Factorial of 5 is 120 which has one trailing 0.
# Case 2
# Input: n = 20
# Output: 4
# Factorial of 20 is 2432902008176640000 which has 4 trailing zeroes.
def factorial_trailing_zeros(n: int) -> int:
    return 0


# Given an array of integers and a target integer value,
# return the indices of the two numbers that add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
def two_sum(self, nums: List[int], target: int) -> List[int]:
    return []
