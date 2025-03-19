def func_a():
    return "Function A"

def call_b():
    import module_b
    print(module_b.func_b())

if __name__ == "__main__":
    call_b()