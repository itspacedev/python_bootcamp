import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New Label text"

# Entry
my_input = tkinter.Entry(width=10)
my_input.insert(tkinter.END, string="Some text to begin with.")
my_input.pack()


# Button
def button_clicked():
    print("I got clicked")
    entry_text = my_input.get()
    if len(entry_text) == 0:
        entry_text = "No text entered in the input"

    my_label["text"] = entry_text


my_button = tkinter.Button(text="Click Me :)", command=button_clicked)
my_button.pack()


# Text
text = tkinter.Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(tkinter.END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", tkinter.END))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
