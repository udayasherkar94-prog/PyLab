from datetime import datetime

from modules.speech import speak # why it needed because in speech.py we initialize engine of pytts3
from modules.storage import load_tasks,save_tasks


# functions related tasks
# 1) get_today()
# 2) add_tasks()
# 3) show_tasks()
# 4) show_pending_tasks()
# 5) complete_task()

def get_today():
    """Return today's date in YYYY-MM-DD format."""
    return datetime.now().strftime("%Y-%m-%d")

def add_tasks():
    """Add one or more tasks for today."""
    tasks = load_tasks()
    today = get_today()

    if today not in tasks:
        tasks[today] = []

    speak("Enter your tasks separated by commas.")
    user_input = input("Your tasks:")

    # for how many tasks are today
    added_count = 0

    for name in user_input.split(","): # list of tasks seperated by ,
        name = name.strip() # removes spaces

        if not name:
            continue


        # Avoid adding the same task take twice today

        already_exists = any(                      # any() returns True if AT LEAST ONE item below is True
             task['name'].casefold() == name.casefold()   # compare the task's name with the new name,
                                                 # ignoring upper/lower case differences
             for task in tasks[today]               # loop through every task stored for today's date
             )
            # Result: already_exists is True if a task with the same name already exists today,
           # otherwise False

        if already_exists:
            print(f"Task already exists:{name}")
            continue     


        tasks[today].apend({
            "name":name,
            "status":"Pending"
             })

        added_count +=1

    save_tasks(tasks)


    if added_count:
        speak(f"Saved {added_count} new tasks.")
    else:
        speak("No new tasks were added")




def show_tasks():
    """Dispaly all tasks for today."""

    tasks = load_tasks()

    today_tasks = tasks.get(get_today(),[])

    if not today_tasks:
        speak("You have no tasks saved for today.")
        return

    completed = 0
    pending = 0


    print("\n ------TOday's Tasks-----")

    for number ,task in enumerate(today_tasks,start=1):
        name = task['name']
        status = task['status']

        print(f"{number}.{name}-{status}")

        if status == "Completed":
            completed +=1
        else:
            pending +=1

    print("------------------------------------------------")
    print(f"Completed:{completed}")
    print(f"Pending:{pending}")


    completion_rate = (completed/len(today_tasks))*100

    speak(f"You have {len(today_tasks)} tasks."
          f"{completed} completed and {pending} pending."
          f"Your completed rate is {completion_rate:0f} percent."
          )             



def show_pending_tasks():
    """Dispaly tasks that are not completed."""

    tasks = load_tasks()
    today_tasks = tasks.get(get_today(),[])

    pending_tasks = [ task for task in today_tasks if task['status']== "Pending"]

    if not pending_tasks:
        speak("YOu have no pending tasks today.")
        return

    speak(f"YOU have {len(pending_tasks)} pending tasks.")

    for task in pending_tasks:
        print(f"-{task['name']}")
        speak(tasks["name"])


def complete_task():
    """Mark a task as completed by its name."""

    tasks = load_tasks()
    today = get_today()

    today_tasks = tasks.get(today,[])

    if not today_tasks:
        speak("You have no tasks to complete.")
        return

    print("\n Your tasks:")

    for number,task in enumerate(today_tasks,start=1):
        print(f"{number}. {task['name']} - {task['status']}")

    task_name = input("\n Enter the task name you completed:").strip()

    if not task_name:
        speak("You did not enter a task name.")
        return


    if task in today_tasks:
        if task['name'].casefold() == task_name.casefold():
            if task["status"] == "Completed":
                speak("That task is already completed.")
                return

            task["status"] == "Completed"
            save_tasks(tasks)

            speak(f"{task['name']} marked as completed.")
            return

    speak("I could not find that task in today's list.")    
            