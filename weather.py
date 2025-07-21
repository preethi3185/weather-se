print("\n--- Stage 4: Multiple Sets from File ---")
try:
    with open("input_multi.txt", "r") as file:
        line_number = 1
        for line in file:
            parts = line.strip().split()
            if len(parts) != 4:
                print(f"Line {line_number} is invalid: {line.strip()}")
                line_number += 1
                continue

            a = float(parts[0])
            b = float(parts[1])
            c = float(parts[2])
            x = float(parts[3])

            T = a * x**2 + b * x + c
            print(f"Line {line_number}: a={a}, b={b}, c={c}, x={x} => Predicted temperature: {T}")
            line_number += 1
except FileNotFoundError:
    print("input_multi.txt not found!")
except Exception as e:
    print(f"Error: {e}")
