import tkinter
import math
from math import *
from tkinter import *
from tkinter import messagebox
# Messagebox module : It is used to display the message boxes in the python application.
                     # There are various functions which are used to display the messageboxes

var ="" 
A = 0
opr = ""

#defining a function for button 1
def button_1():
    global var
    var = var +"1"
    data.set(var)

#defining a function for button 2

def button_2():
    global var
    var =  var + "2"
    data.set(var)

#defining a function for button 3

def button_3():
    global var
    var = var + "3"
    data.set(var)

#defining a function for button 4

def button_4():
    global var
    var = var + "4"
    data.set(var)

#defining a function for button 5

def button_5():
    global var
    var = var + "5"
    data.set(var)

#defining a function for button 6

def button_6():
    global var
    var = var + "6"
    data.set(var)

#defining a function for button 7

def button_7():
    global var
    var = var + "7"
    data.set(var)

#defining a function for button 8

def button_8():
    global var
    var = var + "8"
    data.set(var)

#defining a function for button 9

def button_9():
    global var
    var = var + "9"
    data.set(var)

#defining a function for 0 

def button_0():
    global var
    var = var + "0"
    data.set(var)

#defining a function for addition

def button_add():
    global var
    global A
    global opr

    A = float(var)
    opr = "+"
    var = var + "+"
    data.set(var)

#defining a function for subtraction

def button_sub():
    global var
    global A
    global opr

    A = float(var)
    opr = "-"
    var = var + "-"
    data.set(var)

#defining a function for multiply

def button_multipy():
    global var
    global A
    global opr

    A = float(var)
    opr = "*"
    var  = var + "*"
    data.set(var)

#defining a function for division

def button_divide():
    global var
    global A
    global opr

    A = float(var)
    opr = "/"
    var = var + "/"
    data.set(var)

#defining a function for equalto

def button_equalto():
    global var
    global A
    global opr

    A = float(var)
    opr = "="
    var = var + "="
    data.set(var)

#defining a function for clearing

def button_clear():
    global var
    global A
    global opr

    A = float(var)
    opr = ""
    var = ""
    data.set(var)

#defining a function for absolute value

def button_absval():
    global var
    global A
    global opr

    A = float(var)
    opr = "//"
    var = var + "//"
    data.set(var)

#defining a function for remainder

def button_remainder():
    global var
    global A
    global opr

    A = float(var)
    opr = "%"
    var = var + "%"
    data.set(var)

#defining a function for power

def button_power():
    global var
    global A
    global opr

    A = float(var)
    opr = "**"
    var = var + "**"
    data.set(var)

#defining a function for log

def button_log():
    global var
    global A
    global opr

    A = float(var)
    opr = "log"
    var = var + "log"
    data.set(var)

#defining a function to display the result

def res():
    global var
    global A
    global opr 
    var2 = var

    if opr == "+":

        a = float(var2.split("+")[1])
        x = A+a
        data.set(x)
        var = str(x)

    elif opr == "-":

        a = float(var2.split("-")[1])
        x = A-a
        data.set(x)
        var = str(x)

    elif opr == "*":

        a = float(var2.split("*")[1])
        x = A*a
        data.set(x)
        var = str(x)

    elif opr == "/":

        a = float(var2.split("/")[1]) 
        x = A/a
        data.set(x)
        var = str(x)

        if a== 0:
            messagebox.showerror("Division by zero not allowed")
            A=""
            var=""
            data.set(var) 
            var = str(x)
                       

    elif opr == "//":

        a = float(var2.split("//")[1])
        x = A//a
        data.set(x)
        var = str(x)

    elif opr == "%":

        a = float(var2.split("%")[1])
        x = A%a
        data.set(x)
        var = str(x)

    elif opr == "**":

        a = float(var2.split("**")[1])
        x = A**a
        data.set(x)
        var = str(x)  

    elif opr == "log":

        a = float(var2.split("log")[1])
        x = math.log(a)
        data.set(x)
        var = str(x)   

    else :

        x= float(A/a)
        data.set(x)
        var = str(x)


# DEFINING THE CODE FOR GUI OF THE CALCULATOR :

# creating an object of the Tk() class  
guiWindow = tkinter.Tk()  
# setting the size of the window  
guiWindow.geometry("1366x768")   
guiWindow.resizable(0, 0)  
# setting the title of the Calculator window  
guiWindow.title("GUI Calculator - BY_UDAY")  
  
# creating the label for the window  
data = StringVar()  
guiLabel = Label(  
    guiWindow,  
    text = "Label",  
    anchor = SE,  
    font = ("Cambria Math", 20),  
    textvariable = data,  
    background = "#A9A9A9",  
    fg = "#000000"  
)  
# using the pack() method  
guiLabel.pack(expand = True, fill = "both")  
  
# creating the frames for the buttons  
# first frame  
frameOne = Frame(guiWindow, bg = "#A9A9A9")  
frameOne.pack(expand = True, fill = "both") # frame can expand if it gets some space  
  
