#1
age = 250
#2
height = 150.00
#3
complex_num = 1 + 2j
#4 
height = float(input("Enter the height of the triangle: "))
base = float(input("Enter the base of the triangle: "))
area_of_triangle = 0.5 * height * base
print("The area of the triangle is ", area_of_triangle)
#5
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter_of_triangle = side_a + side_b + side_c
print("The perimeter of the triangle is ", perimeter_of_triangle)
#6
length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print("The area of the rectangle is ", area_of_rectangle)
print("The perimeter of the rectangle is ", perimeter_of_rectangle)
#7
radius = float(input("Enter radius: "))
pi = 3.14
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius
print("The area of the circle is ", area_of_circle)
print("The circumference of the circle is ", circum_of_circle)
# 8. Slope, x-intercept and y-intercept of y = 2x -2
#slope intercept form y = mx + b
m1 = 2
b = -2
print("The slope is ", m1)
print("The y-intercept is (",0,",",b,")")
# x-intercept is when y = 0
y=0
x = (y - b) / m1
print("The x-intercept is (",x,",",y,")")
# 9. Slope between two points (2, 2) and (6, 10)  
x1, y1 = 2, 2
x2, y2 = 6, 10
m2 = (y2 - y1) / (x2 - x1)
print("The slope of the line is ", m2)
# 10. Compare the slopes m1 and m2
print("Are the slopes equal? ", m1 == m2)

# 11. Calculate the value of y (y = x^2 + 6x + 9) for x values 0 to 5
for x in range(0,5):
    y = x**2 + 6*x + 9
    print("For x =",x, ", y =",y)
# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement
print(len('python'))
print(len('dragon'))
print(len('python') != len('dragon'))
# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')
# 14. I hope this course is not full of jargon. Use in operator to check
print('jargon' in 'I hope this course is not full of jargon')
# 15. There is no 'on' in both dragon and python
print('on' not in 'dragon' and 'on' not in 'python')
# 16. Find the length of the text python and convert the value to float and then to string
length = len('python')
print("The length of python ",float(length))
print("The length of python in string " ,str(float(length)))
# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check this in Python?
for i in range(0,11):
    if i % 2 == 0:
        print(i, " is an even number")
    else:
        print(i, " is an odd number")
# 18. Check if the floor division of 7 by 3 is equal to the
floor_div = 7 // 3
print("The floor division of 7 by 3 is ", floor_div)
int_conversion = int(2.7)
print("The integer conversion of 2.7 is ", int_conversion)
if floor_div == int_conversion:
    print("The floor division of 7 by 3 is equal to the integer conversion of 2.7")
else:
    print("The floor division of 7 by 3 is not equal to the integer conversion of 2.7")
# 19. Check if type of '10' is equal to type of 10
print(type('10') == type(10))
# 20. Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10)
# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print("Your weekly earning is : ", pay)
# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
num_of_years = int(input("Enter number of years you live: "))
seconds = num_of_years * 365 * 24 * 60 * 60
print("You live ", seconds, " seconds.")
# 23. Write a Python script that displays the following table
for n in range(1,6): #from 1 to 5
    print(n," " ,n**0 ," ",n**1," ",n**2," ", n**3)
    #end()
