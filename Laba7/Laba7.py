import tkinter as tk
from tkinter import filedialog
from random import randint

arr = [randint(1, 30)
       for i in range(5)]
with open("arr.txt", "w") as file:
    for number in arr:
        file.write(f"{number} ")
print("Код успешно записан в файл")

with open('arr.txt', 'r') as file:
    content = file.read()
    print(content)
qq = [int(num)
           for num in content.split()
           ]

if qq:
    sr_znach = sum(qq) / len(qq)
    print("Среднее значение массива:", sr_znach)

root = tk.Tk()
root.withdraw()
file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"),
                                                          ("All files", "*.*")],
                                               title="Сохранить файл как")
if file_path:
     with open(file_path, 'w') as file:
           file.write(f"{sr_znach}")