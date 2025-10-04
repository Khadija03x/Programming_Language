#Day-6 : tuples
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

#level-1

#1
empty_tuple=()
print(empty_tuple)
#2
brothers=("rahul","rohit","raj")
sisters=("rita","reena","rani")
print(brothers)
print(sisters)
#3
siblings=brothers+sisters
print(siblings)
#4
print(len(siblings))
#5
siblings=list(siblings)
siblings.append("father")
siblings.append("mother")
family_members=tuple(siblings)
print(family_members)

#level-2

#1
sibling1, sibling2, sibling3, sibling4, sibling5, sibling6, father, mother = family_members
print(sibling1)
print(sibling2)
print(sibling3)
print(sibling4)
print(sibling5)
print(sibling6)
print(father)
print(mother)
#2
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('milk', 'meat', 'butter', 'yogurt')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
#3
food_stuff_tp = list(food_stuff_tp)
#4
if len(food_stuff_tp) % 2 == 0:
    middle1 = food_stuff_tp[len(food_stuff_tp)//2 - 1]
    middle2 = food_stuff_tp[len(food_stuff_tp)//2]
    print('Middle items:', middle1, 'and', middle2)
else:
    middle = food_stuff_tp[len(food_stuff_tp)//2]
    print('Middle item:', middle)
#5
print(food_stuff_tp[:3])
print(food_stuff_tp[-3:])
#6
del food_stuff_tp
#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
#end of the code