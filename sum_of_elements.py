def sum_of_elements(numbers, exclude_negative=False):
    return sum(num for num in numbers if not exclude_negative or num >= 0)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
exclude_negative = input("Exclude negative numbers? (yes/no): ").lower() == "yes"

print("Sum of elements:", sum_of_elements(numbers, exclude_negative))
