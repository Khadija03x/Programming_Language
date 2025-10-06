#Day-8 :dictinary
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are

#level-1
#1
empty_dict = {}
print(empty_dict)
print(type(empty_dict))
#2
dog={
    'name':'Buddy',
    'color':'Brown',
    'breed':'LGoldren Retriever',
    'legs':4,
    'age':3
}
print(dog)
#3
student={
    'first_name':'John',
    'last_name':'Doe',
    'gender':'Male',
    'age':21,
    'marital_status':'Single',
    'skills':['Python','Java','C++'],
    'country':'USA',
    'city':'New York',
    'address':{
        'street':'123 Main St',
        'zipcode':'10001'
    }
}
print(student)
#4
print(len(student))
#5
print(student['skills'])
print(type(student['skills']))
#6
student['skills'].append('JavaScript')
student['skills'].append('HTML')
print(student['skills'])
student['skills'][2]='React'
print(student['skills'])
#7
student_keys = student.keys()
print(student_keys)
#8
student_values = student.values()
print(student_values)
#9
student_items = student.items()
print(student_items)
#10
student.pop('marital_status')
print(student)
#11
del student

#end of the code