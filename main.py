import tkinter
window = tkinter.Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=200, height=100)
window.config(padx=20,pady=20)
def miles_to_km_converter():
    #km = miles * 1.689
    miles = float(miles_input.get())
    km = miles * 1.689
    km_output.config(text=f"{km}")

miles_input = tkinter.Entry(width = 7)
miles_input.grid(column = 1,row = 0)
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)
is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
km_output = tkinter.Label(text="0")
km_output.grid(column=1, row=1)
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)
calculate_button = tkinter.Button(
    text="Calculate", command=miles_to_km_converter)
calculate_button.grid(column=1, row=3)

window.mainloop()
