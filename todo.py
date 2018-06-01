todos = []

def display_todos():
    print("Todo List: ")
    if len(todos) == 0:
        print('You have no todos.')
    else:
        for todo in todos:
            if todo['completed'] == True:
                print('(x) ' + todo['text'])
            else:
                print('( ) ' + todo['text'])

def add_todo(todo_text):
    todos.append({
        'text': todo_text,
        'completed': False,
    })
    display_todos()

def delete_todo(index):
    del todos[index]
    display_todos()

def change_todo(index, new_todo_text):
    try:
        todos[index]['text'] = new_todo_text
    except IndexError:
        print('The todo you have tried to change does not exist.')
    display_todos()

add_todo('hello')
change_todo(0, 'goodbye')
