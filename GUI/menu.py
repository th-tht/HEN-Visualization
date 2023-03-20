# 实现GUI菜单功能

import tkinter as tk

def single_datain_module():
    ...

#主界面1-顶层菜单：文件输入功能
def mainmenu_function(window):
    mainmenu=tk.Menu(window)
#子菜单1：文件，包含“新建、打开、保存、另存为、关闭”功能
    file_menu=tk.Menu(mainmenu,tearoff=False)
    file_menu.add_command(label='新建')
    file_menu.add_command(label='打开')
    file_menu.add_command(label='保存')
    file_menu.add_command(label='另存为')
    file_menu.add_command(label='关闭')
    mainmenu.add_cascade(label='文件',menu=file_menu)
#子菜单2：添加，包含“添加单个流股数据、导入多个流股数据”
    add_menu=tk.Menu(mainmenu,tearoff=False)
    add_menu.add_command(label='添加单个流股数据',command=single_datain_module)
    add_menu.add_command(label='导入多个流股数据')
    mainmenu.add_cascade(label='添加',menu=add_menu)
#子菜单3：计算，包含“方法1：夹点法、方法2：模拟退火、……”
    calculate_menu=tk.Menu(mainmenu,tearoff=False)
    calculate_menu.add_command(label='方法1:夹点法')
    calculate_menu.add_command(label='方法2:模拟退火')
    mainmenu.add_cascade(label='计算',menu=calculate_menu)
    #将主菜单设置到主窗口
    window.config(menu=mainmenu)
