from matplotlib import pyplot as plt
import numpy.matlib
import numpy as np
print()

# Ndarray Object
def ndarray_object():
    arr = np.array([1,2,3], dtype = complex, ndmin = 2)
    print(arr)
    print()

# Data Types
def data_types():
    teacher = np.dtype([('name', 'U20'), ('age', 'i1'), ('subject', 'U20')])
    teachers = np.array([('Aarti', 38, 'English'), ('Rajesh', 51, 'Physics')],
        dtype = teacher)
    print(teachers)
    print()

# Array Attributes
def array_attributes():
    arr = np.array([[1,2,3],[4,5,6]])
    print("Shape = " + str(arr.shape))
    print("Dimensions = " + str(arr.ndim))
    print()

# Array Creation Routines
def array_creation_routines():
    arr = np.empty([4,3], dtype = int)
    print(arr)
    print()

# Numpy Array from Existing Data
def array_existing_data():
    lis = [1,2,3,4,5]
    arr = np.asarray(lis)
    print(arr)
    print()

    s = 'Hello World'.encode()
    arr = np.frombuffer(s, dtype = 'S1') # creating an array with elements being
                                       # 1 substringed character each
    print(arr)
    print()

    list = [5,4,3,2,1]
    arr = np.fromiter(list, dtype = 'U1')
    print(arr)
    print()

# Array from Numerical Ranges
def numerical_ranges():
    arr = np.arange(10, 51, 5)
    print(arr)
    print()

    ar = np.linspace(10, 20, 5)
    print(ar)
    print()

    ar = np.logspace(1, 10, num = 10, base = 2)
    print(ar)
    print()

# Indexing and Slicing
def index_slice():
    num = [1,2,3,4,5,6,7,8,9,10]
    sli = slice(1,8,2)
    print(num[sli])
    print()

    arr = np.array([[1,2,3],[3,4,5],[4,5,6]])
    print(arr[...,0]) # printing column 1
    print()

# Advanced Indexing
def advanced_slice():
    arr = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])

    print('Our array is:')
    print(arr)
    print('\n')

    rows = np.array([0,0, 3,3])
    cols = np.array([0,2, 0,2])
    cor_elem = arr[rows,cols]

    print('The corner elements of this array as listed in a row are:')
    print(cor_elem)
    print()

    print('The elements > 5 are:')
    print(arr[arr>5])
    print()

# Broadcasting
def broadcast():
    a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]])
    b = np.array([1.0,2.0,3.0])
    print('First array:')
    print(a)
    print('\n')

    print('Second array:')
    print(b)
    print('\n')

    print('First Array + Second Array')
    print(a + b)
    print()

# Iterating Over Array
def iter_array():
    arr = np.arange(0,200,10)
    arr = arr.reshape(4,5)
    print('Original array is:')
    print(arr)
    print('\n')

    for ele in np.nditer(arr, op_flags = ['readwrite']):
        ele[...] = 0.1*ele

    print('Modified array is:')
    print(arr)
    print()

# Array Manipulation
def array_mani():
    a = [1,2,3]
    b = [4,5,6]
    print(np.concatenate((a,b)))
    print()

# Mathematical Functions
def math_func():
    arr = [-0.56, 2, 3.66]
    print(np.floor(arr))
    print(np.around(arr, 1))
    print()

# Statistical Functions
def stat_func():
    arr = np.array([[30,65,70],[80,95,10],[50,90,60]])
    print("Median = " + str(np.median(arr)))
    print("Average = " + str(np.average(arr)))
    print()

# Sort, Search, & Counting Functions
def sscf():
    arr = np.array([[30,65,70],[80,95,10],[50,90,60]])
    arr2 = np.where(arr > 65)
    print(arr[arr2])
    print()

# Byte Swapping
def byte_swap():
    a = np.array([1, 256, 8755], dtype = np.int16)

    print('Our array is:')
    print(a)
    print()

    print('Representation of data in memory in hexadecimal form:')
    print(map(hex,a))
    print()
    # byteswap() function swaps in place by passing True parameter

    print('Applying byteswap() function:')
    print(a.byteswap(True))
    print()

    print('In hexadecimal form:')
    print(map(hex,a))
    print()
    # We can see the bytes being swapped

# Copies and Views
def copies_views():
    arr = np.arange(3)
    arr2 = arr.view()
    print("ID of arr: " + str(id(arr)))
    print("ID of arr2: " + str(id(arr2)))
    print()

    arr3 = arr.copy()
    print("ID of arr: " + str(id(arr)))
    print("ID of arr3: " + str(id(arr3)))
    print()

# Matrix Library
def matlib():
    print(np.matlib.identity(5, dtype = float))
    print()
    print(np.matlib.rand(3,3))
    print()

# Linear Algebra
def linalg():
    a = np.array([[1,2],[3,4]])
    b = np.array([[11,12],[13,14]])
    print(a)
    print('dot product with')
    print(b)
    print('=')
    print(np.dot(a,b))
    print()

# Matplotlib
def matpl():
    x = np.arange(1,11)
    y = 2 * x + 5
    plt.title("Matplotlib demo")
    plt.xlabel("x axis caption")
    plt.ylabel("y axis caption")
    plt.plot(x,y)
    plt.show()

# Histogram using Matplotlib
def histo():
    a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
    plt.hist(a, bins = [0,20,40,60,80,100])
    plt.title("histogram")
    plt.show()

# TOGGLE COMMENTS to call the functions
# ndarray_object()
# data_types()
# array_attributes()
# array_creation_routines()
# array_existing_data()
# numerical_ranges()
# index_slice()
# advanced_slice()
# broadcast()
# iter_array()
# array_mani()
# math_func()
# stat_func()
# sscf()
# byte_swap()
# copies_views()
# matlib()
# linalg()
# matpl()
# histo()
