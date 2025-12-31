a=int(input("Enter first number:\n"))
b=int(input("Enter second number:\n"))

op=input("Enter operation(+,-,*,/)\n")

match op:
    case "+":
        print("a+b",a+b)
    case "-":
        print("a-b",a-b)
    case "*":
        print("a*b",a*b)
    case "/":
        print("a/b",a/b)
    case _:
        print("Operation Invalid")