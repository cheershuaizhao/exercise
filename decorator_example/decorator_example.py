def my_decorator(some_function):
    def wrapper():
        num = 10
        if num == 10:
            print("yes!")
        else:
            print("no!")
        some_function()
        print("Something is happending after some_function() is called.")
    return wrapper

def just_some_function():
    print("wheee!")

just_some_function = my_decorator(just_some_function)
just_some_function()
