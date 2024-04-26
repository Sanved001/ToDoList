# This Is A To DO List Application
import os
import Print_Colored




def Add_New_Task():
    Task_input = input("Enter Task: ")
    

    File_open1 = open(r'data\Tasks', 'a')
    File_open1.write(f'\n{Task_input}')
    File_open1.close()
    


def What(Selected_number, Done_Task_Number=[]):
    os.system('cls')  # Clear the console screen
    with open(r'data\Tasks', 'r') as file:
        Task_Number = 0
        for lines in file.readlines():
            Task_Number += 1

            if lines.__contains__('[DONE]'):
                Print_Colored.print_colored(Print_Colored.green,f'{Task_Number}.{lines.strip()} [DONE]')
            elif Selected_number != Task_Number:
                print(f'{Task_Number}.{lines.strip()}')
            elif lines.__contains__('[DONE]'):
                Print_Colored.print_colored(Print_Colored.green,f'{Task_Number}.{lines.strip()} [DONE]')
            elif Task_Number in Done_Task_Number:
                Print_Colored.print_colored(Print_Colored.green,f'{Task_Number}.{lines.strip()} [DONE]')
                with open(r'data\Tasks', 'w') as f:
                    Temp_f_write = f.writelines(lines + '[DONE]')
            elif Selected_number == Task_Number:
                print(f'\033[93m{Task_Number}.{lines.strip()}\033[0m')  # Print in yellow

        print("===========================================================================")

def View_Tasks():
    os.system('cls')  # Clear the console screen
    Done_Tasks = []
    try:
        Selecting = True
        Select = 0
        Selected = False
        while Selecting:
            What(Select, Done_Tasks)
            try:
                if Selected == False:
                    Select = int(input(f'\nEnter the Number of a Corresponding Task to Select it || 0 to Exit || -1 TO DELETE ALL TASKS\n=> '))
                    if Select == 0:
                        Selecting = False
                    elif Select == -1:
                        # Delete all tasks
                        with open(r'data\Tasks', 'w') as file:
                            file.write('')
                        print("All tasks deleted.")
                        input("Press Enter to continue...")
                        Selecting = False
                else:
                    WhatToDo = int(input("What TO DO?\n0.Exit\n1.Go Back\n2.Mark Task As Done\n=> "))
                    if WhatToDo == 0:
                        break
                    elif WhatToDo == 1:
                        Select = 0
                        Selected = False
                    elif WhatToDo == 2:
                        Done_Tasks.append(Select)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except KeyboardInterrupt:
                print("\nOperation aborted by user.")
                break

            if Select != 0:
                Selected = True

    except FileNotFoundError:
        print('Tasks file not found. Create tasks first.')

    input("Press Enter to continue...")




Start_Running = True
while Start_Running:
    user_input = input('''
Enter The Corrosponding Number to the Thing you want to Do
1.Add New Task
2.View Tasks
3.Exit
=>''')
    if user_input == 1 or user_input == '1':
        Add_New_Task()
    if user_input == 2 or user_input == '2':
        View_Tasks()
    if user_input == 3 or user_input == '3':
        exit()

    os.system('cls')











exit()
#Test Zone YAY
