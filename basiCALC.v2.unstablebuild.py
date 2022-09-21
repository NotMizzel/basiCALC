print("Welcome to basiCALC © 2022 Brayden Allen \n Operators: + - * / \n Warning: do not use more than one value for each prompt \n")
while True:
    input_mult = "*"
    input_div = "/"
    input_add = "+"
    input_sub = "-"
    first = float(input('Please enter your first value: '))
    operator = input('Please enter your operator: ')
    second =  float(input('Please enter your second value: '))
    if first == float(int(first)):
        print(int(first + second))
        if operator == input_mult:
         print(first * second)
    if operator == input_div:
        print(first / second)
    if operator == input_add and first == float and second == float or first == float(int(first)) and second == float or second == float and first == float(int(second)):
        print(first + second)
    if operator == input_sub:
        print(first - second)