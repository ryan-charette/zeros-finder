while True:
    print("Select a type of equation:")
    print("[1] Linear")
    print("[2] Quadratic")
    print("[3] Quit Program")

    degree = input("")
    if degree == "3":
        break
    if degree != "1" and degree != "2":
        print("Invalid Input")
        continue
    if degree == "1":
        linear_str = input("Enter a function in the form y = m * (x - a) + b    ")
        linear_values = linear_str.split()
        m = float(linear_values[2])
        a_string = linear_values[6]
        a = float(a_string[ : a_string.find(')')])
        b = float(linear_values[8])

        # y = 0 = m * (x - a) + b
        # (-b/m) + a = x

        if linear_values[5] == "+": a = -a
        if linear_values[7] == "-": b = -b

        linear_zero = (-b/m) + a

        print("The function intercepts the x-axis when x equals " + str(linear_zero))
    if degree == "2":
        quadratic_str = input("Enter a function in the form y = ax^2 + bx + c    ")
        quadratic_values = quadratic_str.split()
        a_string = quadratic_values[2]
        a = float(a_string[ : a_string.find('x')])
        b_string = quadratic_values[4]
        b = float(b_string[ : b_string.find('x')])
        c = float(quadratic_values[6])

        if quadratic_values[3] == "-": b = -b
        if quadratic_values[5] == "-": c = -c

        # x = (-b +- sqrt(b^2 - 4ac)/2a
        quadratic_zero1 = (-b + (b * b - 4 * a * c) ** .5) / (2 * a)
        quadratic_zero2 = (-b - (b * b - 4 * a * c) ** .5) / (2 * a)

        print("The function intercepts the x-axis when x equals " + str(quadratic_zero1), end="")
        if quadratic_zero1 != quadratic_zero2:
            print(" or " + str(quadratic_zero2))
        else: print("/n")