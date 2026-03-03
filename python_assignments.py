# PYTHON ASSIGNMENT 1

#Section A

student_name = 'Obibi Oghenofegor Gregory' #variable containing full name (text type)
print(student_name)

age = 20                                   #variable containing age (numerical type)
print(age)

is_student = True                          #variable containing boolean value True (boolean type)
print(is_student)

#Section B

first_name = 'Fegor'
last_name = 'Obibi'
full_name = first_name + ' ' + last_name
print(f'My name is {full_name}')
print(full_name.upper())
print(full_name.lower())

#Section C

num1 = 25
num2 = 7
print(num1 + num2)       # Performs the addition of the two values
print(num1 - num2)       # Performs the subtraction of the two values
print(num1 * num2)       # Performs the multiplication of the two values
print(num1 / num2)       # Performs the division of the two values
print(num1 % num2)       # Performs the modulus of the two values (gives the remainder left after the division)

#Section D

variable_1 = str(333)
print(type(variable_1))

variable_2 = int(333.4)
print(type(variable_2))

variable_3 = float(333)
print(type(variable_3))

variable_4 = bool(1)
print(type(variable_4))

# A data type could be described as the classification of data that determines how data interacts with operations in python.

# Section E

number_as_string = "50"
A = int(number_as_string)
B = float(number_as_string)

print(A + 10)
print(B + 10)

# Casting is important in manipulating and specifying data types because it prevents errors or confusion in a program.

# Section F

x = 10
y = 20

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# A boolean value is one that is True if a condion is met and False if it isn't.

# Section G

Name = input('Enter your name:')
Year_of_birth = int(input('Enter your year of birth:'))

Age = 2025 - Year_of_birth

print(f'Name: {Name}')
print(f'Age: {Age}')

if Age >= 18:
    print('Adult: True')
else:
    print('Adult: False')
    

# SIMULTANEOUS EQUATION CALCULATOR

# The formula used for both equation formats is cramer's rule.

# Defining the functions(formulas) used in the calculator for 2 x 2 equations.

def Det1():
    return (a1 * b2) - (a2 * b1)

def Det1_x():
    return (c1 * b2) - (c2 * b1)

def Det1_y():
    return (a1 * c2) - (a2 * c1)

def X1():
    return Det1_x() / Det1()

def Y1():
     return Det1_y() / Det1()

# Defining the functions(formulas) used in the calculator for 3 x 3 equations.

def Det2():
    return a1 * ((b2 * c3) - (b3 * c2)) - b1 * ((a2 * c3) - (a3 * c2)) + c1 * ((a2 * b3) - (a3 * b2))

def Det2_x():
    return d1 * ((b2 * c3) - (b3 * c2)) - b1 * ((d2 * c3) - (d3 * c2)) + c1 * ((d2 * b3) - (d3 * b2))

def Det2_y():
    return a1 * ((d2 * c3) - (d3 * c2)) - d1 * ((a2 * c3) - (a3 * c2)) + c1 * ((a2 * d3) - (a3 * d2))

def Det2_z():
    return a1 * ((b2 * d3) - (b3 * d2)) - b1 * ((a2 * d3) - (a3 * d2)) + d1 * ((a2 * b3) - (a3 * b2))

def X2():
    return Det2_x() / Det2()

def Y2():
    return Det2_y() / Det2()

def Z2():
    return Det2_z() / Det2()

# Below is what the user will see and the required input for the calculator to work.

print('simultaneous equation calculator!')
print('1. Ax + By = C')
print('2. Ax + By + Cz = D')

option = input('select equation format (1 or 2):')

if option == '1':
    print('first equation:')
    a1 = float(input('input first coefficient (A): '))
    b1 = float(input('input second coefficient (B): '))
    c1 = float(input('input constant(C): '))
    print('second equation: ')
    a2 = float(input('input first coefficient (A): '))
    b2 = float(input('input second coefficient (B): '))
    c2 = float(input('input constant(C): '))
    if Det1() == 0:
        print('It has no unique solution (The matrix is singular)')
    else:
        print(f'The values are: X = {X1()} and Y = {Y1()}')
    

