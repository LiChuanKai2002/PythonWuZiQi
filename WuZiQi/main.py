import tkinter as tk
import sys
from tkinter import messagebox

win = tk.Tk()
win.geometry('1000x750')  # 窗口大小


class QiPan:  # 棋盘类
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def h(self):
        can = tk.Canvas(win, width=self.width, height=self.height, background='gray')  # 设置画布
        can.pack(side="left")
        return can

    def q(self, can):
        for i in range(0, 15):
            can.create_line(25, i * 50 + 25, 725, i * 50 + 25)  # 画水平棋盘线
            can.create_line(i * 50 + 25, 25, i * 50 + 25, 725)  # 画竖直棋盘线
        can.create_oval(20 + 50 * 3, 20 + 50 * 3, 30 + 50 * 3, 30 + 50 * 3, fill='black')  # 左上角点位
        can.create_oval(20 + 50 * 11, 20 + 50 * 11, 30 + 50 * 11, 30 + 50 * 11, fill='black')  # 右下角点位
        can.create_oval(20 + 50 * 3, 20 + 50 * 11, 30 + 50 * 3, 30 + 50 * 11, fill='black')  # 左下角角点位
        can.create_oval(20 + 50 * 11, 20 + 50 * 3, 30 + 50 * 11, 30 + 50 * 3, fill='black')  # 右上角点位
        can.create_oval(15 + 50 * 7, 15 + 50 * 7, 35 + 50 * 7, 35 + 50 * 7, fill='black')  # 中心点点位
        d = {}
        for i in range(1, 16):  # 给棋盘的每个落子点赋初始值，值为0代表未落子
            for j in range(1, 16):
                d[(i, j)] = 0  # 元组为落子点，字典的键为落子点状态
        return d


class LuoZi:  # 落子类

    global steps

    def __init__(self, d, x, y):
        self.d = d
        self.x = x
        self.y = y

    def l(self):
        global steps, c1, c2, isTrue
        m, n = 0, 0
        for m in range(0, 15):  # 判断落子位置
            for n in range(0, 15):
                if (self.x - (20 + m * 50)) ** 2 + (self.y - (20 + n * 50)) ** 2 <= 25 ** 2 + 25 ** 2:
                    break
            if (self.x - (20 + m * 50)) ** 2 + (self.y - (20 + n * 50)) ** 2 <= 25 ** 2 + 25 ** 2:
                break
        if steps % 2 == 0 and (d.get((m + 1, n + 1)) == 0):  # 判断落黑色子
            c1 = can.create_oval(5 + 50 * m, 5 + 50 * n, 45 + 50 * m, 45 + 50 * n, fill='black')
            d[(m + 1, n + 1)] = 1  # 值为1代表黑子
            steps += 1
            isTrue = True
        elif steps % 2 == 1 and (d.get((m + 1, n + 1)) == 0):  # 判断落白色子
            c2 = can.create_oval(5 + 50 * m, 5 + 50 * n, 45 + 50 * m, 45 + 50 * n, fill='white')
            d[(m + 1, n + 1)] = 2  # 值为2代表白子
            steps += 1
            isTrue = True
        return m, n


