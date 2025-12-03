def ask_for_user_info():
    name = input("What is your name?: ")
    food = input("What is your favorite food:? ")
    age = int(input("How old are you?: "))
    return name, age, food

name, age, food = ask_for_user_info()
print(f"\nHello {name}, you are {age} years old and you like to eat {food}")


