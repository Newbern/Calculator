import tkinter as tk
import ttkbootstrap as tkk

# Window Display // Title
window = tkk.Window(themename="darkly")
Width = 450
Height = 600
window.geometry(f"{Width}x{Height}")
window.title("Calculator")

# Screen size resizable
window.resizable(width=False, height=False)

# Empty string used to put numbers in
output = ""

# Math function to keep everything straight
def Math(var):
    # setting up the label to the right of the screen
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

# Location and size
x = y = 0
w = Width/4
h = Height/6

# Output field
Output = tk.Label(master=window, text="Calculator", font=('Comic Sans MS', 24), anchor='center')
Output.place(x=x+w, y=y, width=w*2, height=h)

# Math
Button = tk.Button(master=window, text="c", command=lambda: Math("c"))
Button.place(x=x, y=y+h, width=w, height=h)

Button = tk.Button(master=window, text="/", command=lambda: Math("/"))
Button.place(x=x+w, y=y+h, width=w, height=h)

Button = tk.Button(master=window, text="x", command=lambda: Math("*"))
Button.place(x=x+w*2, y=y+h, width=w, height=h)

Button = tk.Button(master=window, text="_", command=lambda: Math("-"))
Button.place(x=x+w*3, y=y+h, width=w, height=h)

Button = tk.Button(master=window, text="+", command=lambda: Math("+"))
Button.place(x=x+w*3, y=y+h*2, width=w, height=h*2)

Button = tk.Button(master=window, text="=", command=lambda: Math("="))
Button.place(x=x+w*3, y=y+h*4, width=w, height=h*2)

# Numbers
Button = tk.Button(master=window, text='7', command=lambda: Math('7'))
Button.place(x=x, y=y+h*2, width=w, height=h)

Button = tk.Button(master=window, text='8', command=lambda: Math('8'))
Button.place(x=x+w, y=y+h*2, width=w, height=h)

Button = tk.Button(master=window, text='9', command=lambda: Math('9'))
Button.place(x=x+w*2, y=y+h*2, width=w, height=h)

Button = tk.Button(master=window, text='4', command=lambda: Math('4'))
Button.place(x=x, y=y+h*3, width=w, height=h)

Button = tk.Button(master=window, text='5', command=lambda: Math('5'))
Button.place(x=x+w, y=y+h*3, width=w, height=h)

Button = tk.Button(master=window, text='6', command=lambda: Math('6'))
Button.place(x=x+w*2, y=y+h*3, width=w, height=h)

Button = tk.Button(master=window, text='1', command=lambda: Math('1'))
Button.place(x=x, y=y+h*4, width=w, height=h)

Button = tk.Button(master=window, text='2', command=lambda: Math('2'))
Button.place(x=x+w, y=y+h*4, width=w, height=h)

Button = tk.Button(master=window, text='3', command=lambda: Math('3'))
Button.place(x=x+w*2, y=y+h*4, width=w, height=h)

Button = tk.Button(master=window, text="0", command=lambda: Math("0"))
Button.place(x=x, y=y+h*5, width=w*2, height=h)

Button = tk.Button(master=window, text=".", command=lambda: Math("."))
Button.place(x=x+w*2, y=y+h*5, width=w, height=h)

tk.mainloop()
