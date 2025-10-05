#Day -7 :Sets
# A set is a collection which is unordered and unindexed. In Python sets are written with

#level-1
#1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
#2
it_companies.add('Twitter')
print(it_companies)
#3
it_companies.update(['Meta', 'Netflix', 'Adobe'])
print(it_companies)
#4
it_companies.remove('Apple')
print(it_companies)
#5
it_companies.discard('Apple')
#it_companies.remove('Apple') # it gives an error as 'Apple' is already removed
print(it_companies)

#level-2
#1
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))
#2
print(A.intersection(B))
#3
print(A.issubset(B))
#4
print(A.isdisjoint(B))
#5
print(A.union(B))
print(B.union(A))
#6
print(A.symmetric_difference(B))
#7
del A
del B

#level-3
#1
age = [22, 19, 24, 25, 26, 24, 24]
age_set = set(age)
if len(age) > len(age_set):
    print('The list is bigger than the set, so there are duplicates in the age list')
else:
    print('Both are equal')
#2
string = 'I am a teacher and I love to inspire and teach people'
list_string = string.split()
tuple_string = tuple(list_string)
set_string = set(list_string)
print('String : ',string)
print('List : ',list_string)
print('Tuple : ' ,tuple_string)
print('Set : ', set_string)
#3
string1 = 'I am a teacher and I love to inspire and teach people I teach people'
list_string1 = string1.split()
set_string1 = set(list_string1)
print('The number of unique words : ',len(set_string1))
print('The unique words are :' ,set_string1)

#end of the code