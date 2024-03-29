#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 18, 2018 08:34:05 PM

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import searching14_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    searching14_support.set_Tk_var()
    top = Searching_Block (root)
    searching14_support.init(root, top)
    root.mainloop()

w = None
def create_Searching_Block(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    searching14_support.set_Tk_var()
    top = Searching_Block (w)
    searching14_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Searching_Block():
    global w
    w.destroy()
    w = None


class Searching_Block:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 14 -weight bold -slant "  \
            "italic -underline 1 -overstrike 0"

        top.geometry("600x338+650+150")
        top.title("Searching Block")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.12, rely=0.15, height=41, width=447)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''SEARCHING PORTAL''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.13, rely=0.44, height=34, width=76)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Subject''')

        self.subjectentry = Entry(top)
        self.subjectentry.place(relx=0.35, rely=0.44,height=26, relwidth=0.46)
        self.subjectentry.configure(background="white")
        self.subjectentry.configure(disabledforeground="#a3a3a3")
        self.subjectentry.configure(font="TkFixedFont")
        self.subjectentry.configure(foreground="#000000")
        self.subjectentry.configure(highlightbackground="#d9d9d9")
        self.subjectentry.configure(highlightcolor="black")
        self.subjectentry.configure(insertbackground="black")
        self.subjectentry.configure(selectbackground="#c4c4c4")
        self.subjectentry.configure(selectforeground="black")
        self.subjectentry.configure(textvariable=searching14_support.ssub)

        self.ssearchbutton = Button(top)
        self.ssearchbutton.place(relx=0.15, rely=0.71, height=42, width=98)
        self.ssearchbutton.configure(activebackground="#d9d9d9")
        self.ssearchbutton.configure(activeforeground="#000000")
        self.ssearchbutton.configure(background="#d9d9d9")
        self.ssearchbutton.configure(command=searching14_support.searchfunction)
        self.ssearchbutton.configure(disabledforeground="#a3a3a3")
        self.ssearchbutton.configure(foreground="#000000")
        self.ssearchbutton.configure(highlightbackground="#d9d9d9")
        self.ssearchbutton.configure(highlightcolor="black")
        self.ssearchbutton.configure(pady="0")
        self.ssearchbutton.configure(text='''Search''')

        self.sclearbutton = Button(top)
        self.sclearbutton.place(relx=0.42, rely=0.71, height=42, width=98)
        self.sclearbutton.configure(activebackground="#d9d9d9")
        self.sclearbutton.configure(activeforeground="#000000")
        self.sclearbutton.configure(background="#d9d9d9")
        self.sclearbutton.configure(command=searching14_support.sclearfunction)
        self.sclearbutton.configure(disabledforeground="#a3a3a3")
        self.sclearbutton.configure(foreground="#000000")
        self.sclearbutton.configure(highlightbackground="#d9d9d9")
        self.sclearbutton.configure(highlightcolor="black")
        self.sclearbutton.configure(pady="0")
        self.sclearbutton.configure(text='''Clear''')

        self.sbackbutton = Button(top)
        self.sbackbutton.place(relx=0.7, rely=0.71, height=42, width=98)
        self.sbackbutton.configure(activebackground="#d9d9d9")
        self.sbackbutton.configure(activeforeground="#000000")
        self.sbackbutton.configure(background="#d9d9d9")
        self.sbackbutton.configure(command=searching14_support.sbackfunction)
        self.sbackbutton.configure(disabledforeground="#a3a3a3")
        self.sbackbutton.configure(foreground="#000000")
        self.sbackbutton.configure(highlightbackground="#d9d9d9")
        self.sbackbutton.configure(highlightcolor="black")
        self.sbackbutton.configure(pady="0")
        self.sbackbutton.configure(text='''Back''')

        self.slogoutbutton = Button(top)
        self.slogoutbutton.place(relx=0.87, rely=0.0, height=42, width=78)
        self.slogoutbutton.configure(activebackground="#d9d9d9")
        self.slogoutbutton.configure(activeforeground="#000000")
        self.slogoutbutton.configure(background="#d9d9d9")
        self.slogoutbutton.configure(command=searching14_support.slogoutfunction)
        self.slogoutbutton.configure(disabledforeground="#a3a3a3")
        self.slogoutbutton.configure(foreground="#000000")
        self.slogoutbutton.configure(highlightbackground="#d9d9d9")
        self.slogoutbutton.configure(highlightcolor="black")
        self.slogoutbutton.configure(pady="0")
        self.slogoutbutton.configure(text='''logout''')






if __name__ == '__main__':
    vp_start_gui()



