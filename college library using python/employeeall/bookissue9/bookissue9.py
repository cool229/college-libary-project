#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 18, 2018 07:34:38 PM

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

import bookissue9_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    bookissue9_support.set_Tk_var()
    top = Book_issue_details (root)
    bookissue9_support.init(root, top)
    root.mainloop()

w = None
def create_Book_issue_details(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    bookissue9_support.set_Tk_var()
    top = Book_issue_details (w)
    bookissue9_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Book_issue_details():
    global w
    w.destroy()
    w = None


class Book_issue_details:
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

        top.geometry("538x345+678+150")
        top.title("Book issue details")
        top.configure(background="#d9d9d9")



        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.11, rely=0.2, relheight=0.73, relwidth=0.8)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=433)

        self.Label2 = Label(self.Canvas1)
        self.Label2.place(relx=0.09, rely=0.16, height=34, width=82)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Roll No.''')

        self.srollentry = Entry(self.Canvas1)
        self.srollentry.place(relx=0.35, rely=0.16,height=26, relwidth=0.59)
        self.srollentry.configure(background="white")
        self.srollentry.configure(disabledforeground="#a3a3a3")
        self.srollentry.configure(font="TkFixedFont")
        self.srollentry.configure(foreground="#000000")
        self.srollentry.configure(insertbackground="black")
        self.srollentry.configure(textvariable=bookissue9_support.sroll)
        self.srollentry.configure(width=254)

        self.Label3 = Label(self.Canvas1)
        self.Label3.place(relx=0.14, rely=0.4, height=34, width=50)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''BID''')
        self.Label3.configure(width=50)

        self.bidentry = Entry(self.Canvas1)
        self.bidentry.place(relx=0.35, rely=0.4,height=26, relwidth=0.59)
        self.bidentry.configure(background="white")
        self.bidentry.configure(disabledforeground="#a3a3a3")
        self.bidentry.configure(font="TkFixedFont")
        self.bidentry.configure(foreground="#000000")
        self.bidentry.configure(insertbackground="black")
        self.bidentry.configure(textvariable=bookissue9_support.bid)
        self.bidentry.configure(width=254)

        self.esubmitbutton = Button(self.Canvas1)
        self.esubmitbutton.place(relx=0.14, rely=0.71, height=42, width=128)
        self.esubmitbutton.configure(activebackground="#d9d9d9")
        self.esubmitbutton.configure(activeforeground="#000000")
        self.esubmitbutton.configure(background="#d9d9d9")
        self.esubmitbutton.configure(command=bookissue9_support.esubmitfunction)
        self.esubmitbutton.configure(disabledforeground="#a3a3a3")
        self.esubmitbutton.configure(foreground="#000000")
        self.esubmitbutton.configure(highlightbackground="#d9d9d9")
        self.esubmitbutton.configure(highlightcolor="black")
        self.esubmitbutton.configure(pady="0")
        self.esubmitbutton.configure(text='''Submit''')
        self.esubmitbutton.configure(width=128)

        self.ebackbutton = Button(self.Canvas1)
        self.ebackbutton.place(relx=0.6, rely=0.71, height=42, width=128)
        self.ebackbutton.configure(activebackground="#d9d9d9")
        self.ebackbutton.configure(activeforeground="#000000")
        self.ebackbutton.configure(background="#d9d9d9")
        self.ebackbutton.configure(command=bookissue9_support.ebackfunction)
        self.ebackbutton.configure(disabledforeground="#a3a3a3")
        self.ebackbutton.configure(foreground="#000000")
        self.ebackbutton.configure(highlightbackground="#d9d9d9")
        self.ebackbutton.configure(highlightcolor="black")
        self.ebackbutton.configure(pady="0")
        self.ebackbutton.configure(text='''Back''')
        self.ebackbutton.configure(width=128)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.26, rely=0.06, height=31, width=257)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Book Issue table''')
        self.Label1.configure(width=257)

        self.elogoutbutton = Button(top)
        self.elogoutbutton.place(relx=0.87, rely=0.0, height=42, width=68)
        self.elogoutbutton.configure(activebackground="#d9d9d9")
        self.elogoutbutton.configure(activeforeground="#000000")
        self.elogoutbutton.configure(background="#d9d9d9")
        self.elogoutbutton.configure(command=bookissue9_support.elogoutfunction)
        self.elogoutbutton.configure(disabledforeground="#a3a3a3")
        self.elogoutbutton.configure(foreground="#000000")
        self.elogoutbutton.configure(highlightbackground="#d9d9d9")
        self.elogoutbutton.configure(highlightcolor="black")
        self.elogoutbutton.configure(pady="0")
        self.elogoutbutton.configure(text='''logout''')






if __name__ == '__main__':
    vp_start_gui()


