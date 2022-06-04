try:
    n = input("Enter size of pyramid: ")
    n = int(n)
    row = 1
    # printing and calculating pyramid
    while (row <= n ):
        p1, p2 = '', ''
        for i in range(n-row):
            p1 = p1 + ' '
        for i in range(row):
            p2 = p2 + '* '
        print (p1+p2+p1)
        row = row + 1
except Exception:
    print("Invalid input. Please try again.")
