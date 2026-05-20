cont = 0
def fibonacci(n):


    if n == 1:
        return 1

    else:
        return f"{ n + fibonacci(n - 1)},"


fibonacci(10)
