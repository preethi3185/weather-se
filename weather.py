print("\n--- Stage 2: Keyboard Input ---")
try:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    x = float(input("Enter x (time): "))

    T = a * x**2 + b * x + c
    print(f"Predicted temperature: {T}")
except ValueError:
    print("Invalid input! Please enter numeric values.")