elif option == '2':
    print('first equation: ')
    a1 = float(input('input first coefficient (A): '))
    b1 = float(input('input second coefficient (B): '))
    c1 = float(input('input third coefficient(C): '))
    d1 = float(input('input constant(D): '))
    print('second equation: ')
    a2 = float(input('input first coefficient (A): '))
    b2 = float(input('input second coefficient (B): '))
    c2 = float(input('input third coefficient(C): '))
    d2 = float(input('input constant(D): '))
    print('third equation: ')
    a3 = float(input('input first coefficient (A): '))
    b3 = float(input('input second coefficient (B): '))
    c3 = float(input('input third coefficient(C): '))
    d3 = float(input('input constant(D): '))
    if Det2() == 0:
        print('It has no unique solution (The matrix is singular)')
    else:
        print(f'The values are: X = {X2()}, Y = {Y2()} and Z = {Z2()}')
    

else:
    print('option not listed')


# PYTHON ASSIGNMENT 2

# SETS

#Q1

print('Hello user')
print("Enter the number you want to store and type 'exit' to stop")
Set = set()
while True:
    values = input('Enter a number: ')
    
    if values.lower() == 'exit':
        break
    if not values:
        print("Please type a number")
        continue
    try:
        number = float(values)
        Set.add(number)
    except ValueError:
        print("You did not enter a number")

print(f'This is your set of numbers: {Set}')

#Q2

ID_1 = {'ID100', 'ID121', 'ID232', 'ID300', 'ID424'}
ID_2 = {'ID100', 'ID125', 'ID246', 'ID300', 'ID569'}
A = ID_1.intersection(ID_2)
print(A)
B = ID_1.difference(ID_2)
print(B)

#DICTIONARIES

#Q3

print('Hello user')
print("Enter the student's profile")
Dic = {'GREG' : {'Course' : 'MECHANICAL', 'Age' : 20}, 'ENIOLA': {'Course' : 'MEDICINE', 'Age' : 20}, 'DAVID' : {'Course': 'COMPUTER SCIENCE', 'Age' : 21}}
def Dic_update(N, A, C):
  Dic.update({N : {'Age' : A, 'Course' : C}})
while True:
    P = input('Enter profile?, Y/N: ')
    
    if P.upper() == 'Y':
       N = input("Enter student's name:")
       
       try:
         A = int(input("Enter student's age:"))

       except ValueError:
         print('Wrong input')
         break
       
       C = input("Enter student's course:")
       Dic_update(N, A, C)
    
    elif P.upper() == 'N':
     break

    else:
      print('Wrong input')

print('Preparing profile(s)...')    
print(Dic)

#Q4

print('hello user')
a = input('type a sentence:').lower().split()
dict = {}

for x in a:
   if x in dict:
      dict[x] += 1
   else:
      dict[x] = 1
   
print(dict)

# IF...ELSE

#Q5

print('Enter your score')
A = float(input('Input score:'))

if A >= 70:
    print('Excellent')
elif A >= 50:
    print('Good')
elif A >= 40:
    print('pass')
else:
    print('Fail')

#Q6

DIC = {'OBIBI' : 'STUDENT', 'DARA': 'DATA ANALYST', 'MR BEAST': 'YOUTUBER', 'WISDOMKAYE':'TIKTOKER', 'RONALDO' : 'FOOTBALLER'}

A = input('Enter name to check your profile: ').upper()

if A in DIC.keys():
    print(f"Your profile is [{A} : {DIC[A]}]")
else:
    print('Profile does not exist')

# WHILE LOOP

#Q7

Password = 'GAME1234'
attempts = 0
while attempts < 3:
    A = input('Enter password: ')

    if A == Password:
        print('Correct password')
        print('Proceed')
        break
    elif A != Password:
        print('incorrect password')
        attempts += 1
        if attempts == 3:
            print('You have reached the maximum number of attempts')
        continue

#Q8

Item_list = ['orange', 'apple', 'banana', 'mango', 'guava', 'pear', 'pawpaw']

print('Hello user')
print('What do you want to do with your item list?')
print('1. Add items')
print('2. View items')
print('3. Exit')

while True:
    option = input('Select option to perform (1/2/3):')

    if option == '3':
        print('Closing menu')
        break
    
    elif option == '1':
        ITEM = input('Enter the item to add:')
        Item_list.append(ITEM)
        print('item has been added')
    
    elif option == '2':
        print(f'This is your list of items: {Item_list}')
    
    else:
        print('Wrong input')

