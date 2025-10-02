# my_module.py

# variable

__version__ = 0.1

def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiple(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


if __name__ == "__main__":
    result = plus(10, 20)
    print(result)   
    result = minus(20, 10)
    print(result)
