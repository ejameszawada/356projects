# Course: CSCI 356, Section 1
# Student Name: Ethan Zawada
# Student ID: 10627257
# Program 3
# Due Date: 2/25/22
# In keeping with the Honor Code of UM, I have neither given nor received inappropriate assistance
# from anyone other than the TA or instructor.
# Program Description: This program takes a string and reverses it uses two different stack implementations
# and finds the time it takes both respective implementations to reverse the given string.

from stackA import Stack as StackA
from stackB import Stack as StackB
import timeit

def reverseString1(string):
    # holder for the reversed string
    reverse = ""
    # instantiation of stack from StackA class
    s1 = StackA()
    # push character by character of the string
    for i in string:
        s1.push(i)
    # pop off the values one by one and appending them onto the end of the string
    for i in range(s1.size()):
        reverse += s1.pop()
    return reverse

# the same as the other function
def reverseString2(string):
    s2 = StackB()
    reverse = ""
    for i in string:
        s2.push(i)
    for i in range(s2.size()):
        reverse += s2.pop()
    return reverse

# the string we will be reversing
inputString = "Python programming is fun"
# this is to check the time difference
testString = inputString * 200

# timer for both function
t1 = timeit.Timer('reverseString1(testString)', 'from __main__ import reverseString1, testString')
t2 = timeit.Timer('reverseString2(testString)', 'from __main__ import reverseString2, testString')

def main():
    # print both reversed string using both respective classes
    print(reverseString1(inputString))
    print(reverseString2(inputString))
    # print the time it takes for both functions
    print("\nTime for reverseString1 is", t1.timeit(1000))
    print("Time for reverseString2 is", t2.timeit(1000))

main()