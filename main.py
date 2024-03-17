from tkinter import *


# Change Label based on the User Input
def button_clicked():
    my_label.config(text=user_input.get())


# Default Settings
window = Tk()
window.title("Taha First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


# Add a Label then Pack it
my_label = Label(text="Default Text", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

new_button = Button(text="Hey")
new_button.grid(column=2, row=0)

# Tkinter Button Module
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)
# Keep the Window Open

# Tkinter Entry Field
user_input = Entry(width=18)
# user_input.pack()
user_input.grid(column=3, row=3)




window.mainloop()
