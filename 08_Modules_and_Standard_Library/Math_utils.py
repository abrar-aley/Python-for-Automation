def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def square(number):
    return number ** 2

def cube(number):
    return number ** 3

def factorial(n):
    if n < 0:
        return "Factorial not defined"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_even(number):
    return number % 2 == 0

def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def demo():
    print("=== Math Utilities Demo ===")

    print(f"10 + 20 = {add(10, 20)}")
    print(f"5! = {factorial(5)}")


if __name__ == "__main__":
    demo()