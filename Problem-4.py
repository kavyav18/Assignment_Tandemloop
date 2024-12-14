def count_multiples(numbers):
    multiples_count = {i: 0 for i in range(1, 10)}
    
    for num in numbers:
        for i in multiples_count:
            if num % i == 0:
                multiples_count[i] += 1
                
    return multiples_count

# Input: Read a list of integers from the user
input_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

# Output: Count of multiples
output = count_multiples(input_list)
print(output)
