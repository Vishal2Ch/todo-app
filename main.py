# from functions_of_main import get_todos , write_todos
from time import strftime

from bonus import functions

now = strftime("%b %d, %Y %H:%M:%S")
print("It is now",now)
while True:
    user_action = input("Type add or show or exit or Edit or complete")


    if user_action.startswith("add"):
        todo = user_action[4:]    #this is the example of list slicing it will only return the value after the index 4

        todos= functions.get_todos("todos.txt")

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos= functions.get_todos("todos.txt")

        for index,item in enumerate(todos):
            item= item.strip('\n')
            r=f"{index + 1}-{item}"
            print(r)
            # print("hello",index,item)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number -1

            todos= functions.get_todos("todos.txt")

            new_todo= input("Enter a new todo")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is invalid")
            # user_action = input("Type add or show or exit or Edit or complete")
            # user_action=user_action.strip()
            continue

    elif user_action.startswith("complete"):
        try:
            number=int(user_action[9:])

            todos= functions.get_todos("todos.txt")
            index= number -1
            todos_to_remove=todos[index]
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todos_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("Enter the value which is already in the list")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("user did not enter correct command")
print("bye")