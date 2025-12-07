todo_list = []

def view_list():
    print("\nYour To-Do List:")
    for i, j in enumerate(todo_list, start=1):
        print(f"{i}. {j}")
    

def add_item():
    task = input("What do you want to add?: ")
    todo_list.append(task)

def remove_item():
    task = input("What do you want to remove?: ")
    if task in todo_list:
        todo_list.remove(task)
    else:
        print("Task not found. Please try again")

while True:
    question = input("\nType 'quit' to quit. What would you like to do? (add, remove, view, quit): ")
    if question == "add":
        add_item()
    elif question == "remove":
        remove_item()
    elif question == "view":
        view_list()
        
    elif question == 'quit':
        print("bye")
        break
    else:
        print("Please select from ('add', 'remove', 'view', 'quit')")


