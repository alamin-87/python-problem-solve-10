# # reverse a string
# def reverse_string(s: str) -> str:
#     return s[::-1]

# print(reverse_string("hello"))     
# print(reverse_string("a"))           
# print(reverse_string(""))           


# fizzbuzz from 1 to n
def fizzbuzz(n: int) -> list:
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

print(fizzbuzz(15))


# find the largest number in a list
def find_largest(nums: list) -> int:
    largest = nums[0]
    for num in nums[1:]:
        if num > largest:
            largest = num
    return largest

print(find_largest([3, 7, 1, 9, 4]))    # 9
print(find_largest([-3, -1, -7, -2]))   # -1


# check if a string is a palindrome
def is_palindrome(s: str) -> bool:
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("racecar"))   # True
print(is_palindrome("hello"))     # False
print(is_palindrome("A man a plan a canal Panama"))  # True


# sum of an array
def sum_array(nums: list) -> int:
    total = 0
    for num in nums:
        total += num
    return total

print(sum_array([1, 2, 3, 4, 5]))  # 15
print(sum_array([]))               # 0



# count vowels in a string
def count_vowels(s: str) -> int:
    vowels = set('aeiouAEIOU')
    return sum(1 for c in s if c in vowels)

print(count_vowels("Hello World"))  # 3
print(count_vowels("rhythm"))       # 0



# factorial
def factorial(n: int) -> int:
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(0))   # 1
print(factorial(5))   # 120
print(factorial(12))  # 479001600



# filter even numbers from a list
def filter_evens(nums: list) -> list:
    return [n for n in nums if n % 2 == 0]

print(filter_evens([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
print(filter_evens([1, 3, 5]))            # []



# fibonacci sequence
def fibonacci(n: int) -> list:
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq

print(fibonacci(1))   # [0]
print(fibonacci(7))   # [0, 1, 1, 2, 3, 5, 8]



# find minimum in a list
def find_minimum(nums: list) -> int:
    minimum = nums[0]
    for num in nums[1:]:
        if num < minimum:
            minimum = num
    return minimum

print(find_minimum([4, 2, 7, 2, 1]))   # 1
print(find_minimum([-5, -1, -9]))      # -9