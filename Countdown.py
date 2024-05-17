import time
from tkinter import *

#Variable
WIDTH = 750
HEIGHT = 400
BTN_WIDTH = 12
BTN_HEIGHT = 3
FONY_COLOR = "#FF0000"
BG_COLOR = "#000000"

T = 0
Text = ""
TIMEGO = 0

window = Tk()
frame = Frame(window)
#===============================


#cal time
#稍微有誤差
def CountDown():
    global Text, T, TIMEGO

    millisecond = "{:0>1}".format(T % 10)
    second = "{:0>2}".format(T // 10)
    minute = "{:0>2}".format(T // 600)
    hour = "{:0>2}".format(T // 36000)
    
    
    if T < 36000:
        Text = minute + ':' + second + '.' + millisecond
    else:
        Text = hour + ':' + minute + ':' + second + '.' + millisecond
    
    label.config(text = Text)

    if TIMEGO == 1:
        T += 1
        window.after(93, CountDown)





def TimeStart():
    global Text, T, button, TIMEGO
    
    TIMEGO = 1
    CountDown()
    button.config(text = 'STOP')


def TimeStop():
    global Text, T, button, TIMEGO

    TIMEGO = 0
    CountDown()
    button.config(text = 'START')


current_function = TimeStart


def toggle_function():
    global current_function, TIMEGO

    current_function()

    if current_function == TimeStart:
        current_function = TimeStop
        
    else:
        current_function = TimeStart




def TimeReset():
    global Text, T

    T = 0
    Text = "00:00.0"
    label.config(text = Text)
    



def main():
    global window, label, Text, canvas, frame, button, Reset, Spacer
    
    window.title("CountDown Machine")
    window.resizable(False, False)
    window.iconphoto(False, PhotoImage(file = 'alert.png'))
    window.configure(background = BG_COLOR)

    #Time label
    label = Label(window, text = Text, font = ("consolas", 100), 
                  fg = FONY_COLOR, bg = BG_COLOR)
    label.pack(fill = 'x')


    #Button
    button = Button(frame, text = 'START', width = BTN_WIDTH, height = BTN_HEIGHT, 
                   fg = FONY_COLOR, bg = BG_COLOR, activebackground = BG_COLOR,
                   font = ("Arial", 20, 'bold'), command = toggle_function)
    
    Reset = Button(frame, text = 'RESET', width = BTN_WIDTH, height = BTN_HEIGHT,
                  fg = FONY_COLOR, bg = BG_COLOR, activebackground = BG_COLOR,
                  font = ("Arial", 20, 'bold'), command = TimeReset)

    #Space between buttons
    Spacer = Label(frame, text = "", width = 10, bg = BG_COLOR)

    button.pack(side = "left")
    Spacer.pack(side = "left")
    Reset.pack(side = "left")

    #Frame
    frame.configure(bg = BG_COLOR)
    frame.pack(pady = 30)



    window.update()


    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (WIDTH / 2))
    y = int((screen_height / 2) - (HEIGHT / 1.2))
    window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

    CountDown()


if __name__ == '__main__':
    main()
    window.mainloop()
