#Day -15
#1 Syntex Error
#print 'hello world'
#  File "<stdin>", line 1
#    print 'hello world'
#    ^^^^^^^^^^^^^^^^^^^
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
#2 NAmeError
#print(age)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#    import platform
#          ^^^
#NameError: name 'age' is not defined
#3 Index Error
#numbers = [1, 2, 3, 4, 5]
#>>> numbers[7]
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#    import platform
#    ^^^^^^^^^^
#IndexError: list index out of range
#4 Module Not Found Error
#import maths
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#    import platform
#    ^^^^^^^^^^^^
#ModuleNotFoundError: No module named 'maths'
#5 Attribute Error
#import math
#>>> math.PI
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#    import platform
#    ^^^^^^^
#AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
#6 Key Error
#users = {'name':'Asab', 'age':250, 'country':'Finland'}
#>>> users['name']
#'Asab'
#>>> users['county']
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#    import platform
#keyError: 'county'
#7 Type Error
#5+ '6'
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#    import platform
#    ^^^^^^
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#8 Import Error
#from math import power
##Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#    import platform
#ImportError: cannot import name 'power' from 'math' (unknown location)
#9 Value Error
#int('10b')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#    import platform
#    ^^^^^^^^^^
#ValueError: invalid literal for int() with base 10: '10b'
#10 Zero Division Error
#6/0
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#    import platform
#    ^^^
#ZeroDivisionError: division by zero
#end of file