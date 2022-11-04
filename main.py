#Task 1: Fizz Buzz
print('Task 1: Fizz Buzz')
number = int(input('Write number: '))
result = ''
if (number % 3) == 0:
    result = 'Fizz '
if (number % 5) == 0:
    result = result + 'Buzz'
if result == '':
    result = f'{number}'
print(result)
input('Press "Enter" to continue!')

#Task 2
print('Task 2')
number = int(input('Write number: '))
result = ''
if number >= 2:
    result = 'Неплохо'
if number >= 6:
    result = 'Так себе'
if number > 20:
    rstult = 'Отлично'
if number % 2 == 1:
    result = 'Плохо'
print(result)
input('Press "Enter" to continue')

#Task 3
print('Task 3')
number = int(input('Write a number: '))
result = ''
for i in range(number):
    result += f'{i + 1}'
print(result)
input('Press "Enter" to continue')

#Task 4
print('Task 4')
str = 'How are you? Eh, ok. Low or Lower? Ohhh.'
result = ''
for i in range(len(str)):
    if str[i].isupper() == True:
        result = result + str[i]
print(f'Исходная строка: {str}')
print(result)
input('Press "Enter" to continue')

#Task 5
print('Task 5')
string = input('Write a string: ')
words = string.split()
count = 0
for i in range(len(words)):
    if words[i].isalpha() == True:
        count += 1
    else:
        count = 0
    if count == 3:
        break
if count == 3: print('True')
else: print('False')

input('Press "Enter" to continue')

#Task 6
print('Task 6')
strings = ["left", "right", "left", "stop"]
string = strings[0]
for i in range(len(strings) - 1):
    string += f",{strings[i + 1]}"
print('Было: ' + string)
string = string.replace('right', 'left')
print('Стало: ' + string)