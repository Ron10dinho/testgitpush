def calculator(operator,num1,num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Incorrect input."
print(calculator('+',2,5))