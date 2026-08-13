# 1. Function definition to greet a user
def greet_user(username):
    """Prints a friendly greeting message."""
    print(f"Hello, {username}! Welcome to Python.")


# 2. Main execution block
def main():
    print("--- Simple Python Demo Script ---")
    
    # 3. Taking user input and calling a function
    name = input("Enter your name: ")
    greet_user(name)
    
    # 4. Working with a list and conditional filtering
    numbers = [12, 45, 7, 23, 56, 90, 3]
    even_numbers = []
    odd_numbers = []
    
    # 5. Using a for-loop to sort numbers
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
            
    # 6. Printing the structured results
    print("\n--- Processing Results ---")
    print(f"Original List: {numbers}")
    print(f"Even Numbers:  {even_numbers}")
    print(f"Odd Numbers:   {odd_numbers}")


# Standard entry point structure for Python programs
if __name__ == "__main__":
    main()
