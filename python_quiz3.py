#1.Add Two Numbers
#Write a program that takes two numbers from the user and prints their sum.
#🧩 Hint: Use input(), convert to int, then add.
from math import radians


first_no = input("please enter first number: ")
second_no = input("please enter second number: ")
print(int(first_no) + int(second_no))
#2.Find the Type of a Variable
#Create a variable with your name and print the data type of that variable using type().
my_name = "Hassaan Mahmood "
print(type(my_name))
#3.Convert Float to Integer
#Take a float number (e.g., 5.9) and convert it to an integer using casting.
number = 5.9
print(int(number))
#4.Area of a Circle
#Write a function area_of_circle(radius) that returns the area of a circle using the formula:
#Area = π * r^2
#(Use 3.14 for π)
def area_of_circle(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    return area
print(area_of_circle(17))
#5.Even or Odd
#Write a function check_even_odd(num) that prints whether the number is even or odd.
def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
check_even_odd(100)
check_even_odd(15)           
#6.Welcome Message
#Ask the user for their name and print:
#Welcome, <name>! Have a great day!
name = input("Please enter your name: ")
print("Welcom, " + name + "! Have a great day! ")
#7.String Slicing
#Given a string text = "Python Programming", print:
#The first 6 characters
#The last 6 characters
#The word “Programming” using slicing
text = "Python Programming"
print(text[:6])
print(text[-6:])
print(text[7:])
#8.Modify String Case
#Take user input and:
#Print it in uppercase
#Print it in lowercase
user_name = input("Please enter your name: ")
print(user_name.upper())
print(user_name.lower())
#9.Count Characters
#Write a function count_characters(s) that returns how many characters (letters only) are in the string (ignore spaces).
def count_characters(s):
    count = 0
    for char in s:
        if char.isalpha():
            count += 1
    return count
print(count_characters("Hassaan Mahmood Ahmad "))
print(count_characters("Mufti Mahmood Ahmad "))
#10.Format Output
#Write a program that uses .format() to display:
#My name is Bilal and I am 25 years old.
#(using variables name = "Bilal", age = 25)
name = "Bilal"
age = 25
print("My name is {n} and I am {a} years old.".format(n= name,a =age))