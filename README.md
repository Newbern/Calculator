# Calculator
# Python
## Module:
- tkinter
- ttkbootstrap

This is how i built my own calculator and i used `tkinter` to do that very fun project made it able to change size and location in the pop-up window
```bash
import tkinter as tk
import tkkbootstrap as tkk

# Window Display // Title
window = tkk.Window(themename="darkly")
Width = 450
Height = 600
window.geometry(f"{Width}x{Height}")
window.title("Calculator")

# Screen size resizable
window.resizable(width=False, height=False)
```
getting the preferred size and title of the screen along with the theme and size of the screen I had liked.
```bash
# Location and size
x = y = 0
w = Width/4
h = Height/6
```
```bash
# Output field
Output = tk.Label(master=window, text="Calculator", font=('Comic Sans MS', 24), anchor='center')
Output.place(x=x+w, y=y, width=w*2, height=h)
```
This code is the title of the calculator, and it will eventually be changed through the Math function I made.
```bash 
# Empty string used to put numbers in
output = ""

# Math function to keep everything straight
def Math(var):

    # Resetting the Label to be turned into number input can be read
    Output["anchor"] = 'e'
    Output.place_configure(x=x, w=w*4)
    try:
        # Adding the output string
        global output

        # Addition
        if var == "+":
            output += "+"

        # Subtraction
        elif var == "-":
            output += "-"

        # Multiplication
        elif var == "*":
            output += "*"

        # Division
        elif var == "/":
            output += "/"

        # Equal
        elif var == "=":
            if output == "":
                pass

            # Solving
            else:
                Output["text"] = eval(output)
                output = str(eval(output))

        # Clear
        elif var == "c":
            Output["anchor"] = 'center'
            Output.place_configure(x=x+w, w=w*2)
            Output["text"] = "Cleared!"
            output = ""

        # Adding more Numbers
        else:
            output += var

        # Output
        if var != "=":
            if var != "c":
                Output["text"] = output
    except:
        pass
```
Unfortunately I could not figure out how to save space or time by adding a for loop to place all the buttons down, so I had to go through and add them all myself.
```bash
Button = tk.Button(master=window, text='1', command=lambda: Math('1'))
Button.place(x=x, y=y+h*4, width=w, height=h).....
```
