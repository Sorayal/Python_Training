from tkinter import *

# global variable to give the components access to main window
# None is like null in Java
main_window = None


# method to close the main window after clicking the button
def close_window():
    global main_window
    main_window.destroy()


# init main window
def init_main_window():
    global main_window

    # creating a top level widget (container like Java Swing)
    main_window = Tk()
    main_window.title("Hello World")
    main_window.geometry("480x480")
    # set window color
    main_window.configure(bg='#856ff8')


# init button and label
def init_button_label():
    global main_window
    label = Label(main_window, text="Hallo Welt!",
                  height=1, width=10, font=('Courier', 11))
    button = Button(main_window, text="Close",
                    command=close_window, height=1, width=10, font=('Courier', 11))
    # button.config(height=1, width=10)

    # uses the place manager to order the window
    # x = 10, y = 10
    button.place(x=205, y=250)
    label.place(x=205, y=0)


# build components
init_main_window()
init_button_label()

# to keep the window running, must run after all related components
# are built.
main_window.mainloop()
