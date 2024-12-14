def generate_triangular_pattern(a):
    # Generate a triangular pattern
    for i in range(1, a + 1):
        # Generate odd numbers for the current row
        row = [2 * j - 1 for j in range(1, i + 1)]
        # Print the current row as a string of numbers
        print(" ".join(map(str, row)))

# Input from the user
a = int(input("Enter a number: "))
# Generate and display the triangular pattern
generate_triangular_pattern(a)
