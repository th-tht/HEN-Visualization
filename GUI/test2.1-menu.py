from tkinter import *
#创建主窗口
win = Tk()
win.title("C语言中文网")
win.geometry('450x350+300+200')

#创建主目录菜单（顶级菜单）
mainmenu = Menu (win)
#在顶级菜单上新增"文件"菜单的子菜单，同时不添加分割线
filemenu = Menu (mainmenu, tearoff=False)
#新增"文件"菜单的菜单项，并使用 accelerator 设置菜单项的快捷键
filemenu.add_command (label="新建")
filemenu.add_command (label="打开")
filemenu.add_command (label="保存")
filemenu.add_command (label="退出",command=win. quit)
#在主目录菜单上新增"文件"选项，并通过menu参数与下拉菜单绑定
mainmenu.add_cascade (label="文件",menu=filemenu)

'''
注意此处是在mainmenu上add_cascade
'''

# 将主菜单设置在窗口上
win.config (menu=mainmenu)

# 显示主窗口
win.mainloop()