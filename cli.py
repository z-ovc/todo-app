from functions import get_todos,write_todos

while True:
        user_action = input("type add, show, edit ,complete or exit: ").strip()
    
        if user_action.startswith('add'):
                todo = user_action[4:]+'\n'

                todos = get_todos()
                todos.append(todo)
                # file = open("files/todolist.txt", 'w')
                # file.writelines(todos)
                # file.close()
                write_todos(todos)


        elif user_action.startswith('show'):
                # file = open('files/todolist.txt','r')
                # todos = file.readlines()
                # file.close()
                todos = get_todos()               
                new_todos = [item.strip('\n') for item in todos]
                for index,item in enumerate(new_todos):
                        item = item.title()
                        row = f"{index+1}----{item}"
                        print(row)
        elif user_action.startswith('edit'):
                # number = int(input('Type number of to do to edit: '))
                try:
                        number = int(user_action[5:])
                        number = number-1  
                        todos = get_todos()

                        new_todo = input("Enter alternative to do!: ")
                        todos[number] = new_todo + '\n'
                        write_todos(todos)
                                       
                except ValueError:
                        print('your command is not valid!!!')
                        continue
                
        elif user_action.startswith('complete'):
                # number = int(input('Type number of to do to complete: '))
                try:
                        number = int(user_action[9:])
                        number = number-1
                        todos = get_todos()
                        todo_to_remove = todos[number].strip('\n') 
                        todos.pop(number)
                        with open('files/todolist.txt','w') as file:
                                todos = file.writelines(todos)           
                        message = f"the todo {todo_to_remove} is DONE!"  
                        print(message)  
                except IndexError:
                        print('out Of range')
                        continue
                        
        elif user_action.startswith('exit'):
                break

        else:
                print("byee")

