print("\n--- Stage 3: Single Set from File ---")
try:
    with open("input.txt", "r") as file:
        a = float(file.readline())
        b = float(file.readline())
        c = float(file.readline())
        x = float(file.readline())

    T = a * x**2 + b * x + c
    print(f"Predicted temperature: {T}")
except Exception as e:
    print(f"Error reading file: {e}")
