def get_todos():
        """
        function to get all todo list from last times
        """
        with open('files/todolist.txt','r') as file_local:
                todos_local = file_local.readlines()
        return todos_local