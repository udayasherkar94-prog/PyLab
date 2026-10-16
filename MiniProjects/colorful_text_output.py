# output prints in colors varies from different code
# fixed text  "\033[color_code  text string \033[0m" 

"""
    \033[color_code text string \033[0m is an ANSI escape code used to colorize text in a terminal or command prompt.
Here is the quick breakdown:
• \033[ – Starts the formatting command (Escape key signal).
• color_code – The number that picks the color (e.g., 31 for Red, 32 for Green).
• text string – The actual text you want to print.
• \033[0m – Resets the terminal back to default text styles so subsequent text doesn't stay colored.
"""


print("\033[31mThis text is Red!\033[0m")
print("\033[32m This is green text \033[0m")
print("\033[33m This is Yellow text \033[0m")
print("\033[34m This is blue text \033[0m")
print("\033[37m This is white text \033[0m")


"""
 Common Color Codes

Most terminals support standard 16-color codes (8 foreground colors and 8 background colors). Here are the standard text (foreground) colors:

Code	Color
30	    Black
31	    Red
32	    Green
33	    Yellow
34	    Blue
35	    Magenta
36	    Cyan
37	    White

"""