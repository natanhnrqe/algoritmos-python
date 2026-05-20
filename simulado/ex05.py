def fibonnaci(target, a=0, b=1):

    if target == 0:
        return

    print(a, end=", ")

    fibonnaci(target - 1, b, a + b)

fibonnaci(2)