todos = []

while True:
    user_action = input("Type add, show, edit or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                row = f"{index}-{item.title()}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit:"))
            number = number - 1
            new_todo = input("Enter a new todo:")
            todos[number] = new_todo
        case 'exit':
            break
        case _:
            print("Hey you entered unknown command!")
print("Bye!")