class PanDuan:  # 规则类
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def p(self):
        global steps
        count = 1
        for k in range(1, 5):  # 竖直方向
            if 14 >= self.n >= 0 and 14 >= self.n + k >= 0 and d[(self.m + 1, self.n + 1)] == \
                    d[(self.m + 1, self.n + 1 + k)]:
                count += 1
            else:
                break
        for k in range(1, 5):
            if 14 >= self.n >= 0 and 14 >= self.n - k >= 0 and d[(self.m + 1, self.n + 1)] == \
                    d[(self.m + 1, self.n + 1 - k)]:
                count += 1
            else:
                break

        if count <= 4:  # 水平方向
            count = 1
            for k in range(1, 5):
                if 14 >= self.m >= 0 and 14 >= self.m + k >= 0 and d[(self.m + 1, self.n + 1)] == \
                        d[(self.m + 1 + k, self.n + 1)]:
                    count += 1
                else:
                    break
            for k in range(1, 5):
                if 14 >= self.m >= 0 and 14 >= self.m - k >= 0 and d[(self.m + 1, self.n + 1)] == \
                        d[(self.m + 1 - k, self.n + 1)]:
                    count += 1
                else:
                    break

        if count <= 4:  # 左上右下方向
            count = 1
            for k in range(1, 5):
                if 14 >= self.n >= 0 and 14 >= self.n + k >= 0 and 14 >= self.m >= 0 and 14 >= self.m + k >= 0 and \
                        d[(self.m + 1, self.n + 1)] == d[(self.m + 1 + k, self.n + 1 + k)]:
                    count += 1
                else:
                    break
            for k in range(1, 5):
                if 14 >= self.n >= 0 and 14 >= self.n - k >= 0 and 14 >= self.m >= 0 and 14 >= self.m - k >= 0 and \
                        d[(self.m + 1, self.n + 1)] == d[(self.m + 1 - k, self.n + 1 - k)]:
                    count += 1
                else:
                    break

        if count <= 4:  # 右上左下方向
            count = 1
            for k in range(1, 5):

                if 14 >= self.n >= 0 and 14 >= self.n - k >= 0 and 14 >= self.m >= 0 and 14 >= self.m + k >= 0 and \
                        d[(self.m + 1, self.n + 1)] == d[(self.m + 1 + k, self.n + 1 - k)]:
                    count += 1
                else:
                    break
            for k in range(1, 5):
                if 14 >= self.n >= 0 and 14 >= self.n + k >= 0 and 14 >= self.m >= 0 and 14 >= self.m - k >= 0 and \
                        d[(self.m + 1, self.n + 1)] == d[(self.m + 1 - k, self.n + 1 + k)]:
                    count += 1
                else:
                    break

        if count >= 5 and steps % 2 == 1:
            messagebox.showinfo(title="黑棋胜", message="黑棋胜出")
        elif count >= 5 and steps % 2 == 0:
            messagebox.showinfo(title="白棋胜", message="白棋胜出")


qi = QiPan(750, 750)  # 棋盘类对象
can = qi.h()
d = qi.q(can)
steps = 0  # 下棋次数

global c1, c2


def kaishi():
    global d, steps
    steps = 0
    can.delete("all")
    qi = QiPan(750, 750)  # 棋盘类对象
    d = qi.q(can)


def luopan(event):
    luo = LuoZi(d, event.x, event.y)  # 落子类对象
    global m, n
    m, n = luo.l()
    pan = PanDuan(m, n)  # 判断类对象
    pan.p()


def huiqi():  # 悔棋
    global isTrue  # 判断是否是第一次悔棋
    if isTrue:
        global c1, c2, steps, m, n
        if steps % 2 == 1:
            can.delete(c1)
        elif steps % 2 == 0:
            can.delete(c2)
        d[(m + 1, n + 1)] = 0
        steps -= 1
        isTrue = False
    elif not isTrue:
        messagebox.showinfo(title="悔棋", message="最多只能悔棋一次")


def tuichu():  # 退出游戏
    sys.exit(0)


btn0 = tk.Button(win, height="3", width="20", bg="#add", text="新的开始", command=kaishi)  # 重新开始按钮
btn0.place(x=800, y=260)
btn1 = tk.Button(win, height="3", width="20", bg="#add", text="悔棋", command=huiqi)  # 悔棋按钮
btn1.place(x=800, y=360)
btn2 = tk.Button(win, height="3", width="20", bg="#add", text="退出游戏", command=tuichu)  # 退出游戏按钮
btn2.place(x=800, y=460)

can.bind('<Button-1>', luopan)  # 画布绑定鼠标单击事件

win.mainloop()
