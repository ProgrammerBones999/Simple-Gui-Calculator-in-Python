from tkinter import *
from tkinter import ttk


#base setup
root = Tk()
root.title("Calculator")
root.geometry('195x200')

#input field
input_field = Entry(root, width=20, borderwidth=10)
input_field.grid(row=0, column=1, columnspan=4)

#funct
def button_click(number):
	#input_field.delete(0, END)
	current = input_field.get()
	input_field.delete(0,END)
	input_field.insert(0, str(current) + str(number))

def clear():
	input_field.delete(0,END)

def delete():
	input_field.delete(0, 1)

def _power():
	first_number = input_field.get()
	global f_num
	global math
	math= 'pow of'
	f_num = float(first_number)
	input_field.delete(0, END)

def per():
	first_number = input_field.get()
	global f_num
	global math
	math= 'percentage'
	f_num = float(first_number)
	input_field.delete(0, END)

def divide():
	first_number = input_field.get()
	global f_num
	global math
	math= 'division'
	f_num = float(first_number)
	input_field.delete(0, END)

def multiply():
	first_number = input_field.get()
	global f_num
	global math
	math= 'multiplication'
	f_num = float(first_number)
	input_field.delete(0, END)

def subtract():
	first_number = input_field.get()
	global f_num
	global math
	math= 'subtraction'
	f_num = float(first_number)
	input_field.delete(0, END)

def add():
	first_number = input_field.get()
	global f_num
	global math
	math= 'addition'
	f_num = float(first_number)
	input_field.delete(0, END)

def equal():
	second_number = input_field.get()
	input_field.delete(0, END)

	if math == 'pow of':
		input_field.insert(0, f_num**float(second_number))

	if math == 'addition':
		input_field.insert(0, f_num+float(second_number))

	if math == 'subtraction':
		input_field.insert(0, f_num-float(second_number))

	if math == 'division':
		input_field.insert(0, f_num/float(second_number))

	if math == 'multiplication':
		input_field.insert(0, f_num*float(second_number))

#num_keys
b_num1 = Button(root, text=('1'), command= lambda: button_click(1))
b_num1.grid(row=2, column=1)

b_num2 = Button(root, text=('2'), command= lambda: button_click(2))
b_num2.grid(row=2, column=2)

b_num3 = Button(root,text=('3'), command= lambda: button_click(3))
b_num3.grid(row=2, column=3)

b_num4 = Button(root, text=('4'), command= lambda: button_click(4))
b_num4.grid(row=3, column=1)

b_num5 = Button(root, text=('5'), command= lambda: button_click(5))
b_num5.grid(row=3, column=2)

b_num6 = Button(root, text=('6'), command= lambda: button_click(6))
b_num6.grid(row=3, column=3)

b_num7 = Button(root, text=('7'), command= lambda: button_click(7))
b_num7.grid(row=4, column=1)

b_num8 = Button(root, text=('8'), command= lambda: button_click(8))
b_num8.grid(row=4, column=2)

b_num9 = Button(root, text=('9'), command= lambda: button_click(9))
b_num9.grid(row=4, column=3)

b_num0 = Button(root, text=('0'), command= lambda: button_click(0))
b_num0.grid(row=5, column=1)

#other buttons
dec = Button(root, text=('.'), command= lambda: button_click())
dec.grid(row=5, column=2)


b_del = Button(root, text='del', command=delete)
b_del.grid(row=5, column=3)

ac = Button(root, text='ac', command=clear)
ac.grid(row=1, column=1)

power = Button(root, text='^', command=_power)
power.grid(row=1, column=2)

percent = Button(root, text='%', command=per)
percent.grid(row=1, column=3)

div = Button(root, text='÷', command=divide)
div.grid(row=1, column=4)

mul = Button(root, text='x', command=multiply)
mul.grid(row=2, column=4)

minus = Button(root, text='-', command= subtract)
minus.grid(row=3, column=4)

plus = Button(root, text='+', command=add)
plus.grid(row=4, column=4)

eq = Button(root, text='=', command=equal)
eq.grid(row=5, column=4)

root.mainloop()
