import numpy as np
import matplotlib.pyplot as plt
import math

u = 720  # 均值μ
# u01 = -1
sig = math.sqrt(100000)  # 标准差δ

maxvalue = 10

x = np.linspace(0, 1439, 24 * 60)
y = (np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig))
mul = maxvalue / max(y)
i = 0
for num in y:
    y[i] = int(num * mul)
    i += 1
print("时间: ")
print(x)
print("值: ")
print(y)

plt.plot(x, y, "r-", linewidth=2)
plt.grid(True)
plt.show()
