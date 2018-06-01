todos = []

def displayTodos():
    print("Todo List: ")
    if len(todos) == 0:
        print('You have no todos.')
    else:
        for todo in todos:
            if todo['completed'] == True:
                print('(x) ' + todo['text'])
            else:
                print('( ) ' + todo['text'])

def addTodo(todoText):
    todos.append({
        'text': todoText,
        'completed': False,
    })
    displayTodos()

def deleteTodo(index):
    del todos[index]
    displayTodos()
