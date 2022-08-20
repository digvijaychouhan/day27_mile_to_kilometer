from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text=0)
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)


def mile_to_km():
    mile_value = float(miles_input.get())
    kms = round(mile_value * 1.609344)
    kilometer_result_label.config(text=f"{kms}")


button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=4)


# entry = Entry(width=30)
# entry.insert(END, string="Some text to begin with.")
# print(entry.get())
# entry.pack()
#
# text = Text(height=5, width=30)
# text.focus()
# text.insert(END, "Example of multi-line text entry.")
# print(text.get("1.0", END))
# text.pack()
#
#
# def spinbox_used():
#     print(spinbox.get())
#
#
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
#
# def radio_used():
#     print(radio_state.get())
#
#
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))
#
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
#
#
# def scale_used(value):
#     print(value)
#
#
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
window.mainloop()