# second frame  
frameTwo = Frame(guiWindow, bg = "#00ffff")  
frameTwo.pack(expand = True, fill = "both")  
  
# third frame  
frameThree = Frame(guiWindow, bg = "#00ffff")  
frameThree.pack(expand = True, fill = "both")  
  
# fourth frame  
frameFour = Frame(guiWindow, bg = "#00ffff")  
frameFour.pack(expand = True, fill = "both")  

# fifth frame  
frameFifth = Frame(guiWindow, bg = "#00ffff")  
frameFifth.pack(expand = True, fill = "both")  
  
# creating buttons for each frame  
# buttons for first frame  
# button 1  
buttonONE = Button(  
    frameOne,  
    text = "1",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_1  
)  
# placing buttons side by side  
buttonONE.pack(side = LEFT, expand = True, fill = "both")  
  
# button 2  
buttonTWO = Button(  
    frameOne,  
    text = "2",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_2  
)  
# placing buttons side by side  
buttonTWO.pack(side = LEFT, expand = True, fill = "both")  
  
# button 3  
buttonTHREE = Button(  
    frameOne,  
    text = "3",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_3 
)  
# placing buttons side by side  
buttonTHREE.pack(side = LEFT, expand = True, fill = "both")  
  
# button C  
buttonC = Button(  
    frameOne,  
    text = "C",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_clear  
)  
# placing buttons side by side  
buttonC.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for second frame  
# button 4  
buttonFOUR = Button(  
    frameTwo,  
    text = "4",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_4 
)  
# placing buttons side by side  
buttonFOUR.pack(side = LEFT, expand = True, fill = "both")  
  
# button 5  
buttonFIVE = Button(  
    frameTwo,  
    text = "5",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_5  
)  
# placing buttons side by side  
buttonFIVE.pack(side = LEFT, expand = True, fill = "both")  
  
# button 6  
buttonSIX = Button(  
    frameTwo,  
    text = "6",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_6  
)  
# placing buttons side by side  
buttonSIX.pack(side = LEFT, expand = True, fill = "both")  
  
# button +  
buttonADD = Button(  
    frameTwo,  
    text = "+",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_add  
)  
# placing buttons side by side  
buttonADD.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for third frame  
# button 7  
buttonSEVEN = Button(  
    frameThree,  
    text = "7",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_7 
)  
# placing buttons side by side  
buttonSEVEN.pack(side = LEFT, expand = True, fill = "both")  
  
# button 8  
buttonEIGHT = Button(  
    frameThree,  
    text = "8",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_8  
)  
# placing buttons side by side  
buttonEIGHT.pack(side = LEFT, expand = True, fill = "both")  
  
# button 9  
buttonNINE = Button(  
    frameThree,  
    text = "9",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_9  
)  
# placing buttons side by side  
buttonNINE.pack(side = LEFT, expand = True, fill = "both")  
  
# button -  
buttonSUB = Button(  
    frameThree,  
    text = "-",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_sub  
)  
# placing buttons side by side  
buttonSUB.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for fourth frame  
# button 0  
buttonZERO = Button(  
    frameFour,  
    text = "0",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_0 
)  
# placing buttons side by side  
buttonZERO.pack(side = LEFT, expand = True, fill = "both")  
  
# button *  
buttonMUL = Button(  
    frameFour,  
    text = "*",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_multipy  
)  
# placing buttons side by side  
buttonMUL.pack(side = LEFT, expand = True, fill = "both")  
  
# button /  
buttonDIV = Button(  
    frameFour,  
    text = "/",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_divide 
)  

# placing buttons side by side  
buttonDIV.pack(side = LEFT, expand = True, fill = "both")  
  
# button = 
buttonEQUAL = Button(  
    frameFour,  
    text = "=",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = res  
)  
# placing buttons side by side  
buttonEQUAL.pack(side = LEFT, expand = True, fill = "both") 


# button //
buttonAbsval = Button(  
    frameFifth,  
    text = "//",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_absval  
)  
# placing buttons side by side  
buttonAbsval.pack(side = LEFT, expand = True, fill = "both") 


# button %  
buttonRemainder = Button(  
    frameFifth,  
    text = "%",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_remainder 
)  
# placing buttons side by side  
buttonRemainder.pack(side = LEFT, expand = True, fill = "both") 


# button **  
buttonPower = Button(  
    frameFifth,  
    text = "**",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_power  
)  
# placing buttons side by side  
buttonPower.pack(side = LEFT, expand = True, fill = "both")  
  
# button log 
buttonPower = Button(  
    frameFifth,  
    text = "log",  
    font = ("Times", "24", "bold italic"),  
    relief = GROOVE,  
    border = 1,  
    command = button_log 
)  
# placing buttons side by side  
buttonPower.pack(side = LEFT, expand = True, fill = "both")  
  
# running the GUI  
guiWindow.mainloop()  
 




























