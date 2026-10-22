import json
from pathlib import Path

# 1. Finds the absolute, real file path of the current script (__file__),
#    resolves any symlinks, and moves up two folder levels (.parent.parent) 
#    to anchor the project's root directory, no matter where the script is executed from.
PROJECT_DIR = Path(__file__).resolve().parent.parent

# 2. Creates a path to a folder named "data" directly inside that project root directory.
DATA_DIR = PROJECT_DIR / "data"

# 3. Creates a path to a specific file named "tasks.json" located inside that "data" folder.
TASK_FILE = DATA_DIR / "tasks.json"



def load_tasks():
    """Load tasks from the JSON file."""

# edge case 1)
    if not TASK_FILE.exists():
        return{}

    try:

        with TASK_FILE.open("r",encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data,dict):
            return data

    # edge case 2)
        return {}

    except (json.JSONDecodeError,OSError):
        print("Warning: Could not read the saved task file.")
        return {}

def save_tasks(tasks):
    """Save tasks to the Json file."""

    DATA_DIR.mkdir(parents=True,exist_ok=True) 

    with TASK_FILE.open("w",encoding="utf-8") as file:
        json.dump(tasks,file,indent=4,ensure_ascii=False) 




