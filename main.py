#теорія декоратори

def my_decorator_func(func): #3
    def wrapper(): #4
        print('lalalala')
        func()
        print('okeokeoke')
    return wrapper


@my_decorator_func #2
def say_hello(): #1
    print('Hello!')
say_hello()