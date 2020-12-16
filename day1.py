# link of problem: https://adventofcode.com/2020/day/1

with open('day1.txt') as file:
    lines = file.read().splitlines()

list=[]
for line in lines:
    list.append(int(line))

target=2020

def prob2(list, target):
    for counter1, num1 in enumerate(list):
        for counter2, num2 in enumerate(list[counter1+1:]):
            if num1+num2 == target:
                print(num1, num2)
                print(num1*num2)
                return

def prob3(list, target):
    for counter1, num1 in enumerate(list):
        for counter2, num2 in enumerate(list[counter1+1:]):
            for counter3, num3 in enumerate(list[counter2+1:]):
                if num1+num2+num3 == target:
                    print(num1, num2, num3)
                    print(num1*num2*num3)
                    return

prob2(list, target)
prob3(list, target)