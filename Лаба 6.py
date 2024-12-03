import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Главное окно")
root.geometry("300x200")

def summa(x, y):
    """
    Возвращает сумму двух чисел.

    :param x: Первое число.
    :param y: Второе число.
    :return: Сумма x и y.
    """
    return x + y

def minus(x, y):
    """
    Возвращает разность двух чисел.

    :param x: Первое число.
    :param y: Второе число.
    :return: Разность x и y.
    """
    return x - y

def umno(x, y):
    """
    Возвращает произведение двух чисел.

    :param x: Первое число.
    :param y: Второе число.
    :return: Произведение x и y.
    """
    return x * y

def delenie(x, y):
    """
    Возвращает частное двух чисел.

    :param x: Первое число.
    :param y: Второе число.
    :raises ValueError: Если y равно нулю.
    :return: Частное x и y.
    """
    if y != 0:
        return x / y
    else:
        raise ValueError("На ноль делить нельзя!")

def calculate(operation):
    """
    Выполняет арифметическую операцию и отображает результат.

    :param operation: Операция, которую нужно выполнить.
    """
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        if operation == 'summa':
            result = summa(num1, num2)
            messagebox.showinfo("Результат", f"{num1} + {num2} = {result}")
        elif operation == 'minus':
            result = minus(num1, num2)
            messagebox.showinfo("Результат", f"{num1} - {num2} = {result}")
        elif operation == 'umno':
            result = umno(num1, num2)
            messagebox.showinfo("Результат", f"{num1} * {num2} = {result}")
        elif operation == 'delenie':
            result = delenie(num1, num2)
            messagebox.showinfo("Результат", f"{num1} / {num2} = {result}")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

def clear_entries():
    """Очищает поля ввода."""
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)

def open_calculator():
    """Открывает окно калькулятора."""
    root.withdraw()
    calculator_window = tk.Toplevel(root)
    calculator_window.title("Калькулятор")
    calculator_window.geometry("300x300")

    global entry_num1, entry_num2
    entry_num1 = tk.Entry(calculator_window)
    entry_num1.pack(pady=10)

    entry_num2 = tk.Entry(calculator_window)
    entry_num2.pack(pady=10)

    button_summa = tk.Button(calculator_window, text="Сложить", command=lambda: calculate('summa'))
    button_summa.pack(pady=5)

    button_minus = tk.Button(calculator_window, text="Вычесть", command=lambda: calculate('minus'))
    button_minus.pack(pady=5)

    button_umno = tk.Button(calculator_window, text="Умножить", command=lambda: calculate('umno'))
    button_umno.pack(pady=5)

    button_delenie = tk.Button(calculator_window, text="Разделить", command=lambda: calculate('delenie'))
    button_delenie.pack(pady=5)

    button_clear = tk.Button(calculator_window, text="Очистить", command=clear_entries)
    button_clear.pack(pady=20)

    button_back = tk.Button(calculator_window, text="Назад", command=lambda: go_back(calculator_window))
    button_back.pack(pady=5)

button_open_calculator = tk.Button(root, text="Открыть калькулятор", command=open_calculator)
button_open_calculator.pack(pady=50)
def go_back(calculator_window):
    """Закрывает окно калькулятора и возвращает к главному окну."""
    calculator_window.destroy()
    root.deiconify()

root.mainloop()
