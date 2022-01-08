# decorator

def my_decorator(func):
    def wrap_func(*args,**kwargs):
        print('*******')
        func(*args,**kwargs)
        print('*******')

    return wrap_func

def hello(x):
    print(x)
# @my_decorator
# def hello():
    # print('hello')
x='helllllooooooo'

@my_decorator
def hello(greeting,emoji=':)'):
    print(greeting,emoji)

# hello2=my_decorator(hello)
# hello2()
hello('nam')