# FOR LOOP

#Q9

Nolist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
for i in Nolist:
    total += i

print(f'the total is {total}')
average = total / len(Nolist)
print(f'the average is {average}')

#Q10

DIC = {'OBIBI' : 'STUDENT', 'DARA': 'DATA ANALYST', 'MR BEAST': 'YOUTUBER', 'WISDOMKAYE':'TIKTOKER', 'RONALDO' : 'FOOTBALLER'}
for i in DIC.items():
    print(i)

# FUNCTIONS

#Q11

def calculate_average(n):
    return sum(n)/len(n)

Nolist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(calculate_average(Nolist))

#Q12

def dict(n):
    for i in n.values():
        if i > 60:
            print(i)

DIC = {'josh' : 20, 'gabe' : 45, 'cole' : 65, 'anna' : 70, 'michael': 80, 'kevin' : 30}

dict(DIC)

# LAMBDA FUNCTIONS

#Q13

A = float(input('Enter number: '))
x = lambda A : A ** 2
print(x(A))

#Q14

A = [('greg', 34), ('shalom', 23), ('mark', 45), ('josh', 40)]
A.sort(key = lambda n : n[1])
print(A)

# TRY...EXCEPT (EXCEPTION HANDLING)

#Q15

A = input('Enter first number:')
B = input('Enter second number: ')

try:
    a = float(A)
    b = float(B)
    C = a / b
    print(f'{a} / {b} is equal to {C}')

except ZeroDivisionError:
    print('Cannot divide by zero')

except ValueError:
    print('One or both inputs was not a number')

#Q16

A = input('Enter a number:')

try:
    int(A)
    print(f'the number you typed is {A}')

except ValueError:
    print('You did not enter a number')

# FILE HANDLING

#Q17

F = open('student.txt', 'w')
F.write('greg, mark, shalom, david, dara, tayo')
F.close()
F = open('student.txt', 'r')
F.read()

#Q18

f = open('student.txt','r')
for i in f:
    print(len(i))
f.close()
f = open('student.txt', 'r')
A = f.read()
B = A.split()
print(len(B))

# COMBINED/PRACTICAL QUESTIONS

#Q19

print('Hello user')
DIC = {'ID1023' : 53, 'ID3302' : 45, 'ID2231' : 68, 'ID4453' : 72}
def Dic_update(ID, S):
    DIC.update({ID : S})

def Dic_display():
    print(DIC)

print('1. Add student ID and score')
print('2. Display student ID and score')
print('3. Exit app')

while True:
    A = input('Select action to perform:')
    
    if A == '3':
        print('closing app')
        break
    
    elif A == '1':
        ID = input('Enter student ID:')
        try:
            S = int(input('Enter student score'))
        except ValueError:
            print('input is not a number')
            continue
        Dic_update(ID, S)
        print('Student ID and score has been added')
    
    elif A == '2':
        Dic_display()
    
    else:
        print('invalid input')
        continue

#Q20

import re

print('Student Record Management System')
file = open('student records.txt', 'r')
file.close()
DICT = {}
nlist = []

print('1. Display class average')
print('2. Add student record')
print('3. Display student records')
print('4. Exit')

while True:
    option = input('Enter option to perform (1/2/3/4):')

    if option == '4':
        
        print('closing app')
        break
    
    elif option =='3':
        
        print('Displaying student records...')
        file = open('student records.txt', 'r')
        print(file.read())
        file.close()
        continue

    elif option == '2':
        
        name = input('Enter student name:')
        score = input('Enter student score:')

        try:
            newscore = int(score)
            DICT.update({name : newscore})
            file = open('student records.txt', 'a')
            file.write(f'{DICT}')
            file.close
            continue

        except ValueError:
            print('Please enter a number')
            continue
    
    elif option == '1':
    
        file = open('student records.txt', 'r')
        record = file.read()
        file.close()

        pattern = r'\d\d+'
        value = re.findall(pattern, record)
        
        try:
            for i in value:
                num = int(i)
                nlist.append(num)
                average = lambda x: sum(nlist) / len(nlist)
        
            print(f'The class average is {average(value)}')
            continue
        
        except ZeroDivisionError:
            
            print('There are no student records')
            continue
        
        except NameError:

            print('There are no student records')
            continue
            
    else:
        print('Wrong input')
        continue
