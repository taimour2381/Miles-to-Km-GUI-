from tkinter import *

def converter():
    miles = float(miles_entry.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")

miles_entry = Entry(width=10)
miles_entry.grid(row=0,column=1)
miles_label = Label(text="Miles.")
miles_label.grid(row=0,column=2)
label2 = Label(text="Is equal to: ")
label2.grid(row=1,column=0)
result_label = Label(text="0")
result_label.grid(row=1,column=1)
label3 = Label(text="Kms.")
label3.grid(row=1,column=2)
calculate_button = Button(text="Calculate", command=converter)
calculate_button.grid(row=2,column=1)



window.mainloop()