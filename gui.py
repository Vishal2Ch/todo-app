# from FreeSimpleGUI import Window

import functions
import FreeSimpleGUI as sg



label =sg.Text("Type in a TO-Do")
input_box= sg.InputText(tooltip="Enter a todo" , key="todo")
add_button= sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos")
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                         layout=[[label], [input_box, add_button],[list_box,edit_button ]],
                         font=('Helvetica',20))
while True:
    event, values = window.read()
    print(1,event)
    print(2,values)
    print(3,values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos1 = values['todo'] + "\n"
            todos.append(new_todos1)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todos = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todos
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()