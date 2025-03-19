def func_b():
    return "Function B"

def call_a():
    import module_a
    print(module_a.func_a())

if __name__ == "__main__":
    call_a()
