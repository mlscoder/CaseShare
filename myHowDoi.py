# coding:utf-8
import tkinter
from tkinter import scrolledtext
from tkinter import *
import tkinter.messagebox

from howdoi import howdoi
from translate import Translator

ytm = tkinter.Tk()  # 创建Tk对象
ytm.title("Howdoi@马拉松程序员")  # 设置窗口标题
ytm.geometry("600x400")  # 设置窗口尺寸
menubar = Menu(ytm)
fmenu1 = Menu(ytm)
fmenu2 = Menu(ytm)
l1 = tkinter.Label(ytm, text="请输入搜索问题：", foreground='gray')


def click():
    tkinter.messagebox.showinfo('作者', '@马拉松程序员\nwx:mlscdoer\n版权所有©')


fmenu2.add_command(label='制作信息', command=click)
fmenu2.add_command(label='退出', command=ytm.quit)
l1.pack()  # 指定包管理器放置组件
user_text = tkinter.Entry(background='gainsboro')  # 创建文本框
user_text.pack()
text1 = scrolledtext.ScrolledText(ytm)
w = tkinter.Label(ytm, text="", foreground='red')
menubar.add_cascade(label="关于", menu=fmenu2)


def getGoogle():
    text1.delete(1.0, 'end')
    question = user_text.get().replace(" ", "")
    # 中文翻译成英文
    translator = Translator(from_lang="chinese", to_lang="english")
    translation = translator.translate(question)
    result1 = howdoi.howdoi(question)
    result2 = howdoi.howdoi(translation)
    print(result1)
    print(result2)
    text1.insert('insert', '中文搜索结果：\n')
    text1.insert('insert', result1)
    text1.insert('insert', '英文搜索结果：\n')
    text1.insert('insert', result2)
    w.pack()
    text1.pack()


tkinter.Button(ytm, height=1, text="快速查询", command=getGoogle).pack()
ytm['menu'] = menubar
ytm.mainloop()
