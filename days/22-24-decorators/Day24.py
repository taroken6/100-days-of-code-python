def run():
    func1()
    func2(5)
    func3(10)
    func4('hello', 4, ('yes', False), key1='value', key2=0)


def decorator4(param):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('-- decorator4 --')
            print(f'arg param = {param}')
            res1, res2 = func(*args, **kwargs)
            print(f'args in decorator = {res1}')
            print(f'kwargs in decorator = {res2}')
            print('-- End --')

        return wrapper

    return decorator


@decorator4('param')
def func4(*args, **kwargs):
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')
    return args, kwargs


def decorator3(param):
    def decorator(func):
        def wrapper(input):
            print('-- decorator3 --')
            res = func(input)
            print(f'Add another {param} to {res} and it\'s {int(res + 10)} ')
            print('-- End --\n')

        return wrapper

    return decorator


@decorator3(10)
def func3(input):
    res = input + 10
    print(f'{res} + 10 = {int(res + 10)}')
    return res


def decorator2(func):
    def wrapper(*args):
        print('-- decorator2 --')
        func(*args)
        print('-- End --\n')

    return wrapper


@decorator2
def func2(input):
    print(f'{input} + 5 = {int(input + 5)}')


def decorator1(func):
    def wrapper():
        print('-- decorator1 --')
        func()
        print('-- End --\n')

    return wrapper


@decorator1
def func1():
    print('- func1 -')
