
# variable_logic_puzzles.py

# Puzzle 1: Swap two values
# You have two variables:
a = "pen"
b = "book"
# Swap the values of a and b without typing "pen" or "book" again.
# Use only variables to do it.
swap = a
a = b
b = swap
print("a:",a)
print("b:",b)
# Puzzle 2: Create full name
# You have:
first_name = "Hafiz"
last_name = "Usman"
# Combine them into one variable full_name and print it with a space in between.
full_name = first_name + " " + last_name
print("Full name:",full_name)
# Puzzle 3: Chain swapping
# Given three variables:
box1 = "dates"
box2 = "apples"
box3 = "bananas"
# Make box1 = bananas, box2 = dates, box3 = apples using only variables.
change = box1
box1 = box3
box3 = box2
box2 = change
print("box1:",box1)
print("box2:",box2)
print("box3:",box3)
# Puzzle 4: Secret code
# You have:
word1 = "peace"
word2 = "love"
# Combine them in reverse order (love + peace) and print the result.
print(word2 + " " + word1)
# Puzzle 5: Repeat and combine
# You have:
item = "Quran"
# Make a new variable that repeats this word 3 times with spaces in between, like:
# Quran Quran Quran
repeated_item = item + " " + item + " " + item
print("You have:",repeated_item)