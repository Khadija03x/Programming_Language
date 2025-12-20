#1
numbers =[-4, -3, -2, -1, 0, 2,4,6]
negative_and_zero =[i for i in numbers if i<=0]
print(negative_and_zero)
#2
list_of_lists =[[[1,2,3]], [[4,5,6]], [[7,8,9]]]
flattened = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print(flattened)
#3
list_of_tuples = [(i , i**0 , i**1 , i**2 , i**3 , i**4 , i**5) for i in range(11)]
print(list_of_tuples)
#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output:
#[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
flat_countries = [[country.upper(), country.upper()[:3], city.upper()] for country_list in countries for (country, city) in country_list]
print(flat_countries)
#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output:
#[{'country': 'FINLAND', 'city': 'HELSINKI'},{'country': 'SWEDEN', 'city': 'STOCKHOLM'},{'country': 'NORWAY', 'city': 'OSLO'}]
country_dicts = [{'country': country.upper(), 'city': city.upper()} for country_list in countries for (country, city) in country_list]
print(country_dicts)
#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#output
#['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
full_names = [f"{first} {last}" for name_list in names for (first, last) in name_list]
print(full_names)