playing = True

# a = int(input("Choose a number:\n"))
# b = int(input("Choose another one:\n"))
# operation = input(
#     "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
# )

# add your code here!
while playing:
    a = int(input("Choose a number:\n"))
    b = int(input("Choose another one:\n"))
    operation = input(
        "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
    )
    if operation == "+":
        print(f"Result : {a+b}")
    elif operation == "-":
        print(f"Result : {a-b}")
    elif operation == "*":
        print(f"Result : {a*b}")
    elif operation == "/":
        print(f"Result : {a/b}")
    elif operation == "exit":
        playing = False
    else:
        print(
            "Choose an appropriate operaion.\nTry again from the beginning.")
