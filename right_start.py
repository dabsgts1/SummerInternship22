try:
    n = input("Enter size of pyramid: ")
    n = int(n)
    row = 1
    # print pyramid
    while (row <= n ):
        p2 = ''
        for i in range(row):
            p2 = p2 + '* '
        print (p2)
        row = row + 1
except Exception:
    print("Invalid input. Please try again.")
