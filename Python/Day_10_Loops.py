#day-10 
#Loops

#1
num = list(range(11))
print("For loop : ")
for i in num:
    print(i , end=" ")  
print("\nWhile loop : ")
i=0
while i < 11:
    print(num[i], end=" ")
    i+=1  
#2
print("\n")


#3
for i in range(8):
    for j in range(0,i):
        print("#", end="")
    print()
print()
#4
for i in range(9):
    for j in range(9):
        print("#",end=" ")
    print()
print()
#5
for i in range (11):
    print(f"{i} x {i} = {i*i}")
print()
#6
languages = ['Python', 'Numpy','Pandas','Django', 'Flask']
for lang in languages:
    print(lang, end=" ")
print()
#7
print ("Even numbers : ")
for i in range(101):
    if i % 2 == 0:
        print(i, end=" ")
print()
#8
print("Odd numbers : ")
for i in range(101):
    if i % 2 != 0:
        print(i, end=" ")
print()

#level 2
#1
sum = 0

for i in range(101):
    sum += i
print("The sum of all numbers from 0 to 100 : " , sum)
print()
#2
print()
sum_even=0
sum_odd=0
for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print("The sum of all even numbers from 0 to 100 : ", sum_even)
print("The sum of all odd numbers from 0 to 100 : ", sum_odd)
#level 3
#1
from data.countries import countries
land_count = []
for country in countries:
    if 'land' in country.lower():
        land_count.append(country)
print("Countries containing 'land': ", land_count)
print()
#2
fruits = ['banana', 'orange', 'mango', 'lemon']
for fruit in reversed(fruits):
    print(fruit, end=" ")
print()


#end of code 








