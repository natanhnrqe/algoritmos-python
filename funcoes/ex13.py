def retangulo(line, column):

    for j in range(line):

        if j == 0 or j == line - 1:
            for i in range(column):
                print(end="_ ")

        print()

        for k in range(column):
            if k == 0 or k == column - 1:
                print(end="| ")
            else:
                print(end="  ")


retangulo(5, 8)