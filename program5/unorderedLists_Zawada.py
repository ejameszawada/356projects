# Course: CSCI 356, Section 1
# Student Name: Ethan Zawada
# Student ID: 10627257
# Program 5
# Due Date: 3/11/2022
# In keeping with the Honor Code of UM, I have neither given nor received inappropriate assistance
# from anyone other than the TA or instructor.
# Program Description: This program uses an unordered linked list that appends values
# to the end of the list and can print the list out.

class Node:
    # constructor
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    # get value from node
    def getData(self):
        return self.data

    # get next node reference
    def getNext(self):
        return self.next

    # set value to node
    def setData(self, newdata):
        self.data = newdata

    # set next node reference
    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    # constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # check if the list is empty
    def isEmpty(self):
        return self.head == None

    # insert item to be the first item of the list
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.length += 1
        # sets head to tail if it is the first value
        if self.length == 1:
            self.tail = temp

    # gets length of list
    def size(self):
        return self.length


    # find if a value is present in the list
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    # remove function finds a value and removes it if it is found
    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
                self.length -= 1

            else:
                previous = current
                current = current.getNext()

        if not found:
            return

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


    # add values to the end of the list
    def append(self, item):
        current = self.tail
        # if there is a value at the end of the list, set the next and change the tail
        if current:
            current.setNext(Node(item))
            self.length += 1
            self.tail = current.getNext()
        # if not at the end then it should be both head and tail for the value
        else:
            self.head = Node(item)
            self.tail = Node(item)
            self.length += 1

    # iterates through the list and prints
    def printList(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
