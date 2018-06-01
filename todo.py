todos = []

def display_todos():
    print("\n#####\nTodo List: \n")
    if len(todos) == 0:
        print('~ Empty ~')
    else:
        for todo in todos:
            if todo['completed'] == True:
                print('(x) ' + todo['text'])
            else:
                print('( ) ' + todo['text'])
    print('#####\n')

def add_todo():
    todo_text = input('Enter a todo: ')
    if todo_text:
        todos.append({
            'text': todo_text,
            'completed': False,
        })
    else:
        print('** Invalid input. Try again. ** ')

def delete_todo():
    if len(todos) == 0:
        print('Add a todo before attempting to delete something.')
    else:
        try:
            todo_to_delete = int(input('Enter the number of the todo to delete: ')) - 1
            del todos[todo_to_delete]
        except (ValueError, IndexError):
            print('** Invalid input. Try again. **')

def change_todo():
    if len(todos) == 0:
        print('Add a todo before attempting to change something.')
    else:
        try:
            todo_to_change = int(input('Enter the number of the todo to change: ')) - 1
            new_todo_text = input('Enter new text for the todo: ')

            todos[todo_to_change]['text'] = new_todo_text
        except (IndexError, ValueError):
            print('** Invalid input. Try again. **')

while True:
    display_todos()
    print('Menu:\n- Add todo: 1')
    print('- Delete todo: 2')
    print('- Change todo: 3')
    print('- Exit: 4')

    try:
        option = int(input('** Select an option: '))
        if option:
            if option == 1:
                add_todo()
            elif option == 2:
                delete_todo()
            elif option == 3:
                change_todo()
            elif option == 4:
                break
    except ValueError:
        print('** Invalid input. Try again. **\n')
