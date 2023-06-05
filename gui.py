import PySimpleGUI as sg
import functions
import time



sg.theme("DarkTeal11")
label = sg.Text('type a to-do')
clock = sg.Text(key = 'clock')
input_box = sg.InputText(tooltip='Enter :',key='todo')
add_button = sg.Button(key= 'Add',image_source='files/add.png',tooltip='Add a ToDo',mouseover_colors='LightBlue2',image_size=(50,50))

list_box = sg.Listbox(values=functions.get_todos(),key='todos',
                      enable_events=True,size=[40,10])

edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete',key='complete')
exit_button = sg.Button('exit',key='exit')

window = sg.Window(title = 'to-do app',
                   layout=[[clock],[label],[input_box,add_button],[list_box,edit_button,complete_button],[exit_button]],
                   font=('Helvetica',20))



while True:
    event, values = window.read(timeout=200) 
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']+'\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todos = functions.get_todos()
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']+'\n'
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('enter an item please!',font=('helvetica','20'))
        case "complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update('')
            except:
                sg.popup('enter an item please!',font=('helvetica','20'))

        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "exit":
            break
        case sg.WIN_CLOSED:
            break
      

window.close()


