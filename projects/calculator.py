def main():
    num1 = int(input("Input number1: "))
    num2 = int(input("Input number1: "))
    operator = input("Input the operation(+,-,/ or *): ").strip()
    while operator not in ['+', '-', '/', '*']:
        operator = input("Input the operation again(+,-,/ or *): ")
    arithmetic(num1, num2, operator)


def arithmetic(num1, num2, operator):
    match operator:
        case "+":
            print("The Sum is: ", num1 + num2)
        case "-":
            print("The Difference is: ", num1 - num2)
        case "/":
            print("The Division resulted in: ", num1 / num2)
        case "*":
            print("The Multiplication resulted in: ", num1 * num2)

if __name__=="__main__":
    main()