import numpy as np
import matplotlib.pyplot as plt

a = 3
print("a = ", a)
b = 1 / 2
print("b = ", b)
n = 3
print("n = ", n)
x = 0.1
print("x = ", x)

w = b ** n * np.cos(a ** n * np.pi * x)
print("w = ", w)

sw = 'b ** n * np.cos(a ** n * np.pi * x)'
w = sum(eval(sw) for n in range(0, 50))
print("w = ", w)
w = sum(eval(sw) for n in range(0, 100))
print("w = ", w)

dx = 0.00001
x = np.arange(-2, 2, dx)
print("x = ", x)
plt.plot(x, sum(eval(sw) for n in range(0, 100)))
plt.show()

print("Работу выполнил Щугарев А. Ю. 090301-ПОВа-о22")