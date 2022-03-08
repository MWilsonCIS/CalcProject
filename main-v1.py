# importing GUI Library
import tkinter as tk

# initialising global variable that stores the string being displayed
DISPLAY = ""

# defining a function to add the key pressed to the global variable
def btn_press(key):
    '''Button Pressed'''
    global DISPLAY
    DISPLAY += str(key)
    display_box.config(state="normal")
    display_box.delete(0, tk.END)
    display_box.insert(0, DISPLAY)
    display_box.config(state="disabled")

# defining a function to clear the display and the global variable
def ac_btn_press():
    '''AC Button Pressed'''
    global DISPLAY
    DISPLAY = ""
    display_box.config(state="normal")
    display_box.delete(0, tk.END)
    display_box.config(state="disabled")

# defining a function to delete the final character from the display and the global variable
def c_btn_press():
    '''C Button Pressed'''
    global DISPLAY
    DISPLAY = DISPLAY[:-1]
    display_box.config(state="normal")
    display_box.delete(0, tk.END)
    display_box.insert(0, DISPLAY)
    display_box.config(state="disabled")

# defining a function to evaluate the mathematical expression and display the result
def eq_btn_press():
    '''Equation Button Pressed'''
    global DISPLAY
    loc_display = DISPLAY 
    print_display = loc_display.replace('×', '*')
    print_display = print_display.replace('÷', '/')

    ans = str(eval(print_display))

    display_box.config(state="normal")
    display_box.delete(0, tk.END)
    display_box.insert(0, ans)
    display_box.config(state="disabled")

    loc_display = ""
    DISPLAY = ""

# defining the GUI window
window = tk.Tk()
window.configure(bg="#00BFA5")
window.title("CIS Calculator")

# implemeting dynamic resize to the window
for i in range(5):
    window.rowconfigure(i, weight=1)
for i in range(4):
    window.columnconfigure(i, weight=1)

# defining an Entry widget to act as the display
display_box = tk.Entry(window, justify="right", font=("tahoma", 32), state="disabled")
display_box.grid(columnspan=4, ipadx=1)

btn_open_br = tk.Button(window, text='(', command=lambda: btn_press('('), height=3, width=15, fg="black", bg="#1DE9B6")
btn_open_br.grid(row=1, column=0)

btn_close_br = tk.Button(window, text=')', command=lambda: btn_press(')'), height=3, width=15, fg="black", bg="#1DE9B6")
btn_close_br.grid(row=1, column=1)

btn_clear = tk.Button(window, text='C', command=lambda: c_btn_press(), height=3, width=15, fg="#A7FFEB", bg="#009688")
btn_clear.grid(row=1, column=2)

btn_all_clear = tk.Button(window, text='AC', command=lambda: ac_btn_press(), height=3, width=15, fg="#A7FFEB", bg="#00796B")
btn_all_clear.grid(row=1, column=3)

btn7 = tk.Button(window, text='7', command=lambda: btn_press(7), height=3, width=15, fg="black", bg="#1DE9B6")
btn7.grid(row=2, column=0)

btn8 = tk.Button(window, text='8', command=lambda: btn_press(8), height=3, width=15, fg="black", bg="#1DE9B6")
btn8.grid(row=2, column=1)

btn9 = tk.Button(window, text='9', command=lambda: btn_press(9), height=3, width=15, fg="black", bg="#1DE9B6")
btn9.grid(row=2, column=2)

btn_div = tk.Button(window, text='÷', command=lambda: btn_press('÷'), height=3, width=15, fg="black", bg="#1DE9B6")
btn_div.grid(row=2, column=3)

btn4 = tk.Button(window, text='4', command=lambda: btn_press(4), height=3, width=15, fg="black", bg="#1DE9B6")
btn4.grid(row=3, column=0)

btn5 = tk.Button(window, text='5', command=lambda: btn_press(5), height=3, width=15, fg="black", bg="#1DE9B6")
btn5.grid(row=3, column=1)

btn6 = tk.Button(window, text='6', command=lambda: btn_press(6), height=3, width=15, fg="black", bg="#1DE9B6")
btn6.grid(row=3, column=2)

btn_times = tk.Button(window, text='×', command=lambda: btn_press('×'), height=3, width=15, fg="black", bg="#1DE9B6")
btn_times.grid(row=3, column=3)

btn1 = tk.Button(window, text='1', command=lambda: btn_press(1), height=3, width=15, fg="black", bg="#1DE9B6")
btn1.grid(row=4, column=0)

btn2 = tk.Button(window, text='2', command=lambda: btn_press(2), height=3, width=15, fg="black", bg="#1DE9B6")
btn2.grid(row=4, column=1)

btn3 = tk.Button(window, text='3', command=lambda: btn_press(3), height=3, width=15, fg="black", bg="#1DE9B6")
btn3.grid(row=4, column=2)

btn_minus = tk.Button(window, text='-', command=lambda: btn_press('-'), height=3, width=15, fg="black", bg="#1DE9B6")
btn_minus.grid(row=4, column=3)

btn0 = tk.Button(window, text='0', command=lambda: btn_press(0), height=3, width=15, fg="black", bg="#1DE9B6")
btn0.grid(row=5, column=0)

btn_dec = tk.Button(window, text='.', command=lambda: btn_press('.'), height=3, width=15, fg="black", bg="#1DE9B6")
btn_dec.grid(row=5, column=1)

btn_eq = tk.Button(window, text='=', command=lambda: eq_btn_press(), height=3, width=15, fg="black", bg="#18FFFF")
btn_eq.grid(row=5, column=2)

btn_plus = tk.Button(window, text='+', command=lambda: btn_press('+'), height=3, width=15, fg="black", bg="#1DE9B6")
btn_plus.grid(row=5, column=3)

window.mainloop()
