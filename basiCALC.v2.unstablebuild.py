print("Welcome to basiCALC © 2022 Brayden Allen \n Operators: + - * / \n Warning: do not use more than one value for each prompt \n")
while True:
    input_mult = "*"
    input_div = "/"
    input_add = "+"
    input_sub = "-"
    inputequals = "="
    first = float(input('Please enter your first value: '))
    operator = input('Please enter your operator: ')
    second =  float(input('Please enter your second value: '))
    both = (first and second)
    bothint = int(both)
    oneint = int(first)
    twoint = int(second)
    if first == int(first) and operator == input_add:
        print(int(first + second))
    if both != bothint or first != oneint or second != twoint or float(first) + float(second) != bothint and operator == input_mult:
        print(float(first * second))
    if both != bothint or first != oneint or second != twoint or float(first) + float(second) != bothint and operator == input_div:
        print(first / second)
    if operator == input_add and both != bothint or first != oneint or second != twoint or float(first) + float(second) != bothint:
        print(first + second)
    if both != bothint or first != oneint or second != twoint or float(first) + float(second) != bothint and operator == input_sub:
        print(first - second)
    if operator == inputequals and first == second:
        print ("true")
    if operator == inputequals and first != second:
        print("false")