def input_length(first_name, last_name):
    first_name_length = len(first_name)
    last_name_length = len(last_name)
    if first_name_length >= 2 and last_name_length >= 2:
        print(f"First name length: {first_name_length}")
        print(f"Last name length: {last_name_length}")
    else:
        print("Invalid input, please enter at least 2 characters.")


while True:
    first_name = input("Enter your first name:\n").strip()
    last_name = input("Enter your last name:\n").strip()

    input_length(first_name, last_name)

    continue_input = input("Would you like to enter another name?: (yes/no)")
    if continue_input != "yes":
        break
