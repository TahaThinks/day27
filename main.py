import tkinter

# Default Settings
window = tkinter.Tk()
window.title("Taha First GUI Program")
window.minsize(width=500, height=300)

# Add a Label then Pack it
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text Access by Key"
my_label.config(text="New Text Access by Config")





# Keep the Window Open
window.mainloop()