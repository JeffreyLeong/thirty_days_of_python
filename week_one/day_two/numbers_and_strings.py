def get_numbers():
    while True:
        try: 
            first_number = int(input("Give me a number: "))
            second_number = int(input("Give me another number: "))
            return first_number + second_number
        except ValueError:
            print("Invalid input. Please type in numbers.")

answer = get_numbers()
print(f"Hey your numbers add up to: {answer}")