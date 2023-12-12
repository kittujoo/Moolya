def dict_example():
    l1 = ['Google', 'Apple']
    l2 = [['Pixel_mobile', 'Ipods'], ['Mac_book', 'IPhone']]

    # for key,value in zip(l1,l2):
    #     print(key,value)

    produts1 = dict(zip(l1, tuple(l2)))

    print(produts1)

    produts = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
    sum = 0
    for i in 'abc':
        print(i)
        print(produts[i])
        sum = sum + produts[i]

    print(sum)


# dict_example()

def decorator_example():
    def my_decorator(func):
        def wrapper():
            # print("Something is happening before the function is called.")
            ret_stmt = func()
            if ret_stmt == "Exception":
                func()
                print("Something is happening after the function is called.")

        return wrapper

    @my_decorator
    def say_hello():
        print("Hello!")
        return "Exception"

    # Calling the decorated function
    say_hello()


# decorator_example()
def lambda_example():
    result = lambda a, b: a + b

    print(type(result([1], [2])))
    print((result([1], [2])))


# lambda_example()

def filter_example():
    # Example 1: Filter even numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def is_even(num):
        return num % 2 == 0

    even_numbers = list(filter((lambda num: num % 2 == 0), numbers))
    print("Even numbers:", even_numbers)

    # Example 2: Filter names starting with 'A'
    names = ["Alice", "Bob", "Charlie", "David", "Anna", "Eva"]

    def starts_with_a(name):
        return name.startswith("A")

    names_starting_with_a = list(filter(starts_with_a, names))
    print("Names starting with 'A':", names_starting_with_a)


# filter_example()

def my_decorator_example():
    def my_decorator(*args, **kwargs):

        def wrapper():
            print("Before")
            func()
            print("After")

        return wrapper()

    @my_decorator
    def smaple_dec_main(a, b):
        print('Sample dec main',a,b)


my_decorator_example()
