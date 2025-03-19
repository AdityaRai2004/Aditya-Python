import custom_module

if hasattr(custom_module, "my_function"):
    my_func = getattr(custom_module, "my_function")
    if callable(my_func):
        print(my_func)
    else:
        print("The Function cannot be found")