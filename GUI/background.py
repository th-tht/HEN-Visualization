
# 实现界面背景，包括具体输入框布局，以及展示效果


'''
个人代码规范:主函数、子函数名、重要组件(包含指令的,如按钮、菜单)一般用_隔开
设计思路:创建主窗口,包含文件、计算、绘图等功能

主界面——主菜单功能——子菜单1模块
                    子菜单2模块
        数据显示功能

'''

import tkinter as tk
from tkinter import ttk
import time
import random

WIDTH=1200;HEIGHT=600 #主窗口宽高
SUBWID=500;SUBHEI=400 #子窗口宽高
FORMWID=800;FORMHEI=300 #数据显示表宽高
dis_s=10;dis_l=20 #较小和较大的间距
wid=75;hei=25 #标签、按钮宽高,输入框高
entry_wid=100 #输入框宽
input_dict={'0':'init-text0','1':'init-text1','2':'init-text2','3':'init-text3'}


##主窗口
window=tk.Tk() #生成主窗口
window.title('换热网络设计')
window.geometry(f'{WIDTH}x{HEIGHT}+{dis_l}+{dis_l}') #在较大间距的位置生成对应宽高的窗口

#主界面1-顶层菜单：文件输入功能
def mainmenu_function():
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

#子菜单2-模块1：输入单个流股数据模块
def single_datain_module():
    #子窗口1
    sub_window_1=tk.Toplevel()
    sub_window_1.title('流股参数')
    sub_window_1.geometry(f'{SUBWID}x{SUBHEI}')
    #输入框前文字
    tempin=tk.Label(sub_window_1,text='进口温度(℃)')
    tempin.place(x=dis_s,y=dis_s,width=wid,height=hei)
    tempout=tk.Label(sub_window_1,text='出口温度(℃)')
    tempout.place(x=dis_s,y=2*dis_s+hei,width=wid,height=hei)
    cap=tk.Label(sub_window_1,text='热容(J/K)')
    cap.place(x=dis_s,y=3*dis_s+2*hei,width=wid,height=hei)
    flow=tk.Label(sub_window_1,text='流量(kg/s)')
    flow.place(x=dis_s,y=4*dis_s+3*hei,width=wid,height=hei)
    #输入框
    for i in range(4):
        input_dict[i]=tk.StringVar()
        newentry=tk.Entry(sub_window_1,textvariable=input_dict[i])
        newentry.place(x=2*dis_s+wid,y=(i+1)*dis_s+i*hei,width=entry_wid,height=hei)
        input_dict[i]=newentry.get()
    #提交按钮
    handin_button=tk.Button(sub_window_1,text='提交数据',fg='white',bg='yellow')#,command=single_datasubmit_command)
    handin_button.place(x=SUBWID-wid-dis_l,y=SUBHEI-hei-dis_l,width=wid,height=hei)
    #子菜单2-模块1-函数1：提交数据按钮模块
    def single_datasubmit_command():
        #sub_window_1.destroy
        #print(newentry.get())
        for i in range(4):
            
            print(input_dict[i])
    handin_button.config(command=single_datasubmit_command)

#主界面2-数据表格：显示输入数据功能
def dataform_function():
    #表格的列、列标题list
    form_column=['col1','col2','col3','col4','col5','col6','col7','col8']
    formcolumn_text=['进口温度(℃)','出口温度(℃)','热容(J/K)','流量(kg/s)','冷公用工程','热公用工程','公用工程热容','公用工程用量']
    #创建表格并声明要创建的列
    dataform=ttk.Treeview(window,columns=form_column)
    dataform.place(x=10*dis_l,y=10*dis_l,width=FORMWID,height=FORMHEI)
    #表格的xy轴滚动条
    xscroll=tk.Scrollbar(dataform,orient='horizontal',command=dataform.xview)
    yscroll=tk.Scrollbar(dataform,orient='vertical',command=dataform.yview)
    xscroll.pack(side='bottom',fill='x')
    yscroll.pack(side='right',fill='y')
    #在dataform上绑定xy轴滚动命令
    ''' 由于使用变量前需要先声明,因此不能在前面创建dataform时直接绑定xy轴滚动命令 '''
    dataform.config(xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
    #设置列宽、列名
    for i in range(8):
        dataform.column(form_column[i],width=entry_wid)
        dataform.heading(form_column[i],text=formcolumn_text[i])

##主函数
def my_GUI():
    mainmenu_function()
    dataform_function()
    dataout_button=tk.Button(window,text='输出数据',fg='white',bg='red',command=window.destroy)
    dataout_button.place(x=WIDTH-wid-dis_l,y=HEIGHT-hei-dis_l,width=wid,height=hei)

##主函数调用、主窗口维持
my_GUI()
window.mainloop()