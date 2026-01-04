# Example of string concatenation in Python
str1='Hello Python'
str2='Learing is fun'
result=str1 + ' ' + str2
print(result)

# Exercise 1: Concatenate three strings
first='John'
middle='David'
last='Smith'
Date_of_birth='04/09/1993'
full_name=first + ' ' + middle + ' ' + last
message=f'{full_name} and my DOB: {Date_of_birth}'
print(message)

# Exercise 2: Using f-strings
name='Alice'
age=25
gender='Female Employee'
message=f'{name} is {age} years old and {gender}'
print(message)

# Exercise 3: Concatenate with multiplication
symbol= []'&'
symbol1='*'
border=symbol * 100
border2=symbol1 * 100
title='Welcome to Python'
title_2='Lets start coding in python'
print(border)
print(title)
print(border)
print(title_2)
print(border2)


# Exercise 4: String concatenation in a loop
colors=['Red', 'Green', 'Blue']
result=''
for color in colors:
    result=result + color + ', '
print(result)

# Exercise 5: Using join() method
fruits=['Apple', 'Banana', 'Orange', 'Mango']
fruit_list=' | '.join(fruits)
print(fruit_list)

# Exercise 6: Concatenate numbers as strings
num1='123'
num2='456'
concatenated=num1 + num2
print(concatenated)

# Exercise 7: Mixed concatenation with .format()
product='Laptop'
price=1200
info='{} costs ${}'.format(product, price)
print(info)