# Course: CSCI 356, Section 1
# Student Name: Ethan Zawada
# Student ID: 10627257
# Program 6
# Due Date: 4/1/2022
# In keeping with the Honor Code of UM, I have neither given nor received inappropriate assistance
# from anyone other than the TA or instructor.
# Program Description: This program uses an iterative and recursive version of a sequential
# and binary search to search through a list and find if a value is present in that list.

def sequential_iteration(arr, x):
    # check every element
    for y in arr:
        # if present return true, otherwise false
        if(y == x):
            return True
    return False


def sequential_recursion(arr, x, index):
    # base case
    if(index < len(arr)):
        # if element present return true
        if(arr[index] == x):
            return True
        # check the next position
        else:
            return sequential_recursion(arr, x, index+1)
    # element not found
    else:
        return False


def binary_iteration(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        # if x is larger, left side is ignored
        if arr[mid] < x:
            low = mid + 1
        # if x is smaller, right side is ignored
        elif arr[mid] > x:
            high = mid - 1
        # x is found at mid
        else:
            return True
    # element was not found
    return False


def binary_recursion(arr, low, high, x):
    # base case
    if high >= low:
        mid = (high + low) // 2
        # if it is present at middle then true
        if arr[mid] == x:
            return True
        # if x is smaller than middle, it will be in the left
        elif arr[mid] > x:
            return binary_recursion(arr, low, mid - 1, x)
        # if x is smaller than middle, it will only be in the left
        else:
            return binary_recursion(arr, mid + 1, high, x)
    # not found in the array
    else:
        return False


arr = [1, 3, 5, 7, 9]

# sequential searches
print("Sequential Search")

# search for 5
print("Iteration:", sequential_iteration(arr, 5))
# search for 2
print("Iteration:", sequential_iteration(arr, 2))

# search for 5
print("Recursive:", sequential_recursion(arr, 5, 0))
# search for 2
print("Recursive:", sequential_recursion(arr, 2, 0))

# binary searches
print("\nBinary Search")

# search for 5
print("Iteration:", binary_iteration(arr, 5))
# search for 2
print("Iteration:", binary_iteration(arr, 2))

# search for 5
print("Recursive:", binary_recursion(arr, 0, len(arr)-1, 5))
# search for 2
print("Recursive:", binary_recursion(arr, 0, len(arr)-1, 2))
