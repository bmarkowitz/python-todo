todos = []
waiting = True

def display_todos():
    print("\n#####\nTodo List: \n")
    if len(todos) == 0:
        print('You have no todos.')
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
    try:
        todo_to_delete = int(input('Enter the number of the todo to delete: ')) - 1
        del todos[todo_to_delete]
    except (ValueError, IndexError):
        print('** Invalid input. Try again. **')

while(waiting):
    display_todos()
    print('Menu:\n- Add todo: 1')
    print('- Delete todo: 2')
    print('- Exit: 4')

    try:
        option = int(input('** Select an option: '))
        if option:
            if option == 1:
                add_todo()
            elif option == 2:
                delete_todo()
            elif option == 4:
                waiting = False
    except ValueError:
        print('** Invalid input. Try again. **\n')
