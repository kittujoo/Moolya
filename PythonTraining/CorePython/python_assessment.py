def check_palindrome(str_obj="sts"):
    return str_obj == str_obj[::-1]


def get_reversed_string(str_obj='aaa'):
    return str_obj[::-1]


def factorial_of_number(n):
    factorial_of_num = 1
    for i in range(n):
        # print(i)
        factorial_of_num = factorial_of_num + (factorial_of_num * i)
    return factorial_of_num


def prime_number(number):
    import math
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            if number % i == 0:
                return False
        return True


def find_max_and_min_number_in_array(list1):
    return "minimum number is : " + str(min(list1)) + ", And Maximum number is : " + str(max(list1))


def fibonacci(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])

    print(fib_series)


def fibonacci_with_range(start, end):
    pass


def replace_string(s):
    print(s)
    print(s.replace('o', ' '))
    char = 'o'
    print(s.swapcase())
    pass


def args_kwargs():
    def example_function(arg1, *args, kwarg1='default', **kwargs):
        print(f"arg1: {arg1}")
        print(f"args: {args}")
        print(f"kwarg1: {kwarg1}")
        print(f"kwargs: {kwargs}")

    # Example usage
    example_function(1, 2, 3, kwarg1='custom', name='John', age=25)


if __name__ == "__main__":
    # print("Is a Palindrome : ",check_palindrome("akhka"))
    # print("The Factorial of Number : ",factorial_of_number(5))
    # print("Is a prime number : ",prime_number(17))
    # print(find_max_and_min_number_in_array([2,3,4,5,6,7,7,9]))
    # print(fibonacci(6))
    # replace_string("Hello World!")
    args_kwargs()