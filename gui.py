import PySimpleGUI as sg
import functions

label = sg.Text('type a to-do')
input_box = sg.InputText(tooltip='Enter :',key='todo')
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(),key='todos',
                      enable_events=True,size=[40,10])

edit_button = sg.Button('Edit')

window = sg.Window(title = 'to-do app',
                   layout=[[label],[input_box,add_button],[list_box,edit_button]],
                   font=('Helvetica',20))



while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']+'\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todos = functions.get_todos()
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']+'\n'
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break
      

window.close()

