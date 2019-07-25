#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 19, 2018 09:29:11 AM

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

import returnbook18_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    returnbook18_support.set_Tk_var()
    top = New_Toplevel (root)
    returnbook18_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    returnbook18_support.set_Tk_var()
    top = New_Toplevel (w)
    returnbook18_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
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

        top.geometry("606x377+644+150")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.3, rely=0.08, height=44, width=264)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''RETURN  TABLE''')
        self.Label1.configure(width=264)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.18, rely=0.29, height=34, width=77)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Roll No''')

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.36, rely=0.29,height=26, relwidth=0.42)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable=returnbook18_support.sroll)
        self.Entry1.configure(width=254)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.2, rely=0.45, height=34, width=40)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''BID''')

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.36, rely=0.45,height=26, relwidth=0.42)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(textvariable=returnbook18_support.bid)
        self.Entry2.configure(width=254)

        self.esubmitbutton = Button(top)
        self.esubmitbutton.place(relx=0.2, rely=0.66, height=42, width=118)
        self.esubmitbutton.configure(activebackground="#d9d9d9")
        self.esubmitbutton.configure(activeforeground="#000000")
        self.esubmitbutton.configure(background="#d9d9d9")
        self.esubmitbutton.configure(command=returnbook18_support.esubmitfunction)
        self.esubmitbutton.configure(disabledforeground="#a3a3a3")
        self.esubmitbutton.configure(foreground="#000000")
        self.esubmitbutton.configure(highlightbackground="#d9d9d9")
        self.esubmitbutton.configure(highlightcolor="black")
        self.esubmitbutton.configure(pady="0")
        self.esubmitbutton.configure(text='''Submit''')
        self.esubmitbutton.configure(width=118)

        self.ebackbutton = Button(top)
        self.ebackbutton.place(relx=0.61, rely=0.66, height=42, width=118)
        self.ebackbutton.configure(activebackground="#d9d9d9")
        self.ebackbutton.configure(activeforeground="#000000")
        self.ebackbutton.configure(background="#d9d9d9")
        self.ebackbutton.configure(command=returnbook18_support.ebackfunction)
        self.ebackbutton.configure(disabledforeground="#a3a3a3")
        self.ebackbutton.configure(foreground="#000000")
        self.ebackbutton.configure(highlightbackground="#d9d9d9")
        self.ebackbutton.configure(highlightcolor="black")
        self.ebackbutton.configure(pady="0")
        self.ebackbutton.configure(text='''Back''')
        self.ebackbutton.configure(width=118)

        self.elogoutbutton = Button(top)
        self.elogoutbutton.place(relx=0.89, rely=0.0, height=42, width=68)
        self.elogoutbutton.configure(activebackground="#d9d9d9")
        self.elogoutbutton.configure(activeforeground="#000000")
        self.elogoutbutton.configure(background="#d9d9d9")
        self.elogoutbutton.configure(command=returnbook18_support.elogoutfunction)
        self.elogoutbutton.configure(disabledforeground="#a3a3a3")
        self.elogoutbutton.configure(foreground="#000000")
        self.elogoutbutton.configure(highlightbackground="#d9d9d9")
        self.elogoutbutton.configure(highlightcolor="black")
        self.elogoutbutton.configure(pady="0")
        self.elogoutbutton.configure(text='''logout''')






if __name__ == '__main__':
    vp_start_gui()



