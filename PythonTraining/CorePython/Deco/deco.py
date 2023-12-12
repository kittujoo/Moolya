def my_decorator(funch):
    def inner_decorator(funch):
        print('I am inner decorator')
        return funch(*args, **kwargs)

    return inner_decorator


@my_decorator
def say_hello():
    print('Hey there!')
