# Course: CSCI 356, Section 1
# Student Name: Ethan Zawada
# Student ID: 10627257
# Program 4
# Due Date: 3/4/2022
# In keeping with the Honor Code of UM, I have neither given nor received inappropriate assistance
# from anyone other than the TA or instructor.
# Program Description: The program is used to convert a standard math function to a postfix expression
#the program can then perform the given postfix expression to find the answer to the expression

#import stack file
from Stack import Stack as Stack

#first function definition
def infixToPostfix(userExpression):
    #dictionary to establish order of operations
    precedent = dict()
    precedent['^'] = 4
    precedent['*'] = 3
    precedent['/'] = 3
    precedent['+'] = 2
    precedent['-'] = 2
    precedent['('] = 1

    #instantiate empty stack and array for output string
    operatorStack = Stack()
    outputString = []

    #split the string inputted by the user
    characterList = userExpression.split()

    #iterate through characters
    for i in characterList:
        #add the numbers to the output string first
        if i.isdigit():
            outputString.append(i)
        #check for parenthesis to account for them before looking for operators
        elif i == "(":
            operatorStack.push(i)
        #if the character is a left parenthesis, the stack is popped unitl the left parenthesis is gone
        elif i == ")":
            top = operatorStack.pop()
            #adds operators encountered inside parenthesis to the end of the string
            while top != '(':
                outputString.append(top)
                top = operatorStack.pop()
        #anything else should be an operator, added to the end of the string
        else:
            while (not operatorStack.isEmpty()) and (precedent[operatorStack.peek()] >= precedent[i]):
                outputString.append(operatorStack.pop())
            operatorStack.push(i)
    
    #adds all held values in the stack to the end of the output string
    while not operatorStack.isEmpty():
        outputString.append(operatorStack.pop())

    #join the array into a string and returns it
    return ' '.join(outputString)

#function to actually do the math on the postfix expression
def postfixEvaluation(userExpression):
    #instantiate the empty stack for the numbers
    numberStack = Stack()
    #split the postfix expression into individual characters
    characterList = userExpression.split()
    #iterate through characters
    for i in characterList:
        #numbers are pushed onto the stack
        if i.isdigit():
            numberStack.push(int(i))
        #a math function is performed with the numbers based on the operator given
        else:
            number1 = numberStack.pop()
            number2 = numberStack.pop()
            result = doMath(i, number2, number1)
            #result of the math is then pushed to the number stack, as this is sorta kinda recursive with values
            numberStack.push(result)
    return int(numberStack.pop())

#math function to actually perform math on the numbers
def doMath(operator, num1, num2):
    #cases for each of the possible math functions
    #exponential
    if operator == '^':
        return num1 ** num2
    #division
    elif operator == '/':
        return num1 / num2
    #multiplication
    elif operator == '*':
        return num1 * num2
    #addtion
    elif operator == '+':
        return num1 + num2
    #catch all for subtraction
    else:
        return num1 - num2

#main method
def main():
    #store user input as a variable
    infix = input("Enter an infix expression, separate each token with a space:")
    #use the infix to postfix function to convert the expression
    postfix = infixToPostfix(infix)

    #print the found postfix expression, as well as the actual math answer
    print("The postfix expression is:", postfix)
    print("Evaluate this postfix expression, the result is:", postfixEvaluation(postfix))

#calling main method
main()