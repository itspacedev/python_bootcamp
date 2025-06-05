import tkinter


# Button Event
def button_clicked():
    print("I got clicked")
    entry_text = my_input.get()
    if len(entry_text) == 0:
        entry_text = "No text entered in the input"

    my_label["text"] = entry_text


window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Label text"
# my_label.pack()
# my_label.place(x=100, y=0)
my_label.grid(row=0, column=0)
my_label.config(padx=40, pady=20)

# Button
my_button = tkinter.Button(text="Click Me :)", command=button_clicked)
# my_button.pack()
my_button.grid(row=1, column=1)

# New Button
new_button = tkinter.Button(text="My New Button")
new_button.grid(row=0, column=2)

# Entry
my_input = tkinter.Entry(width=10)
my_input.insert(tkinter.END, string="Some text to begin with.")
# my_input.pack()
my_input.grid(row=2, column=3)


window.mainloop()
