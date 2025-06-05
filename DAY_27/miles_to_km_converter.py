import tkinter

window = tkinter.Tk()
window.title("Miles to Km Converter")
window.config(padx=30, pady=30)


miles_input = tkinter.Entry(width=10)
miles_input.grid(row=0, column=1)

label_miles = tkinter.Label(text="Miles")
label_miles.grid(row=0, column=2)

label_is_equal_to = tkinter.Label(text="is equal to")
label_is_equal_to.grid(row=1, column=0)

result_km = tkinter.Label(text="0")
result_km.grid(row=1, column=1)

label_km = tkinter.Label(text="Km")
label_km.grid(row=1, column=2)


def button_clicked():
    miles = int(miles_input.get())
    km = round(miles * 1.6, 2)
    result_km.config(text=f"{km}")


convert_button = tkinter.Button(text="Convert", command=button_clicked)
convert_button.grid(row=2, column=1)

window.mainloop()