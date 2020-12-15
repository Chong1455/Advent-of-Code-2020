import re

with open("day2.txt") as file:
    input_lines = file.read().splitlines()

# Part One

def check_password(password_line):
    password_list = re.split('[- :]', password_line)
    min_num = int(password_list[0])
    max_num = int(password_list[1])
    char = password_list[2][0]
    word = password_list[4]
    return min_num <= word.count(char) <= max_num

valid_password = 0
for line in input_lines:
    if (check_password(line)):
        valid_password += 1

print(f'There are total of {valid_password} Part One valid passwords.')

# Part Two

def check_password_position(password_line):
    password_list = re.split('[- :]', password_line)
    position1 = int(password_list[0])-1
    position2 = int(password_list[1])-1
    char = password_list[2][0]
    word = password_list[4]
    return (word[position1] == char or word[position2] == char) and (word[position1] != word[position2])

valid_password = 0
for line in input_lines:
    if (check_password_position(line)):
        valid_password += 1

print(f'There are total of {valid_password} Part Two valid passwords.')