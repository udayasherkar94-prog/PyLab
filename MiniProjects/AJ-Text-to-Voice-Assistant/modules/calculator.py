from modules.speech import speak

def run_calculator():
    """Perform a basic arithmatic calculation."""

    operation = input("""
                    choose addition,subtraction,multiplication, or division:
                  """).strip().lower()

    try:
        num1 = float(input("enter the first number:"))
        num2 = float(input("enter the second number:"))

        if operation in ['addition','add','+']:
            result = num1+num2

        elif operation in ['subtraction','subtract','-']:
            result = num1-num2

        elif operation in ['multiplication','multiply','*']:
            result = num1*num2

        elif operation in ['division','didvide','/']:
            if num2==0:
                speak("Division by zero is not allowed.")
                return

            result = num1/num2

        else:
            speak("I do not recognize that operation. I only do addition,multiplication, subtraction and division")
            return

        speak(f'the result is {result:g}')

    except ValueError:
        speak("Please enter valid number.")             