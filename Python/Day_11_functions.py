#Day-11:functions
#level 1
#1
def add_two_numbers(a,b):
    sum=a+b
    return sum
print(add_two_numbers(3,5))
#2
def area_of_circle(r):
    pi=3.14
    area = pi*r*r
    return area
print(area_of_circle(5))
#3
def sum_of_all_numbers(*num):
    sum=0
    for i in num:
        if type(i)==int or type(i)==float:
            sum+=i
        elif type(i)!=int or typr(i)!=float:
            print(f'{i} is not a number')
    return sum
print(sum_of_all_numbers(1,2,3,'a',4,5))
#3
def convert_celsius_to_farenheit(c):
    f=(c*(9/5))+32
    print(f'{c} degree celsius is equal to {f} degree farenheit')
convert_celsius_to_farenheit(37)
#5
def check_season(month):
    if month in ('September','October','November'):
        print('The season is Autumn')
    elif month in ('December','January','February'):
        print('The season is Winter')
    elif month in ('March','April','May'):
        print('The season is Spring')
    elif month in ('June','July','August'):
        print('The season is Summer')
    else:
        print('Invalid month')
check_season('March')
#6
def calculate_slope(x,y,c):
    slope=(y-c)/x
    return slope
print(f'Solpe = {calculate_slope(2,4,1)}')
#7
def solve_quadratic_eqn(a,b,c):
    d=(b**2)-(4*a*c)
    if d>0:
        root1=(-b+(d**0.5))/(2*a)
        root2=(-b-(d**0.5))/(2*a)
        return root1,root2
    elif d==0:
        root=-b/(2*a)
        return root
    else:
        return 'No real roots'
print(solve_quadratic_eqn(1,-3,2))
#8
def print_list(lst):
    for item in lst:
        print(item, end=",")
print_list(['Python', 'Numpy','Pandas','Django', 'Flask'])
print()
#9
def reverse_list(lst):
    reversed_lst=[]
    for i in reversed(lst):
        reversed_lst.append(i)
    return reversed_lst
print(reverse_list([1,2,3,4,5]))
#10
def capitalize_list_items(lst):
    capitalized_lst=[]
    for item in lst:
        capitalized_lst.append(item.upper())
    return capitalized_lst
print(capitalize_list_items(['python', 'numpy','pandas','django', 'flask']))
print()
#11
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
def add_item_to_list(lst,item):
    lst.append(item)
    return lst
print(add_item_to_list(food_staff, 'Meat'))
print(add_item_to_list([1,2,3,4],5))
print()
#12
def remove_item_from_list(lst,item):
    if item in lst:
        lst.remove(item)
    return lst
print(remove_item_from_list(food_staff, 'Mango'))
print(remove_item_from_list([1,2,3,4,5],3))
print()
#13
def sum_of_numbers(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))
#14
def sum_of_odds(n):
    sum=0
    for i in range(n+1):
        if i%2!=0:
            sum+=i
    return sum
print(sum_of_odds(5))
print(sum_of_odds(10))
print(sum_of_odds(100))
#15
def sum_of_evens(n):
    sum=0
    for i in range(n+1):
        if i%2==0:
            sum+=i
    return sum
print(sum_of_evens(5))
print(sum_of_evens(10))
print(sum_of_evens(100))
#level 2
#1
def evens_and_odds(n):
    even_count=0
    odd_count=0
    for i in range(n+1):
        if i%2==0:
            even_count+=1
        else:
            odd_count+=1
    return even_count, odd_count
even_count, odd_count = evens_and_odds(100)
print(f'The number of evens are {even_count}')
print(f'The number of odds are {odd_count}')
#2
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
print(factorial(10))
#3
def is_empty(param):
    if param:
        return False
    else:
        return True
print(is_empty([]))
print(is_empty([1,2,3]))
print(is_empty(''))
print(is_empty('Hello'))
#4
def calculate_mean(lst):
    if len(lst)==0:
        return 0
    return sum(lst)/len(lst)
print(calculate_mean([1,2,3,4,5]))
print(calculate_mean([]))
print
def calculate_median(lst):
    n=len(lst)
    if n==0:
        return 0
    sorted_lst=sorted(lst)
    mid=n//2
    if n%2==0:
        median=(sorted_lst[mid-1]+sorted_lst[mid])/2
    else:
        median=sorted_lst[mid]
    return median
print(calculate_median([1,3,3,6,7,8,9]))
print(calculate_median([1,2,3,4,5,6,8,9]))
print(calculate_median([]))
print()
def calculate_mode(lst):
    if len(lst)==0:
        return None
    frequency={}
    for item in lst:
        if item in frequency:
            frequency[item]+=1
        else:
            frequency[item]=1
    max_count=max(frequency.values())
    modes=[key for key, value in frequency.items() if value==max_count]
    return modes
print(calculate_mode([1,2,2,3,4,4,4,5]))
print(calculate_mode(['a','b','b','c','c','c','d']))
print(calculate_mode([]))
print()
def calculate_range(lst):
    if len(lst)==0:
        return 0
    return max(lst)-min(lst)
print(calculate_range([1,2,3,4,5]))
print(calculate_range([10,20,30,40,50]))
print(calculate_range([]))
print()
def calculate_variance(lst):
    if len(lst)==0:
        return 0
    mean=calculate_mean(lst)
    variance=sum((x-mean)**2 for x in lst)/len(lst)
    return variance
print(calculate_variance([1,2,3,4,5]))
print(calculate_variance([10,20,30,40,50]))
print(calculate_variance([]))
print()
def calculate_std_deviation(lst):
    variance=calculate_variance(lst)
    std_deviation=variance**0.5
    return std_deviation
print(calculate_std_deviation([1,2,3,4,5]))
print(calculate_std_deviation([10,20,30,40,50]))
print(calculate_std_deviation([]))
print()
def calculate_frequency_distribution(lst):
    frequency={}
    for item in lst:
        if item in frequency:
            frequency[item]+=1
        else:
            frequency[item]=1
    return frequency
print(calculate_frequency_distribution([1,2,2,3,3,3,4,4,4,4]))
print(calculate_frequency_distribution(['a','b','b','c','c','c','d','d','d','d']))
print()
#level 3
#1
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(is_prime(11))
print(is_prime(15))
print(is_prime(1))
print(is_prime(2))
print()
#2
def unique_items(lst):
   return len(lst)==len(set(lst))
print(unique_items([1,2,2,3,4,4,5]))
print(unique_items(['a','b','b','c','d','d','e']))
print()
#3
def check_data_type_in_list(lst,data_type):
    for item in lst:
        if not isinstance(item, data_type):
            return False
    return True
print(check_data_type_in_list([1,2,3,4,5], int))
print(check_data_type_in_list(['a','b','c','d'], str))
print(check_data_type_in_list([1,'b',3,'d'], int))
print()
#4
def validate_python_variable(var_name):
    import keyword
    if not var_name.isidentifier() or keyword.iskeyword(var_name):
        return False
    return True
print(validate_python_variable('my_var'))
print(validate_python_variable('2nd_var'))
print(validate_python_variable('for'))
print()
#5
import data.countries_data as cd
def most_spoken_languages(n=10):
   # """Return n most spoken languages in descending order"""
    count = {}
    for country in cd.countries_data:
        for lang in country['languages']:
            count[lang] = count.get(lang, 0) + 1

#Sort by count (descending) and take first n
    sorted_langs = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return sorted_langs[:n]

#Test it
top_10 = most_spoken_languages(10)
for lang, num in top_10:
    print(f"{lang}: {num} countries")
