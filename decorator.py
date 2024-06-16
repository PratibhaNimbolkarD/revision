
def func(func):
    def wrapper(*args , **kwargs):
        print(f"{func.__name__} Started")
        func(*args, **kwargs)
        print("Ended")
    return wrapper


@func
def func1(a,b, key=1):
    print("This is function1")
    print(key)


func1(5 , 6)





