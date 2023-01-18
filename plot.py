import os
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

A = simpledialog.askfloat("Input", "Enter the value of A:", parent=root, minvalue=-float('inf'), maxvalue=float('inf'))
B = simpledialog.askfloat("Input", "Enter the value of B:", parent=root, minvalue=-float('inf'), maxvalue=float('inf'))
C = simpledialog.askfloat("Input", "Enter the value of C:", parent=root, minvalue=-float('inf'), maxvalue=float('inf'))


fig, ax = plt.subplots()

if A == 0 and B == 0:
    print("Both A and B can't be zero")
elif A == 0:
    x = [-C/B,-C/B]
    y = [-10,10]
    xtmp=-(C/B)
    ax.plot(x, y, label=f'x = {xtmp}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'x = -{C}/{B}')
elif B == 0:
    x = [-10,10]
    y = [-C/A,-C/A]
    ytmp = -(C/A)
    ax.plot(x, y, label=f'y = {ytmp}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'y = -{C}/{A}')
else:
    x = [-10, 10]
    y = [-(A*x[i]+C)/B for i in range(2)]
    ax.plot(x, y, label=f'{A}*x + {B}*y + {C} = 0')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'{A}*x + {B}*y + {C} = 0')

# line x = 0
x = [0, 0]
y = [-10, 10]
ax.plot(x, y, 'k--')

# line y = 0
x = [-10, 10]
y = [0, 0]
ax.plot(x, y, 'k--')

ax.legend()
plt.grid()
plt.show()
