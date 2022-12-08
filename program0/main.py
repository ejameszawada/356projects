# Course: CSCI 356, Section 1
# Student Name: Ethan Zawada
# Student ID: 10627257
# Program 0
# Due Date: 1/28/2022

# In keeping with the Honor Code of UM, I have neither given nor received any
# inappropriate assistance from anyone other than the TA or the instructor

# initialize dictionaries
rooms = {'CS101':3004, 'CS102':4501, 'CS103':6755, 'NT110':1244, 'CM241':1411}
instructors = {'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}
times = {'CS101':'8am', 'CS102':'9am', 'CS103':'10am', 'NT110':'11am', 'CM241':'1pm'}

# ask for input course
course = input('Enter a course number: ')

# display info
if course in rooms:
    print('The details of the course: ')
    print('\tRoom number: ', rooms[course])
    print('\tRoom number: ', instructors[course])
    print('\tRoom number: ', times[course])
else:
    print('Invalid course entered.')


