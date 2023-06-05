def get_todos():
        """
        function to get all todo list from last times
        """
        with open('files/todolist.txt','r') as file_local:
                todos_local = file_local.readlines()
        return todos_local

def write_todos(x):
        with open('files/todolist.txt','w') as file:
                todos = file.writelines(x)
        return todos

if __name__=="__main__":
        print('ok')