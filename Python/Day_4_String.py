#1
string1= 'Thirty'
string2= 'Days'
string3= 'Of'
string4= 'Python'
string5= 'Coding'
print(string1 + ' ' + string2 + ' ' + string3 + ' ' + string4 + ' ' + string5)
#2
s1= 'Coding'
s2= 'For'
s3= 'All'
print(s1 + ' ' + s2 + ' ' + s3)
#3
company = 'Coding For All'
#4
print(company)
#5
print(len(company))
#6
print(company.upper())
#7
print(company.lower())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
print(company[0:6])
#10
print(company.index('Coding'))
print(company.find('Coding'))
#11
print(company.replace('Coding', 'Python'))
#12
string='Python for Everyone'
print(string.replace( 'Everyone','All'))
#13
print(company.split())
#14
string='Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(string.split(', '))
#15
print(company[0])
#16
print(len(company)-1)
#17
print(company[10])
#18
name='Python For Everyone'
words=name.split()
acronym= words[0][0]+words[1][0]+words[2][0]
print(acronym)
#19
phrase='Coding For All'
words=phrase.split()
acronym= words[0][0]+words[1][0]+words[2][0]
print(acronym)
#20
print(company.index('C'))
#21
print(company.index('F'))
#22
print(company.rindex('l'))
#23
sent='You cannot end a sentence with because because because is a conjunction'
print(sent.find('because'))
#24
print(sent.rfind('because'))
#25
word=sent.split()
print(word[6],word[7],word[8])
#alternative
print(sent[31:54])
#26
print(sent.index('because'))
#28
substring= 'Coding'
print(company.startswith(substring))
#29
substring= 'coding'
print(company.endswith(substring))
#30
print(company.strip())
#31
variable1='30DaysOfPython'
variable2='thirty_days_of_python'
print(variable1.isidentifier())
print(variable2.isidentifier())
#32
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_libraries))
#33
print('I am enjoying this challenge.\nI just wonder what is next.')
#34
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland \tHelsinki')
#35
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius", radius, "is", area, "meters square.")
#36
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')