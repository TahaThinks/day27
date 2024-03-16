from tkinter import *

def button_clicked():
    print("I got clicked")

# Default Settings
window = Tk()
window.title("Taha First GUI Program")
window.minsize(width=500, height=300)

# Add a Label then Pack it
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text Access by Key"
my_label.config(text="New Text Access by Config")

button = Button(text="Click Me", command=button_clicked)
button.pack()



# Keep the Window Open
window.mainloop()