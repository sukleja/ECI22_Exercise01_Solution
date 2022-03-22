'''Exercise01 Solution
This is one possible way to solve it but there are more ways how you can solve
the exercise'''


#1
def name_age():
    name = input("Enter name: ")
    age = input("Enter age: ")
    result = name + age
    print("Hello " + name + " Your age is: " + age)

    return result

#2
def swap_integers(num1, num2):

    print("x: " + str(num1))
    print("y: " + str(num2))

    temp = num1
    num1 = num2
    num2 = temp

    print("After swap:")
    print("x: " + str(num1))
    print("y: " + str(num2))

    return str(num1) + str(num2)

#3
def check_numbers(num1, num2):
    if num1 % 6 == 0 or num2 % 6 == 0:
        if num1 % 10 == 0 and num2 % 10 == 0:
            return True
        else:
            return False
    else:
        return False

#4
def sum_up(num1 , num2 ):
    sum = int(0) #not necessary to cast as an int, but will make sure that we always return an int
    if num2 < num1:
        return sum
    if num1 > 0 and num2 > 0:
        end = (num2 - num1) + 1
        for i in range(end): # iterating from first number to last number
            sum += num1 + i
    return sum

#5
def circle_area(r1, r2, r3):
    PI = 3.142
    area1 = PI * r1**2
    area2 = PI * r2**2
    area3 = PI * r3**2

    result = round(area1 + area2 + area3, 3)
    return result

#6
def check_string(text):
    if text.lower().startswith("a") or text.lower().endswith("a"):
        return True
    else:
        return False

#7
def triangle(rows):
    for i in range(rows): #iterating over rows
        for j in range(i+1): #iteraring over columns
            print("*", end=" ")
        print("") #newline to jump into next row

