def generate_series(a):
    # Determine the count of odd numbers to generate
    count = a if a % 2 != 0 else a - 1
    
    # Generate the series of odd numbers
    series = [i for i in range(1, 2 * count, 2)]
    
    # Print the series as a comma-separated string
    print(", ".join(map(str, series)))

# Test the function with different inputs
generate_series(1)  # Output: 1
generate_series(2)  # Output: 1
generate_series(3)  # Output: 1, 3, 5
generate_series(4)  # Output: 1, 3, 5
generate_series(5)  # Output: 1, 3, 5, 7, 9
generate_series(6)  # Output: 1, 3, 5, 7, 9
