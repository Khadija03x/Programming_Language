x=3
y=2
a = x + y
print("Addition : " , x,'+', y , " = ", a)   # addition(+)
print("Subtraction : " , x,'-', y , " = ", x - y)   # subtraction(-)
print("Multiplication : " , x,'*', y , " = ", x * y)   # multiplication(*)
print("Division : " , x,'/', y , " = ", x / y)   # division(/)
print("Exponential : " , x,'**', y , " = ", x ** y)  # exponential(**)
print("Modulus : " , x,'%', y , " = ", x % y)   # modulus(%)
print("Floor Division : " , x,'//', y , " = ", x // y)  # Floor division operator(//)
My_info = {
'first_name':'khadijatul',
'last_name':'kubra',
'country':'Bangladesh'
}
print()
print("First name : ", My_info['first_name'])          # String
print("Last name : ", My_info['last_name'])            # String
print("Country : ", My_info['country'])                # String
print("I am enjoying 30 days of python") 

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type(['Asabeneh', 'Python', 'Finland']
))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({'country':'Bangladesh'})) # Dictionary



print("\n\n\n")
point_1 = (2, 3) # tuple
point_2 = (10, 8) # tuple
print("Point 1 : ", point_1)
print("Point 2 : ", point_2)
distance = ((point_2[0] - point_1[0])**2 + (point_2[1] - point_1[1])**2)**0.5
print("Distance between point 1 and point 2 : ", distance)
