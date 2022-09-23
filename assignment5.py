#1. Write a Python Program to Find LCM?
def lcm(x, y):
  if x>y:
      z = x
  else:
      z = y
  while(True):
      if((z % x == 0) and (z % y == 0)):
          lcm = z
          break
      z += 1
  return lcm
print(lcm(4, 6))
print(lcm(15, 17))


#2. Write a Python Program to Find HCF?
def compute_hcf(x, y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
num1 = 54
num2 = 24
print("The H.C.F. is", compute_hcf(num1, num2))


#3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
dec = 344
print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


#4. Write a Python Program To Find ASCII value of a character?
def ascii():
    ch = 'g'
    return("The ASCII value of '" + ch + "' is", ord(ch))
print(ascii())




#5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('Calculator-GeeksForGeeks')
frame = tk.Frame(master=window, bg="skyblue", padx=200)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)


def myclick(number):
    entry.insert(tk.END, number)
def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")
def clear():
    entry.delete(0, tk.END)

button_1 = tk.Button( master=frame,text='1', padx=15,pady=5, width=3,fg='green', command=lambda: myclick(1))
button_1.grid(row=1, column=0)
button_2 = tk.Button(master=frame, text='2', padx=15,pady=5, width=3, command=lambda: myclick(2))
button_2.grid(row=1, column=1)
button_3 = tk.Button(master=frame, text='3', padx=15,pady=5, width=3, command=lambda: myclick(3))
button_3.grid(row=1, column=2)
button_4 = tk.Button(master=frame, text='4', padx=15,pady=5, width=3, command=lambda: myclick(4))
button_4.grid(row=2, column=0)
button_5 = tk.Button(master=frame, text='5', padx=15,pady=5, width=3, command=lambda: myclick(5))
button_5.grid(row=2, column=1)
button_6 = tk.Button(master=frame, text='6', padx=15,pady=5, width=3, command=lambda: myclick(6))
button_6.grid(row=2, column=2)
button_7 = tk.Button(master=frame, text='7', padx=15,pady=5, width=3, command=lambda: myclick(7))
button_7.grid(row=3, column=0)
button_8 = tk.Button(master=frame, text='8', padx=15,pady=5, width=3, command=lambda: myclick(8))
button_8.grid(row=3, column=1)
button_9 = tk.Button(master=frame, text='9', padx=15,pady=5, width=3, command=lambda: myclick(9))
button_9.grid(row=3, column=2)
button_0 = tk.Button(master=frame, text='0', padx=15,pady=5, width=3, command=lambda: myclick(0))
button_0.grid(row=4, column=1)

button_add = tk.Button(master=frame, text="+", padx=15,pady=5, width=3, command=lambda: myclick('+'))
button_add.grid(row=5, column=0)
button_subtract = tk.Button(master=frame, text="-", padx=15, pady=5, width=3, command=lambda: myclick('-'))
button_subtract.grid(row=5, column=1)
button_multiply = tk.Button(master=frame, text="*", padx=15, pady=5, width=3, command=lambda: myclick('*'))
button_multiply.grid(row=5, column=2)
button_div = tk.Button(master=frame, text="/", padx=15,pady=5, width=3, command=lambda: myclick('/'))
button_div.grid(row=6, column=0)
button_clear = tk.Button(master=frame, text="clear",padx=15, pady=5, width=12, command=clear)
button_clear.grid(row=6, column=1, columnspan=2)
button_equal = tk.Button(master=frame, text="=", padx=15,pady=5, width=9, command=equal)
button_equal.grid(row=7, column=0, columnspan=3)

window.mainloop()