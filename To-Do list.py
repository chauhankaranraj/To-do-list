print("To-Do List: ")
enter_task = ""
view_task = ""
task_complete = ""
quit = ""
task = [""]
list = ["""
Add task
View task
Mark completed
Quit"""]
print("What do you want to do? ")
print(*list, sep=",")
command = input("> ")
command.upper()
if command == "e":
    task = input('Enter your task: ')
    print(task)




