def greet_user():
    name = input("What is your name?: ")
    return name

user_name = greet_user()
print(f"Hi, {user_name.title()}.")