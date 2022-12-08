# Course: CSCI 356, Section 1
# Student Name: Ethan Zawada
# Student ID: 10627257
# Programming Assignment 1
# Due Date: 2/4/2022
# In keeping with the Honor Code of UM, I have neither
# given nor received assistance from anyone other than the TA or the instructor.
# Program Description: This program takes user input to form a list size of the value given. The user
# then populates the list and the program calculates the mean, median, and mode.

def main():
    stat_list = []
# get user input for size of list
    n = int(input('Enter number of integers in the list: '))
# fill list with user input
    for i in range(0, n):
        ele = int(input('Enter an integer: '))
        stat_list.append(ele)

    print('\nThis is the list: ', stat_list)
# print the mode
    print('The mode in the list is: ', end="", flush=True)
    print(*mode(stat_list), sep=', ')
# print the median and mean
    print('The median in the list is: ', median(stat_list))

    print('The mean in the list is: ', mean(stat_list))


def mode(dataset):
    frequency = {}
# find how frequent each number is
    for value in dataset:
        frequency[value] = frequency.get(value, 0) + 1
# get the most frequent
    most_frequent = max(frequency.values())
# if there are multiple modes
    modes = [modes for modes, value in frequency.items()
             if value == most_frequent]

    return modes


def median(dataset):
# sort the list and divide the length by 2
    data = sorted(dataset)
    index = len(data) // 2
# if the length divided by 2 does not equal zero then return the index
    if len(dataset) % 2 != 0:
        return data[index]

    return round((data[index - 1] + data[index]) / 2, 2)

# mean function, adds all elements from list and then divides by size of list
def mean(dataset):
    return round(sum(dataset) / len(dataset), 2)


main()
