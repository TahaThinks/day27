from tkinter import *


# Default Settings
window = Tk()
window.title("Taha First GUI Program")
window.minsize(width=500, height=300)

# Add a Label then Pack it
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

def button_clicked():
    my_label.config(text="Button Got Clicked")

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Keep the Window Open
window.mainloop()