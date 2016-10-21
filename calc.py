import tkinter as tk

calc = tk.Tk()
calc.title("Tkinter Calculator")

#The numbers and symbols for the calculator
calculatorbuttons = [ 
'7', '8', '9', '/',
'4', '5', '6', '*',
'1', '2', '3', '-',
'0', '+', '=', 'AC' ]

# setting up the row and the colums for the calculator
row = 1
col = 0
for i in calculatorbuttons:
    button_style = 'raised'
    action = lambda x = i: press(x)
    tk.Button(calc, text = i, width = 1, height = 1, relief = button_style, command = action) \
        .grid(row = row, column = col, sticky = 'nesw', )
    col += 1
    if col > 4:
        col = 0
        row += 1

display = tk.Entry(calc, width = 40, bg = "red")#The number entry form
display.grid(row = 0, column = 0, columnspan = 5) # The grid manager for the calculator

#defineing the button function
def press(key):

    #calculation of results
    if key == '=':
        try:
            result = eval(display.get())
            display.insert(tk.END, " = " + str(result))
        except:
            display.insert(tk.END, "Error")
        
    #AC is for Clearing the data that is on the data      
    elif key == 'AC':
        display.delete(0, tk.END)
        display.insert(tk.END, "")        
    else:
        if '=' in display.get():
            display.delete(0, tk.END)
        display.insert(tk.END, key)

calc.mainloop()