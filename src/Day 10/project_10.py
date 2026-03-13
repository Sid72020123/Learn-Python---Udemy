# --- Project 10 ---

allowed_operations = list("+-*/")


def perform_operation(op, a, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b


first_time = True

while True:
    if not first_time:
        confirm = (
            input("Continue with the previous answer as a? [yes/no]: ").strip().lower()
        )
        if confirm == "no":
            a = float(input("Enter the first number: "))
    else:
        a = float(input("Enter the first number: "))
        first_time = False
    print("\n".join(allowed_operations))
    op = input("Enter the operation: ")

    b = float(input("Enter the second number: "))

    if op in allowed_operations:
        a = perform_operation(op, a, b)
        print(f"The result is = {a}")
