# Problem Solve - Python Utility Functions

A comprehensive collection of Python utility functions for solving common programming problems. This module provides efficient implementations of classic algorithms and string operations.

## 📋 Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Features](#features)
- [Function Documentation](#function-documentation)
- [Usage Examples](#usage-examples)
- [Requirements](#requirements)
- [File Structure](#file-structure)
- [License](#license)

## 🎯 Overview

This project provides a collection of well-tested Python functions that solve fundamental programming challenges. Each function is designed with clarity and efficiency in mind, making it ideal for learning, reference, or integration into larger projects.

The functions cover various categories including:
- String manipulation and analysis
- Array/List operations
- Mathematical computations
- Classic algorithms

## 📦 Installation

To use this module, simply clone or download the repository:

```bash
git clone <repository-url>
cd problem
```

No external dependencies are required. All functions use Python's built-in libraries.

## ✨ Features

- **Type hints** for better code clarity and IDE support
- **Pure Python** implementation with no external dependencies
- **Well-documented** functions with clear docstrings
- **Efficient algorithms** optimized for common use cases
- **Comprehensive examples** for each function

## 📚 Function Documentation

### String Operations

#### `reverse_string(s: str) -> str`
Reverses a given string and returns the result.

**Parameters:**
- `s` (str): The string to reverse

**Returns:**
- str: The reversed string

**Example:**
```python
reverse_string("hello")  # Returns: "olleh"
reverse_string("Python")  # Returns: "nohtyP"
```

---

#### `is_palindrome(s: str) -> bool`
Checks if a string is a palindrome. Ignores case and non-alphanumeric characters.

**Parameters:**
- `s` (str): The string to check

**Returns:**
- bool: True if the string is a palindrome, False otherwise

**Example:**
```python
is_palindrome("A man, a plan, a canal: Panama")  # Returns: True
is_palindrome("hello")  # Returns: False
is_palindrome("racecar")  # Returns: True
```

---

#### `count_vowels(s: str) -> int`
Counts the number of vowels in a given string.

**Parameters:**
- `s` (str): The string to analyze

**Returns:**
- int: The total count of vowels (both uppercase and lowercase)

**Example:**
```python
count_vowels("hello")  # Returns: 2
count_vowels("Python")  # Returns: 1
count_vowels("aEiOu")  # Returns: 5
```

---

### Array/List Operations

#### `find_largest(nums: list) -> int`
Finds and returns the largest number in a list.

**Parameters:**
- `nums` (list): A list of numbers

**Returns:**
- int: The largest number in the list

**Example:**
```python
find_largest([3, 1, 4, 1, 5, 9])  # Returns: 9
find_largest([10, 20, 5, 15])  # Returns: 20
```

---

#### `find_minimum(nums: list) -> int`
Finds and returns the smallest number in a list.

**Parameters:**
- `nums` (list): A list of numbers

**Returns:**
- int: The smallest number in the list

**Example:**
```python
find_minimum([3, 1, 4, 1, 5, 9])  # Returns: 1
find_minimum([10, 20, 5, 15])  # Returns: 5
```

---

#### `sum_array(nums: list) -> int`
Calculates and returns the sum of all numbers in a list.

**Parameters:**
- `nums` (list): A list of numbers

**Returns:**
- int: The sum of all numbers

**Example:**
```python
sum_array([1, 2, 3, 4, 5])  # Returns: 15
sum_array([10, 20, 30])  # Returns: 60
```

---

#### `filter_evens(nums: list) -> list`
Filters and returns only the even numbers from a list.

**Parameters:**
- `nums` (list): A list of numbers

**Returns:**
- list: A new list containing only the even numbers

**Example:**
```python
filter_evens([1, 2, 3, 4, 5, 6])  # Returns: [2, 4, 6]
filter_evens([10, 15, 20, 25])  # Returns: [10, 20]
```

---

### Mathematical Functions

#### `factorial(n: int) -> int`
Calculates the factorial of a given number (n!).

**Parameters:**
- `n` (int): A non-negative integer

**Returns:**
- int: The factorial of n

**Example:**
```python
factorial(0)  # Returns: 1
factorial(5)  # Returns: 120 (5! = 5 × 4 × 3 × 2 × 1)
factorial(10)  # Returns: 3628800
```

---

#### `fibonacci(n: int) -> list`
Generates the first n numbers in the Fibonacci sequence.

**Parameters:**
- `n` (int): The number of Fibonacci numbers to generate

**Returns:**
- list: A list containing the first n Fibonacci numbers

**Example:**
```python
fibonacci(1)  # Returns: [0]
fibonacci(5)  # Returns: [0, 1, 1, 2, 3]
fibonacci(8)  # Returns: [0, 1, 1, 2, 3, 5, 8, 13]
```

---

### Classic Algorithms

#### `fizzbuzz(n: int) -> list`
Implements the classic FizzBuzz algorithm for numbers 1 to n.
- Returns "Fizz" for multiples of 3
- Returns "Buzz" for multiples of 5
- Returns "FizzBuzz" for multiples of both 3 and 5
- Returns the number as a string otherwise

**Parameters:**
- `n` (int): The upper limit (inclusive)

**Returns:**
- list: A list with FizzBuzz results

**Example:**
```python
fizzbuzz(15)
# Returns: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

fizzbuzz(5)
# Returns: ['1', '2', 'Fizz', '4', 'Buzz']
```

---

## 🚀 Usage Examples

Here are practical examples of how to use these functions:

```python
from problem_solve import (
    reverse_string,
    fizzbuzz,
    find_largest,
    is_palindrome,
    sum_array,
    count_vowels,
    factorial,
    filter_evens,
    fibonacci,
    find_minimum
)

# String Operations
print(reverse_string("Hello"))  # olleh
print(is_palindrome("noon"))  # True
print(count_vowels("Programming"))  # 3

# List Operations
numbers = [5, 2, 8, 1, 9, 3]
print(find_largest(numbers))  # 9
print(find_minimum(numbers))  # 1
print(sum_array(numbers))  # 28
print(filter_evens(numbers))  # [2, 8]

# Mathematical Functions
print(factorial(6))  # 720
print(fibonacci(6))  # [0, 1, 1, 2, 3, 5]

# Classic Algorithms
print(fizzbuzz(15))  # ['1', '2', 'Fizz', '4', 'Buzz', ...]
```

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies required

## 📁 File Structure

```
problem/
├── problem_solve.py    # Main module with all utility functions
└── README.md           # This documentation file
```

## 🔍 Notes

- All functions include type hints for better IDE support and code clarity
- Functions use efficient iterative approaches where applicable
- Edge cases are handled appropriately (e.g., empty lists, zero values)
- The implementation emphasizes readability and maintainability

## 💡 Tips for Extension

To add more functions to this module:

1. Add your function to `problem_solve.py`
2. Include proper type hints
3. Add a docstring with description, parameters, returns, and examples
4. Test your function thoroughly
5. Update this README.md with documentation

## 📄 License

This project is available for educational and personal use. Feel free to use and modify these functions as needed for your projects.

## 👨‍💻 Contributing

If you'd like to contribute improvements or additional functions:

1. Test your code thoroughly
2. Ensure type hints are included
3. Add appropriate documentation
4. Submit your changes with clear commit messages

---

**Last Updated:** April 2026

For questions or issues, please refer to the function documentation above or review the source code in `problem_solve.py`.
