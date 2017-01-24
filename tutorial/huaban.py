#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# author :insun
#http://yxmhero1989.blog.163.com/blog/static/112157956201311994027168/
import urllib, urllib2, re, sys, os

import tkinter as tk
from tkinter import ttk
reload(sys)

toEnd = False

if(os.path.exists('beauty') == False):
    os.mkdir('beauty')

def get_huaban_beauty(pid):
    if pid is None or pid == '':
        print 'none id'
        return
    pin_id = ''
    board_id = pid
    if(os.path.exists('beauty/'+board_id) == False):
        os.mkdir('beauty/'+board_id)
    maxid = ''
    limit = 20 #他默认允许的limit为100
    while board_id != None:
        # url = 'http://huaban.com/boards/31435061/?max=' + str(pin_id) + '&limit=' + str(limit) + '&wfl=1'
        url = 'http://huaban.com/boards/'+board_id+'/?max='+maxid+'&limit=' + str(limit) + '&wfl=1'
        try:
            i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
                         "Connection":"keep-alive",
                         "Referer":"http://huaban.com/boards/31435061/",
                         "Host":"huaban.com",
                         "Connection":"keep-alive",
                         "Accept":"application/json"
                         }
            req = urllib2.Request(url, headers=i_headers)
            html = urllib2.urlopen(req).read()
            # print html
            # reg = re.compile('"pin_id":(.*?),.+?"file":{"farm":"farm1", "bucket":"hbimg",.+?"key":"(.*?)",.+?"type":"image/(.*?)"', re.S)
            reg = re.compile('"pin_id":(.*?),.+?"file":\{"id":.+?"key":(.*?),.+?"type":"image\/(.*?)"', re.S)
            groups = re.findall(reg, html)
            print(len(groups))
            if len(groups) <= 0 :
                print('没有图片！')
                return
            maxid = groups[len(groups)-1][0]
            for att in groups:
                pin_id = att[0]
                att_url = att[1][1:-1]
                # print att_url
                img_type = att[2]
                img_url = 'http://img.hb.aicdn.com/' + att_url
                # print(img_url)
                if(urllib.urlretrieve(img_url, 'beauty/'+board_id+'/'+att_url+'.'+img_type)):
                    print img_url + ' download success!'
                else:
                    print img_url + '.' + img_type + ' save failed'
            if toEnd is True:
                toEnd = False
                return
            # return
        except:
            print 'error occurs'

######################################GUI界面开始
win = tk.Tk()
win.title("Python GUI")    # 添加标题
aLabel = ttk.Label(win, text="A Label")     # 创建一个标签, text：显示表现的内容
aLabel.grid(column=0, row=0)

def clickMe():   # 当acction被点击时,该函数则生效
    action.configure(text='Hello ' + name.get())     # 设置button显示的内容
    print(name.get())
    get_huaban_beauty(name.get())

action = ttk.Button(win, text="Click Me!", command=clickMe)     # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.grid(column=1, row=1)

ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()     # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
nameEntered = ttk.Entry(win, width=12, textvariable=name)   # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
nameEntered.grid(column=0, row=1)

win.mainloop()      # 当调用mainloop()时,窗口才会显示出来

# mainRun()

