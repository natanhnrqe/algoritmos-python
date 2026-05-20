def retangulo(line, column):
    print("+" + "-" * (column - 2) + "+")

    for j in range(line):
        for k in range(column):
            if k == 0 or k == column - 1:
                print(end="|")
            else:
                print(end=" ")

        print()

    print("+" + "-" * (column - 2) + "+")

retangulo(10, 90)