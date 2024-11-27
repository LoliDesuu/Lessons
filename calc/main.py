import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    pass



window = tk.Tk()
window.title("Калькулятор")
window.geometry("350x350")
window.resizable(False, False)
button_plus = tk.Button(window, text = "+", command=add)
button_plus.place(x=90, y=190, width =30, height= 30)
button_minus = tk.Button(window, text = "-")
button_minus.place(x=140, y=190, width =30, height= 30)
button_mult = tk.Button(window, text = "*")
button_mult.place(x=190, y=190, width =30, height= 30)
button_div = tk.Button(window, text = "/")
button_div.place(x=240, y=190, width =30, height= 30)
number1_entry = tk.Entry()
number1_entry.place(x=90, y=100, width=180)
number2_entry = tk.Entry()
number2_entry.place(x=90, y=150, width=180)
answer_entry = tk.Entry()
answer_entry.place(x=90, y=255, width=180)
number1 = tk.Label(window, text="Введите первое число:")
number1.place(x=63, y=75, width=180)
number2 = tk.Label(window, text="Введите второе число:")
number2.place(x=63, y=125, width=180)
answer = tk.Label(window, text="Ответ:")
answer.place(x=19, y=230, width=180)
window.mainloop()

