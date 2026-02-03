# CALCULATOR
while True:
    print("\n1. Add  2. Subtract  3. Multiply  4. Divide  5. Exit")

    choice = input("Choose: ")
    
    if choice == '5': break
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    if choice == '1':
        print(f"Result: {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1 - num2}")
    elif choice == '3': 
        print(f"Result: {num1 * num2}")
    elif choice == '4':
        if num2 != 0: 
            print(f"Result: {num1 / num2}")
        else: 
            print("Cannot divide by zero.")

