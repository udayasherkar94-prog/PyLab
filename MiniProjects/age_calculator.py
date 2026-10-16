from datetime import datetime

# 1. Accept string input from the user
user_input = input("Enter your birth date (YYYY-MM-DD): ") 

# 2. Parse the string into a date object
birth_date = datetime.strptime(user_input, "%Y-%m-%d").date()

# 3. Get today's date
today = datetime.today().date()

# 4. Subtract to get total days
days_lived = (today - birth_date).days

age = (today.year - birth_date.year)
print(age)

print(f"You have lived for {days_lived} days.")


'''
    # 1. THE CLASSES (The blueprints used to store data types)
date        # Stores only calendar markers: Year, Month, Day
datetime    # Stores calendar markers + wall clock time (Hours, Minutes, Seconds)
timedelta   # Stores a duration of time (a gap or vector between two dates)

# 2. OBJECT GENERATION (Ways to spawn a validated object in memory)
datetime(2026, 10, 16)         # Direct Constructor: Builds an object from explicit numbers
datetime.now()                 # Factory Method: Queries OS clock for a live instance
datetime.strptime(text, fmt)   # Parser Method: Evaluates a text string to extract date objects  fmt like "%dd-%mm-%yyyy" etc

# 3. ATTRIBUTES (Static, read-only facts stored inside the object memory)
# -> Syntax: NO parentheses () because they do not execute calculations.
obj.year    # Accesses the isolated year integer property
obj.month   # Accesses the isolated month integer property
obj.day     # Accesses the isolated day integer property

# 4. METHODS (Dynamic subroutines that perform calculations on the data)
# -> Syntax: REQUIRES parentheses () to trigger execution.
obj.date()             # Behavior: Extracts calendar state, discarding time dimensions
obj.weekday()          # Behavior: Calculates day index (0-6) using calendar algorithms
obj.strftime(format)   # Behavior: Compiles internal numbers into user-facing text strings

'''
