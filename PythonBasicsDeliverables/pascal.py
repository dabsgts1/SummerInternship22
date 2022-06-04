def pascal_row(k):
    """
    Returns a list verison of the kth row of pascal's triangle

    Parameter k: integer specifying which row of pascal's triangle to return
    """
    list1 = [1] # pascal row 1
    list2 = [1,1] # pascal row 2

    # if pascal triangle size is 1, then return list1
    if (k == 1):
        return list1
    # if pascal triangle size is 2, then return list2
    elif (k == 2):
        return list2
    # for pascal triangle size >= 3, we find the respective row
    elif (k >= 3):
        list2 = pascal_row(k-1)
        list3 = [1,1]

        for i in range(len(list2)-1):
            element = list2[i] + list2[i+1]
            list3.insert(i+1, element)

        return list3

def convert_to_string(list):
    """
    Returns a converted given list into a string with a space between each
    element of thelist.

    Parameter list: a list
    """
    s = ''
    for i in list:
        s = s + str(i) + ' '
    return s

def pascal_triangle(n):
    """
    Print pascal's triangle of n rows.

    Parameter n: integer specifying number of rows of pascal's triangle.
    """
    row = 1

    while(row <= n):
        # storing spaces in p1 for printing space
        p1 = ''
        for i in range(n-row):
            p1 = p1 + ' '

        # printing row
        print(p1 + convert_to_string(pascal_row(row)))

        # increment the row
        row = row + 1

try:
    n = input("Enter size of pyramid: ")
    n = int(n)
    pascal_triangle(n)
except:
    print("Incorrect input. Please try again.")
