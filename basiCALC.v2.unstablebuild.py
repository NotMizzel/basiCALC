print("Welcome to basiCALC \n Operators: + - * / \n Warning: do not use more than one value for each prompt \n")
while True:
    exponents = "x"
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
    suma = (first + second)
    sumd = (first / second)
    summ = (first * second)
    sums = (first - second)
    if both == bothint or first / second == int(sumd) and operator == input_div:
        print(int(first - second))
    if both == bothint or first - second == int(sums) and operator == input_sub:
        print(int(first - second))
    if both == bothint or first * second == int(summ) and operator == input_mult:
        print(int(first * second))
    if operator == input_add and both == bothint or first + second == int(suma):
        print(int(first + second))
    if operator == input_mult and both != bothint or first != oneint and second != twoint and summ == first * second != int(summ):
        print(first * second)
    if operator == input_div and both != bothint or first != oneint and second != twoint and sumd == first / second != int(sumd):
        print(first / second)
    if operator == input_add and both != bothint or first != oneint or second != twoint and suma == first + second != int(suma) and operator == input_add:
        print(first + second)
    if operator == input_sub and both != bothint or first != oneint and second != twoint and sums == first - second != int(sums):
        print(first - second)
    if operator == inputequals and first == second:
        print ("true")
    if operator == inputequals and first != second:
        print("false")
