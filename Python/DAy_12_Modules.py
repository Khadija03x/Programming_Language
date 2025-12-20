#level 1
#1
def random_user_id():
    import random
    import string
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id
print(random_user_id())
#2
def user_id_gen_by_user():
    import random
    import string
    n = int(input("Enter the number of characters for the user ID: "))
    m = int(input("Enter the number of user IDs to generate: "))
    characters = string.ascii_letters + string.digits
    for _ in range(m):
        user_id = ''.join(random.choice(characters) for _ in range(n))
        print(user_id)
user_id_gen_by_user()
print()
#3
def rgb_color_gen():
    import random
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r}, {g}, {b})'
print(rgb_color_gen())  
print(rgb_color_gen())
print(rgb_color_gen())
print()
#level 2
#1
def list_of_hexa_colors(n):
    import random
    colors = []
    for _ in range(n):
        color = '#'+''.join(random.choice('0123456789ABCDEF') for _ in range(6))
        colors.append(color)
    return colors
print(list_of_hexa_colors(3))
print(list_of_hexa_colors(5))
print(list_of_hexa_colors(10))
print()
#2
def list_of_rgb_colors(n):
    import random
    colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f'rgb({r}, {g}, {b})')
    return colors
print(list_of_rgb_colors(3))
print(list_of_rgb_colors(5))
print(list_of_rgb_colors(10))
print()
#3
def generate_colors(color_type, n):
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Invalid color type. Choose 'hexa' or 'rgb'."
print(generate_colors('hexa', 3))
print(generate_colors('rgb', 5))
print(generate_colors('hexa', 10))
print()
print(generate_colors('cmyk', 4))
#level 3
#1
def shuffle_list(lst):
    import random
    random.shuffle(lst)
    return lst
print(shuffle_list([1, 2, 3, 4, 5]))
print(shuffle_list(['a', 'b', 'c', 'd', 'e']))
print(shuffle_list([True, False, True, False]))
print()
#2
def seven_random_numbers():
    import random
    numbers = random.sample(range(10), 7)
    return numbers
print(seven_random_numbers())
print(seven_random_numbers())
print(seven_random_numbers())
print()
#end of file
        