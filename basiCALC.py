print("Welcome to basiCALC \n Operators: + - * / \n Warning: do not use more than one value for each prompt \n")
while True:
    input_mult = "*"
    input_div = "/"
    input_add = "+"
    input_sub = "-"
    first = float(input('Please enter your first value: '))
    operator = input('Please enter your operator: ')
    second =  float(input('Please enter your second value: '))
    fns = (first and second)
    if operator == input_mult:
        print(first * second)
    if operator == input_div and fns != 0:
        print(first / second)
    if operator == input_add:
        print(first + second) 
    if operator == input_sub:
        print (first - second)
    if first == 0 or second == 0 and operator == input_div:
        print("Sorry, this is invalid, as you cannot divide by 0. Please try again\n")
