#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 19, 2018 09:44:58 AM

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

import addbooks5_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    addbooks5_support.set_Tk_var()
    top = ADD_BOOK (root)
    addbooks5_support.init(root, top)
    root.mainloop()

w = None
def create_ADD_BOOK(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    addbooks5_support.set_Tk_var()
    top = ADD_BOOK (w)
    addbooks5_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_ADD_BOOK():
    global w
    w.destroy()
    w = None


class ADD_BOOK:
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

        top.geometry("600x386+661+217")
        top.title("ADD BOOK")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.15, rely=0.1, relheight=0.03, relwidth=0.0)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=-7)

        self.Canvas2 = Canvas(top)
        self.Canvas2.place(relx=0.1, rely=0.21, relheight=0.71, relwidth=0.77)
        self.Canvas2.configure(background="#d9d9d9")
        self.Canvas2.configure(borderwidth="2")
        self.Canvas2.configure(highlightbackground="#d9d9d9")
        self.Canvas2.configure(highlightcolor="black")
        self.Canvas2.configure(insertbackground="black")
        self.Canvas2.configure(relief=RIDGE)
        self.Canvas2.configure(selectbackground="#c4c4c4")
        self.Canvas2.configure(selectforeground="black")
        self.Canvas2.configure(width=463)

        self.Label2 = Label(self.Canvas2)
        self.Label2.place(relx=0.13, rely=0.15, height=34, width=49)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Title''')

        self.titleentry = Entry(self.Canvas2)
        self.titleentry.place(relx=0.32, rely=0.15,height=26, relwidth=0.57)
        self.titleentry.configure(background="white")
        self.titleentry.configure(disabledforeground="#a3a3a3")
        self.titleentry.configure(font="TkFixedFont")
        self.titleentry.configure(foreground="#000000")
        self.titleentry.configure(highlightbackground="#d9d9d9")
        self.titleentry.configure(highlightcolor="black")
        self.titleentry.configure(insertbackground="black")
        self.titleentry.configure(selectbackground="#c4c4c4")
        self.titleentry.configure(selectforeground="black")
        self.titleentry.configure(textvariable=addbooks5_support.title)

        self.Label3 = Label(self.Canvas2)
        self.Label3.place(relx=0.11, rely=0.37, height=34, width=76)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Subject''')

        self.subbutton = Entry(self.Canvas2)
        self.subbutton.place(relx=0.32, rely=0.37,height=26, relwidth=0.57)
        self.subbutton.configure(background="white")
        self.subbutton.configure(disabledforeground="#a3a3a3")
        self.subbutton.configure(font="TkFixedFont")
        self.subbutton.configure(foreground="#000000")
        self.subbutton.configure(highlightbackground="#d9d9d9")
        self.subbutton.configure(highlightcolor="black")
        self.subbutton.configure(insertbackground="black")
        self.subbutton.configure(selectbackground="#c4c4c4")
        self.subbutton.configure(selectforeground="black")
        self.subbutton.configure(textvariable=addbooks5_support.sub)

        self.Label4 = Label(self.Canvas2)
        self.Label4.place(relx=0.13, rely=0.59, height=34, width=72)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font10)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Author''')

        self.authorbutton = Entry(self.Canvas2)
        self.authorbutton.place(relx=0.32, rely=0.59,height=26, relwidth=0.57)
        self.authorbutton.configure(background="white")
        self.authorbutton.configure(disabledforeground="#a3a3a3")
        self.authorbutton.configure(font="TkFixedFont")
        self.authorbutton.configure(foreground="#000000")
        self.authorbutton.configure(highlightbackground="#d9d9d9")
        self.authorbutton.configure(highlightcolor="black")
        self.authorbutton.configure(insertbackground="black")
        self.authorbutton.configure(selectbackground="#c4c4c4")
        self.authorbutton.configure(selectforeground="black")
        self.authorbutton.configure(textvariable=addbooks5_support.auth)

        self.esubmitbutton = Button(self.Canvas2)
        self.esubmitbutton.place(relx=0.06, rely=0.81, height=42, width=108)
        self.esubmitbutton.configure(activebackground="#d9d9d9")
        self.esubmitbutton.configure(activeforeground="#000000")
        self.esubmitbutton.configure(background="#d9d9d9")
        self.esubmitbutton.configure(command=addbooks5_support.esubmitfunction)
        self.esubmitbutton.configure(disabledforeground="#a3a3a3")
        self.esubmitbutton.configure(foreground="#000000")
        self.esubmitbutton.configure(highlightbackground="#d9d9d9")
        self.esubmitbutton.configure(highlightcolor="black")
        self.esubmitbutton.configure(pady="0")
        self.esubmitbutton.configure(text='''Submit''')

        self.eclearbutton = Button(self.Canvas2)
        self.eclearbutton.place(relx=0.39, rely=0.81, height=42, width=108)
        self.eclearbutton.configure(activebackground="#d9d9d9")
        self.eclearbutton.configure(activeforeground="#000000")
        self.eclearbutton.configure(background="#d9d9d9")
        self.eclearbutton.configure(command=addbooks5_support.eclearfunction)
        self.eclearbutton.configure(disabledforeground="#a3a3a3")
        self.eclearbutton.configure(foreground="#000000")
        self.eclearbutton.configure(highlightbackground="#d9d9d9")
        self.eclearbutton.configure(highlightcolor="black")
        self.eclearbutton.configure(pady="0")
        self.eclearbutton.configure(text='''Clear''')

        self.ebackbutton = Button(self.Canvas2)
        self.ebackbutton.place(relx=0.71, rely=0.81, height=42, width=108)
        self.ebackbutton.configure(activebackground="#d9d9d9")
        self.ebackbutton.configure(activeforeground="#000000")
        self.ebackbutton.configure(background="#d9d9d9")
        self.ebackbutton.configure(command=addbooks5_support.ebackfunction)
        self.ebackbutton.configure(disabledforeground="#a3a3a3")
        self.ebackbutton.configure(foreground="#000000")
        self.ebackbutton.configure(highlightbackground="#d9d9d9")
        self.ebackbutton.configure(highlightcolor="black")
        self.ebackbutton.configure(pady="0")
        self.ebackbutton.configure(text='''Back''')

        self.Label1 = Label(top)
        self.Label1.place(relx=0.25, rely=0.05, height=31, width=313)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''ADD BOOK INFO''')

        self.eaddlogoutbutton = Button(top)
        self.eaddlogoutbutton.place(relx=0.88, rely=0.0, height=42, width=78)
        self.eaddlogoutbutton.configure(activebackground="#d9d9d9")
        self.eaddlogoutbutton.configure(activeforeground="#000000")
        self.eaddlogoutbutton.configure(background="#d9d9d9")
        self.eaddlogoutbutton.configure(command=addbooks5_support.eaddlogoutfunction)
        self.eaddlogoutbutton.configure(disabledforeground="#a3a3a3")
        self.eaddlogoutbutton.configure(foreground="#000000")
        self.eaddlogoutbutton.configure(highlightbackground="#d9d9d9")
        self.eaddlogoutbutton.configure(highlightcolor="black")
        self.eaddlogoutbutton.configure(pady="0")
        self.eaddlogoutbutton.configure(text='''logout''')






if __name__ == '__main__':
    vp_start_gui()


