#Level 1
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#1
for country in countries:
    print(country)
print()
#2
for name in names:
    print(name)
print()
#3
for number in numbers:
    print(number)
print()
#Level 2

#1
def print_uppercase_countries(countries):
    return list(map(lambda country: country.upper(), countries))
print(print_uppercase_countries(countries))
print()
#2
def square_numbers(numbers):
    return list(map(lambda x: x ** 2, numbers))
print(square_numbers(numbers))
print()
#3
def uppercase_names(names):
    return list(map(lambda name: name.upper(), names))
print(uppercase_names(names))
print()
#4
def land_countries(countries):
    return list(filter(lambda country: 'land' in country.lower(), countries))
print(land_countries(countries))
print()
#5
def six_letter_countries(countries):
    return list(filter(lambda country: len(country) == 6, countries))
print(six_letter_countries(countries))
print()
#6
def more_than_six_letters(countries):
    return list(filter(lambda country: len(country) > 5, countries))
print(more_than_six_letters(countries))
print()
#7
def start_with_e(countries):
    return list(filter(lambda country: country.lower().startswith('e'), countries))
print(start_with_e(countries))
print()
#8
def chain_operations(countries):
    return list(map(lambda country: country.upper(), filter(lambda country: len(country) > 4, countries)))
print(chain_operations(countries))
print()
#9
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))
mixed_list = ['Asabeneh', 123, 'Finland', 456, 'Python', 789]
print(get_string_lists(mixed_list))
print() 
#10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sum_of_all_numbers(x,y):
    return int(x)+int(y)
from functools import reduce
total = reduce(sum_of_all_numbers, numbers)
print(total)
print()
#11
def concatenate_countries(countries):
    return reduce(lambda x, y: x + ', ' + y, countries[:-1] )+ ', and ' + countries[-1]  + 'are north European countries.'
print(concatenate_countries(countries))
print()
#12
import data.countries as country_data
def categorize_countries_with_common_data():
    pattern = {
        'land': [],
        'ia': [],
        'island': [],
        'stan': [],
        'other': []
    }
    for country in country_data.countries:
        lower_country = country.lower()
        if 'land' in lower_country:
            pattern['land'].append(country)
        elif lower_country.endswith('ia'):
            pattern['ia'].append(country)
        elif 'island' in lower_country:
            pattern['island'].append(country)
        elif 'stan' in lower_country:
            pattern['stan'].append(country)
        else:
            pattern['other'].append(country)
    return pattern
print(categorize_countries_with_common_data())
print()
#13
def returning_dictinary():
    country_dict = {}
    total_countries = len(country_data.countries)
    country_dict['total_countries'] = total_countries

    for country in country_data.countries:
        first_letter = country[0]
        if first_letter in country_dict:
            country_dict[first_letter] += 1
        else:
            country_dict[first_letter] = 1
    return country_dict

print(returning_dictinary())
print()
#14
def get_first_ten_countries():
    return country_data.countries[:10]
print(get_first_ten_countries())
print()
#15
def get_last_ten_countries():
    return country_data.countries[-10:]
print(get_last_ten_countries())
print() 
#Level 3
#1
import data.countries_data as countries_Data

sorted_by_name = sorted(
    countries_Data.countries_data,
    key=lambda country: country["name"]
)
sorted_by_capital = sorted(
    countries_Data.countries_data,
    key=lambda country: country["capital"]
)
sorted_by_population = sorted(
    countries_Data.countries_data,
    key=lambda country: country["population"]
)
sorted_by_population_desc = sorted(
    countries_Data.countries_data,
    key=lambda country: country["population"],
    reverse=True
)
print("Countries sorted by name:" , sorted_by_name)
print()
print("Countries sorted by capital:" , sorted_by_capital)
print()
print("Countries sorted by population:" , sorted_by_population)
print()
print("Countries sorted by population (descending):" , sorted_by_population_desc)
print()
#2 
from collections import Counter

language_counter = Counter()

for country in countries_Data.countries_data:
    for language in country["languages"]:
        language_counter[language] += 1

ten_most_spoken_languages = language_counter.most_common(10)
print(ten_most_spoken_languages)
#3
ten_most_populated_countries = sorted_by_population_desc[:10]
print(ten_most_populated_countries)