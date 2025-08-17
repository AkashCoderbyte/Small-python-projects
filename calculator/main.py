# a simple calculator
try:
    a = int(input("Enter a number "))

    b = int(input("Enter another number number "))

    o = input("Enter an operator which you like to perform on your given numbers (+, -, *, / ): ")

    match o:
       case "+":
          print(f"the sum is {a+b}")
       case "-":
          print(f"the sum is {a-b}")
       case "*":
          print(f"the sum is {a*b}")
       case "/":
          print(f"the sum is {a/b}")
       case  default:
          print("Enter a valid operation ")

except Exception as e:
    print(" Enter a valid number")