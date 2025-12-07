todo_list = []

# Backend logic
def add_item(task):
    todo_list.append(task)

def remove_item(task):
    todo_list.remove(task)

def view_list():
    return todo_list.copy()

# UI layer (CLI app)
while True:
    action = input("What do you want to do? (add, remove, view, quit): ")

    if action == "add":
        task = input("Enter a task: ")
        add_item(task)
        print("Added!\n")
    elif action == "remove":
        task = input("Enter a task to remove: ")
        if task in todo_list:
            todo_list.remove(task)
            print("Removed!\n")
        else:
            print("Task not found. Please try again\n")
    elif action == "view":
        tasks = view_list()
        print("\nYour tasks: ")
        for t in tasks:
            print("-", t)
    elif action == "quit":
        break