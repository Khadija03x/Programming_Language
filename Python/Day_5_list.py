#Day-5 :List
#List is a collection which is ordered and changeable. Allows duplicate members.
#List is written with square brackets.


#level 1

#1
lst= list() #creating an empty list
list1 =[]
print(lst)
print(list1)
#2
alphabet = ['a','b','c','d','e','f']
print(alphabet)
#3
print(len(alphabet)) #length of a list
#4
length = len(alphabet)
print(alphabet[0] , alphabet[-1]) #accessing items in a list
#5
mixed_data_types = ['khadija',250, 154 , 'Unmarried','Dhaka']
print(mixed_data_types)
#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#7
print(it_companies)
#8
print(len(it_companies))
#9
length = len(it_companies)
print(it_companies[0], it_companies[length//2],it_companies[-1])
#10
it_companies[0] = 'Meta'
print(it_companies)
#11
it_companies.append('Twitter') #adding an item to the list
print(it_companies)
#12
it_companies.insert(len(it_companies)//2,'LinkedIn') #inserting an item at the middle of the list
print(it_companies)
#13
it_companies[0] = it_companies[0].upper() #changing an item to uppercase
print(it_companies)
#14
print('#'.join(it_companies)) #joining all the items in the list with a separatorango
#15
print('Google' in it_companies) #checking if an item exists in the list
#16
it_companies.sort() #sorting the list
print(it_companies)
#17
it_companies.reverse() #reversing the list
print(it_companies)
#18
print(it_companies[0:3]) #slicing the first 3 companies
#19
print(it_companies[-3:]) #slicing the last 3 companies
#20
middle_index = len(it_companies)//2
if len(it_companies) % 2 == 0:
    print(it_companies[middle_index-1:middle_index+1]) #slicing the middle 2 companies
else:
    print(it_companies[middle_index]) #slicing the middle company
#21
it_companies.remove(it_companies[0]) #removing the first company
print(it_companies)
#22
middle_index = len(it_companies)//2
if len(it_companies) % 2 == 0:
    it_companies.remove(it_companies[middle_index])
    it_companies.remove(it_companies[middle_index-1])
    print(it_companies)
else:
    it_companies.remove[middle_index]
    print(it_companies)
#23
it_companies.remove(it_companies[-1]) #removing the last company
print(it_companies)
#24
it_companies.clear() #removing all the companies
print(it_companies)
#25
del it_companies #deleting the list completely
#26
front_end=['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end=['Node','Express', 'MongoDB']
full_stack = front_end + back_end #joining two lists
print(full_stack)
#27
copied_list = full_stack.copy() #copying a list
full_stack=copied_list+['Python','SQL']
print(full_stack)


#level 2
#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]
print('Min age:', min_age)
print('Max age:', max_age)
ages.append(min_age) #adding min age to the list
ages.append(max_age) #adding max age to the list
print(ages)
if len(ages) % 2 == 0:
    median1 = ages[len(ages)//2]
    median2 = ages[len(ages)//2 - 1]
    median = (median1 + median2) / 2
else:
    median = ages[len(ages)//2]
print('Median:', median)
average = sum(ages) / len(ages)
print('Average:', average)
range_of_ages = max_age - min_age
print('Range of ages:', range_of_ages)
min_diff = abs(min_age - average)
max_diff = abs(max_age - average)
print('Min age difference from average:', min_diff)
print('Max age difference from average:', max_diff)
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
print('Number of countries:', len(countries))
if len(countries) % 2 == 0:
    middle1 = countries[len(countries)//2 - 1]
    middle2 = countries[len(countries)//2]
    print('Middle countries:', middle1, 'and', middle2)

else:
    middle = countries[len(countries)//2]
    print('Middle country:', middle)
#2
if len(countries)%2 == 0:
    first_half = countries[:len(countries)//2]
    second_half = countries[len(countries)//2:]
else:
    first_half = countries[:len(countries)//2 + 1]
    second_half = countries[len(countries)//2 + 1:]
print('First half of countries:', first_half)
print('Last half of countries:', second_half)
#3
country=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country1, country2, country3, *scandic_countries = country
print('Country 1:', country1)
print('Country 2:', country2)
print('Country 3:', country3)
print('Scandinavian countries:', scandic_countries)