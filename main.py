# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # 一元一次函数图像
    x = np.arange(-10, 10, 0.1)  # 生成等差数组x
    y = (0.05+x)/(1+x)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("一元一次函数")
    plt.plot(x, y)
    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
