#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 18, 2018 08:17:10 PM

import sys

try:
    from Tkinter import *
except ImportError:
    from Tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import Tkinter.ttk as ttk
    py3 = True

import employeeoption3_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root = resizable(0,0)
    top = Employee_tools (root)
    employeeoption3_support.init(root, top)
    root.mainloop()

w = None
def create_Employee_tools(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Employee_tools (w)
    employeeoption3_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Employee_tools():
    global w
    w.destroy()
    w = None


class Employee_tools:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI} -size 14 -weight bold -slant "  \
            "italic -underline 1 -overstrike 0"

        top.geometry("600x554+644+205")
        top.title("Employee tools")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.12, rely=0.07, height=31, width=447)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''SELECT OPTIONS''')

        self.eneweregbutton = Button(top)
        self.eneweregbutton.place(relx=0.28, rely=0.2, height=42, width=248)
        self.eneweregbutton.configure(activebackground="#d9d9d9")
        self.eneweregbutton.configure(activeforeground="#000000")
        self.eneweregbutton.configure(background="#d9d9d9")
        self.eneweregbutton.configure(command=employeeoption3_support.eneweregfunction)
        self.eneweregbutton.configure(disabledforeground="#a3a3a3")
        self.eneweregbutton.configure(foreground="#000000")
        self.eneweregbutton.configure(highlightbackground="#d9d9d9")
        self.eneweregbutton.configure(highlightcolor="black")
        self.eneweregbutton.configure(pady="0")
        self.eneweregbutton.configure(text='''NEW REGISTRATION''')

        self.addbookbutton = Button(top)
        self.addbookbutton.place(relx=0.28, rely=0.31, height=42, width=248)
        self.addbookbutton.configure(activebackground="#d9d9d9")
        self.addbookbutton.configure(activeforeground="#000000")
        self.addbookbutton.configure(background="#d9d9d9")
        self.addbookbutton.configure(command=employeeoption3_support.addbookfunction)
        self.addbookbutton.configure(disabledforeground="#a3a3a3")
        self.addbookbutton.configure(foreground="#000000")
        self.addbookbutton.configure(highlightbackground="#d9d9d9")
        self.addbookbutton.configure(highlightcolor="black")
        self.addbookbutton.configure(pady="0")
        self.addbookbutton.configure(text='''ADD BOOK''')

        self.delbookbutton = Button(top)
        self.delbookbutton.place(relx=0.28, rely=0.42, height=42, width=248)
        self.delbookbutton.configure(activebackground="#d9d9d9")
        self.delbookbutton.configure(activeforeground="#000000")
        self.delbookbutton.configure(background="#d9d9d9")
        self.delbookbutton.configure(command=employeeoption3_support.delbookfunction)
        self.delbookbutton.configure(disabledforeground="#a3a3a3")
        self.delbookbutton.configure(foreground="#000000")
        self.delbookbutton.configure(highlightbackground="#d9d9d9")
        self.delbookbutton.configure(highlightcolor="black")
        self.delbookbutton.configure(pady="0")
        self.delbookbutton.configure(text='''DELETE BOOK''')

        self.allbookbutton = Button(top)
        self.allbookbutton.place(relx=0.28, rely=0.52, height=42, width=248)
        self.allbookbutton.configure(activebackground="#d9d9d9")
        self.allbookbutton.configure(activeforeground="#000000")
        self.allbookbutton.configure(background="#d9d9d9")
        self.allbookbutton.configure(command=employeeoption3_support.allbookfunction)
        self.allbookbutton.configure(disabledforeground="#a3a3a3")
        self.allbookbutton.configure(foreground="#000000")
        self.allbookbutton.configure(highlightbackground="#d9d9d9")
        self.allbookbutton.configure(highlightcolor="black")
        self.allbookbutton.configure(pady="0")
        self.allbookbutton.configure(text='''ALL BOOKS''')

        self.searchbookbutton = Button(top)
        self.searchbookbutton.place(relx=0.28, rely=0.63, height=42, width=248)
        self.searchbookbutton.configure(activebackground="#d9d9d9")
        self.searchbookbutton.configure(activeforeground="#000000")
        self.searchbookbutton.configure(background="#d9d9d9")
        self.searchbookbutton.configure(command=employeeoption3_support.searchbookfunction)
        self.searchbookbutton.configure(disabledforeground="#a3a3a3")
        self.searchbookbutton.configure(foreground="#000000")
        self.searchbookbutton.configure(highlightbackground="#d9d9d9")
        self.searchbookbutton.configure(highlightcolor="black")
        self.searchbookbutton.configure(pady="0")
        self.searchbookbutton.configure(text='''SEARCH BOOK''')

        self.issuedbutton = Button(top)
        self.issuedbutton.place(relx=0.28, rely=0.74, height=42, width=248)
        self.issuedbutton.configure(activebackground="#d9d9d9")
        self.issuedbutton.configure(activeforeground="#000000")
        self.issuedbutton.configure(background="#d9d9d9")
        self.issuedbutton.configure(command=employeeoption3_support.issuedfunction)
        self.issuedbutton.configure(disabledforeground="#a3a3a3")
        self.issuedbutton.configure(foreground="#000000")
        self.issuedbutton.configure(highlightbackground="#d9d9d9")
        self.issuedbutton.configure(highlightcolor="black")
        self.issuedbutton.configure(pady="0")
        self.issuedbutton.configure(text='''ISSUED DETAILS''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.Button1 = Button(top)
        self.Button1.place(relx=0.9, rely=0.0, height=42, width=68)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''logout''')






if __name__ == '__main__':
    vp_start_gui()


