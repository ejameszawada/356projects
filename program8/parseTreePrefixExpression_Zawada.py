# Course: CSCI 356, Section 1
# Student Name: Ethan Zawada
# Student ID: 10627257
# Program 8
# Due Date: 4/22/22
# In keeping with the Honor Code of UM, I have neither given nor received inappropriate assistance
# from anyone other than the TA or instructor.
# Program Description: This program obtains a prefix expression from the user and converts it to infix.
# It then enters the expression into a binary tree and parses the operators and operands. After this
# it calculates the expression and returns the value to the user on screen.


from stack_implementation import Stack
from binaryTreeNodes import BinaryTree
import operator

def buildParseTree(exp):
    expList = exp.split()
    expStack = Stack()
    expTree = BinaryTree('')
    expStack.push(expTree)
    currentTree = expTree

    for i in expList:
        if i == '(':
            currentTree.insertLeft('')  # add left child
            expStack.push(currentTree)  # push on stack
            currentTree = currentTree.getLeftChild()  # descend to left child
        elif i.isdigit():  # operands
            currentTree.setRootVal(int(i))  # set value
            parent = expStack.pop()
            currentTree = parent  # return to parent
        elif i in '+-*/':
            currentTree.setRootVal(i)
            currentTree.insertRight('')  # add right child
            expStack.push(currentTree)  # push on stack
            currentTree = currentTree.getRightChild()  # descend to right child
        elif i == ')':
            currentTree = expStack.pop()
        else:
            print('Error, invalid symbol', i)
    return expTree

# calculates the expression
def evaluate(parseTree):
    # list of operators
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC)) #recursion
    else: # leaf node
        return parseTree.getRootVal() #

# writes the tree as a string
def printexp(tree):
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + ')'
    return sVal


def prefixToInfix(prefix):
    arr = []
    # tokenize
    prefix = prefix.split()
    # read prefix reversed
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
            # is operand
            arr.append(prefix[i])
            i -= 1
        # is operator
        else:
            str = "(" + arr.pop() + prefix[i] + arr.pop() + ")"
            arr.append(str)
            i -= 1
    # return spaced out to be read by the tree
    return ' '.join(arr.pop())


def isOperator(op):
    if op in "(+-*/)":
        return True
    else:
        return False


def main():
    infix = input('Enter a prefix expression: ')

    converted = prefixToInfix(infix)

    tree = buildParseTree(converted)

    print('The result is:', evaluate(tree))


main()

