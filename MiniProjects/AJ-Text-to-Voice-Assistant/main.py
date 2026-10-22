# import libraries
# import modules

from modules.speech import speak, greet_user
from modules.task_manager import ( add_tasks, show_tasks, show_pending_tasks,complete_task)
from modules.calculator import run_calculator

from datetime import datetime




# methods  in this file  1) show_help()  2) main()


# 1) show_help()

def show_help():
    """Display commands supported by AJ."""
    print("""
========== AJ ASSISTANT COMMANDS ==========

  hello              - Greet AJ
  how are you        - Talk to AJ
  my name            - Ask about AJ
  time               - Get current time
  date               - Get today's date

  add task           - Add today's tasks
  show tasks         - View all today's tasks
  pending tasks      - View pending tasks
  complete task      - Mark a task completed

  calculator         - Open calculator
  help               - Show available commands
  exit               - Close AJ

===========================================
""")


# 2) main()


def main():

    """ start the personal assistant"""

    greet_user() # method in modules/speech.py

    print("\n Type help if you see available commands")

    # first ask about the task

    speak("Would you like to add todays task?")  # speak is method of engine of pytt3st

    answer = input("Add today's task yes or no ? (y/n)").strip().lower() # strip() object method of string which removes end and start spaces

    if answer in ["yes","y"]:
        add_tasks()  # method in modules/task_manger.py

    # here first part is end of this file code
    



    while True:

        user_input = input("\n User:").strip().lower()

        if user_input in ["exit", "quit", "bye", "stop"]:
            speak("Good By Sir have a productive Day !")
            break

        elif user_input in ['hello','hi','hii']:
            speak("Hello ! How can I help you?")

        elif "time" in user_input:
            current_time = datetime.now().strftime("%I:%M:%p")
            speak(f" The current time is {current_time}.") 

        elif "date" in user_input:
            current_date = datetime.now().strftime("%d %B %Y")
            current_day = datetime.now().strftime("%A")
            speak(f"Today is {current_day}, {current_date}.")    

        elif "add task" in user_input or "new task" in user_input:
            add_tasks() # it is a method modules/task_manager.py

        elif "pending" in user_input:
            show_pending_tasks()  # it is method in mosules/task_manager.py

        elif "complete task" in user_input or "mark task" in user_input:
            complete_task()   # it is method in modules/task_manager.py

        elif "calculator" in user_input:
            run_calculator()  # method in modules/calculator.py

        elif user_input == "help":
            show_help()

        elif user_input:
            speak("Sorry, I do not understand that command. Type help to see commands.")


if __name__ == "__main__":
    main()            










      



