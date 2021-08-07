print('')
print('-------------------- Task 1 --------------------')
print('')

with open ('my_id.txt', 'w', encoding='utf-8') as file:
    file.write(f'My ID:\n')
    file.write('Name: Liya\n')
    file. write('LastName: Yoelson\n')
    file.write('Phone number: 0506470815\n')

print('')
print('-------------------- Task 2 --------------------')
print('')

from collections import Counter

def open_file1():
    my_dict = {}
    lines = open('my_id.txt').read().splitlines()
    for slice in lines:
        slice_1 = slice.split()
        z = dict(Counter(slice_1))
        my_dict = my_dict | z
    print(my_dict)

open_file1()

print('')
print('-------------------- Task 3 --------------------')
print('')

def num_lunes():
    N = 3
    with open('filename.txt') as file:
        for i in range(N):
            line = next(file).strip()
            print(line)

num_lunes()

print('')
print('-------------------- Task 4 --------------------')
print('')

def longest_word(filename):
    with open(filename) as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    count = [word for word in words if len(word) == max_len]
    print(count)

longest_word('filename.txt')

print('')
print('-------------------- Task 5 --------------------')
print('')

def revers_string():
    my_string = 'Python Class Hello .py'
    reverse_string = ''
    for word in my_string.split():
        reverse_string = f'{word} {reverse_string}'
    print(reverse_string)

revers_string()

print('')
print('-------------------- Task 6 --------------------')
print('')

class LowerString:

    def get_String(self, user_string = input('Enter string: ')):

        self.user_string = user_string


    def print_String(self):

        x = self.user_string.upper()
        print(x)

str1 = LowerString()
str1.get_String()
str1.print_String()

print('')
print('-------------------- Task 7 --------------------')
print('')

class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area_rectangle(self):
        area =self.length * self.width
        print(f'Area of a rectangle: {area}')

rec1 = Rectangle(5,10)
rec1.area_rectangle()
