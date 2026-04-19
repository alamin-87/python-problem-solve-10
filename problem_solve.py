# reverse a string
def reverse_string(s: str) -> str:
    return s[::-1]          

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

# find the largest number in a list
def find_largest(nums: list) -> int:
    largest = nums[0]
    for num in nums[1:]:
        if num > largest:
            largest = num
    return largest


# check if a string is a palindrome
def is_palindrome(s: str) -> bool:
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# sum of an array
def sum_array(nums: list) -> int:
    total = 0
    for num in nums:
        total += num
    return total

# count vowels in a string
def count_vowels(s: str) -> int:
    vowels = set('aeiouAEIOU')
    return sum(1 for c in s if c in vowels)



# factorial
def factorial(n: int) -> int:
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# filter even numbers from a list
def filter_evens(nums: list) -> list:
    return [n for n in nums if n % 2 == 0]


# fibonacci sequence
def fibonacci(n: int) -> list:
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq



# find minimum in a list
def find_minimum(nums: list) -> int:
    minimum = nums[0]
    for num in nums[1:]:
        if num < minimum:
            minimum = num
    return minimum
