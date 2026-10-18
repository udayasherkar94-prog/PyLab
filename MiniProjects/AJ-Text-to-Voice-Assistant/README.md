
# AJ - Personal AI Assistant

A beginner-friendly Python personal assistant with text-to-speech,
daily task management, time and date information, and a calculator.

## Features

- Text-to-speech responses using pyttsx3
- Time-based greetings
- Current date and time
- Add and view daily tasks
- Mark tasks as completed
- Check pending tasks
- Calculate daily task completion percentage
- Save tasks in a local JSON file
- Basic calculator
- Command-line interaction

## Technologies Used

- Python
- pyttsx3
- JSON
- datetime
- pathlib

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the dependencies:

   pip install -r requirements.txt

4. Start the assistant:

   python main.py

## Task Storage

Tasks are stored locally in `data/tasks.json`, organized by date.

## Future Improvements

- Speech recognition
- Task deadlines and reminders
- Task history and weekly reports
- GUI dashboard
- AI-powered conversations
