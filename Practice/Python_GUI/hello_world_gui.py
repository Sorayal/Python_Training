from tkinter import *

# method to close the main window after clicking the button


def close_window():
    main_window.destroy()


# creating a top level widget (container like Java Swing)
main_window = Tk()
main_window.title("Hello World")
main_window.geometry("480x480")

# set window color
main_window.configure(bg='#856ff8')


label = Label(main_window, text="Hallo Welt!")
button = Button(main_window, text="Close", command=close_window)

# uses the pack manager to order the window
button.pack()
label.pack()

# to keep the window running
main_window.mainloop()
