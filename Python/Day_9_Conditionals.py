#Day - 9 : Conditionals
#If, elif and else statements

#level 1
#1
age= int(input("Enter your age: "))
if age>=18:
    print("You are old enough to drive")
else:
    print("You need {} more years to learn to drive".format(18-age))
#2
my_age= 25
your_age= int(input("Enter your age: "))
if my_age>your_age:
    if my_age-your_age==1:
        print("I am 1 year older than you")
    else:
        print("I am ",my_age-your_age," years older than you")
elif my_age<your_age:  
    if your_age-my_age==1:
        print("You are 1 year older than me")
    else:
        print("You are {} years older than me".format(your_age-my_age))
else:
    print("We are of the same age")
#3
a = int (input("Enter the first number ,a :"))
b= int(input("Enter the second number , b : "))
if a>b:
    print("a is greater than b")
elif a<b:
    print("b is greater than a")
else:
    print("a is equal to b")

#level 2
#1
score = int(input("Enter your score : "))
if score>=80 and score<=100:
    print("A")
elif score>=70 and score<80:
    print("B")
elif score>=60 and score<70:
    print("C")
elif score>=50 and score<60:
    print("D")
elif score>=0 and score<50:
    print("F")
else:
    print("Invalid score")
#2
month = str(input("Enter the month : "))
if month in ('September','October','November'):
    print("The season is Autumn")
elif month in ('December','January','February'):
    print("The season is Winter")
elif month in ('March','April','May'):
    print("The season is Spring")
elif month in ('June','July','August'):
    print("The season is Summer")
else:
    print("Invalid month")
#3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = str(input("Enter a fruit : "))
if fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit)
    print(fruits)

#level 3
#*
person ={ 'first_name': 'Asabeneh',
            'last_name': 'Yetayeh',
            'age': 250,
            'country': 'Finland',
            'is_married': True,
            'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
            'address': {
                'street': 'Space street',
                'zipcode': '02210'
            }
}
if 'skills' in person:
    print("The middle skill is: ",person['skills'][len(person['skills'])//2])
else:
    print("The person has no skills")
#*
if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person is a Python developer")
    else:
        print("The person is not a Python developer")
else:
    print("The person has no skills")
#*
if 'React' and 'Node' and 'MongoDB' in person['skills']:
    print("The person is a fullstack developer")
elif 'JavaScript' and 'React' in person['skills']:
    print("The person is a front end developer")
elif 'Node' and 'MongoDB' and 'Python' in person['skills']:
    print("The person is a backend developer")
else:
    print("Unknown title")
#*
if person['is_married'] and person['country']=='Finland':
    print("{} {} lives in {}. He is married.".format(person['first_name'],person['last_name'],person['country']))
    #print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
else:
    print("{} {} lives in {}. He is not married.".format(person['first_name'],person['last_name'],person['country']))
    #print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is not married.")

#end of code