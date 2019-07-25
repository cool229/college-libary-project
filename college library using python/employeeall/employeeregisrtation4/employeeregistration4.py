#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 18, 2018 08:19:42 PM

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

import employeeregistration4_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    employeeregistration4_support.set_Tk_var()
    top = New_Employee_Registration (root)
    employeeregistration4_support.init(root, top)
    root.mainloop()

w = None
def create_New_Employee_Registration(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    employeeregistration4_support.set_Tk_var()
    top = New_Employee_Registration (w)
    employeeregistration4_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Employee_Registration():
    global w
    w.destroy()
    w = None


class New_Employee_Registration:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 14 -weight bold -slant "  \
            "italic -underline 1 -overstrike 0"
        font9 = "-family {Segoe UI} -size 10 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("787x581+621+177")
        top.title("New Employee Registration")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.13, rely=0.15, relheight=0.76, relwidth=0.74)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=583)

        self.Label2 = Label(self.Canvas1)
        self.Label2.place(relx=0.14, rely=0.23, height=34, width=73)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Emp.ID''')

        self.enameentryentry = Entry(self.Canvas1)
        self.enameentryentry.place(relx=0.34, rely=0.11, height=26
                , relwidth=0.52)
        self.enameentryentry.configure(background="white")
        self.enameentryentry.configure(disabledforeground="#a3a3a3")
        self.enameentryentry.configure(font="TkFixedFont")
        self.enameentryentry.configure(foreground="#000000")
        self.enameentryentry.configure(highlightbackground="#d9d9d9")
        self.enameentryentry.configure(highlightcolor="black")
        self.enameentryentry.configure(insertbackground="black")
        self.enameentryentry.configure(selectbackground="#c4c4c4")
        self.enameentryentry.configure(selectforeground="black")
        self.enameentryentry.configure(textvariable=employeeregistration4_support.ename)

        self.Label3 = Label(self.Canvas1)
        self.Label3.place(relx=0.12, rely=0.34, height=34, width=95)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Password''')

        self.empidentry = Entry(self.Canvas1)
        self.empidentry.place(relx=0.34, rely=0.23,height=26, relwidth=0.52)
        self.empidentry.configure(background="white")
        self.empidentry.configure(disabledforeground="#a3a3a3")
        self.empidentry.configure(font="TkFixedFont")
        self.empidentry.configure(foreground="#000000")
        self.empidentry.configure(highlightbackground="#d9d9d9")
        self.empidentry.configure(highlightcolor="black")
        self.empidentry.configure(insertbackground="black")
        self.empidentry.configure(selectbackground="#c4c4c4")
        self.empidentry.configure(selectforeground="black")
        self.empidentry.configure(textvariable=employeeregistration4_support.empid)

        self.Label4 = Label(self.Canvas1)
        self.Label4.place(relx=0.14, rely=0.11, height=34, width=62)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Name''')

        self.epasswordentry = Entry(self.Canvas1)
        self.epasswordentry.place(relx=0.34, rely=0.34, height=26, relwidth=0.52)

        self.epasswordentry.configure(background="white")
        self.epasswordentry.configure(disabledforeground="#a3a3a3")
        self.epasswordentry.configure(font="TkFixedFont")
        self.epasswordentry.configure(foreground="#000000")
        self.epasswordentry.configure(highlightbackground="#d9d9d9")
        self.epasswordentry.configure(highlightcolor="black")
        self.epasswordentry.configure(insertbackground="black")
        self.epasswordentry.configure(selectbackground="#c4c4c4")
        self.epasswordentry.configure(selectforeground="black")
        self.epasswordentry.configure(show="*")
        self.epasswordentry.configure(textvariable=employeeregistration4_support.epassword)

        self.Label5 = Label(self.Canvas1)
        self.Label5.place(relx=0.1, rely=0.45, height=34, width=120)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font9)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Department''')

        self.edeptentry = Entry(self.Canvas1)
        self.edeptentry.place(relx=0.34, rely=0.45,height=26, relwidth=0.52)
        self.edeptentry.configure(background="white")
        self.edeptentry.configure(disabledforeground="#a3a3a3")
        self.edeptentry.configure(font="TkFixedFont")
        self.edeptentry.configure(foreground="#000000")
        self.edeptentry.configure(highlightbackground="#d9d9d9")
        self.edeptentry.configure(highlightcolor="black")
        self.edeptentry.configure(insertbackground="black")
        self.edeptentry.configure(selectbackground="#c4c4c4")
        self.edeptentry.configure(selectforeground="black")
        self.edeptentry.configure(textvariable=employeeregistration4_support.edept)

        self.Label6 = Label(self.Canvas1)
        self.Label6.place(relx=0.14, rely=0.56, height=31, width=57)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font9)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''D.O.J''')

        self.edojentry = Entry(self.Canvas1)
        self.edojentry.place(relx=0.34, rely=0.56,height=26, relwidth=0.52)
        self.edojentry.configure(background="white")
        self.edojentry.configure(disabledforeground="#a3a3a3")
        self.edojentry.configure(font="TkFixedFont")
        self.edojentry.configure(foreground="#000000")
        self.edojentry.configure(highlightbackground="#d9d9d9")
        self.edojentry.configure(highlightcolor="black")
        self.edojentry.configure(insertbackground="black")
        self.edojentry.configure(selectbackground="#c4c4c4")
        self.edojentry.configure(selectforeground="black")
        self.edojentry.configure(textvariable=employeeregistration4_support.edoj)

        self.Label7 = Label(self.Canvas1)
        self.Label7.place(relx=0.14, rely=0.68, height=34, width=64)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font9)
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Salary''')

        self.esalaryentry = Entry(self.Canvas1)
        self.esalaryentry.place(relx=0.34, rely=0.68,height=26, relwidth=0.52)
        self.esalaryentry.configure(background="white")
        self.esalaryentry.configure(disabledforeground="#a3a3a3")
        self.esalaryentry.configure(font="TkFixedFont")
        self.esalaryentry.configure(foreground="#000000")
        self.esalaryentry.configure(highlightbackground="#d9d9d9")
        self.esalaryentry.configure(highlightcolor="black")
        self.esalaryentry.configure(insertbackground="black")
        self.esalaryentry.configure(selectbackground="#c4c4c4")
        self.esalaryentry.configure(selectforeground="black")
        self.esalaryentry.configure(textvariable=employeeregistration4_support.esalary)

        self.esubmitbutton = Button(self.Canvas1)
        self.esubmitbutton.place(relx=0.1, rely=0.84, height=42, width=102)
        self.esubmitbutton.configure(activebackground="#d9d9d9")
        self.esubmitbutton.configure(activeforeground="#000000")
        self.esubmitbutton.configure(background="#d9d9d9")
        self.esubmitbutton.configure(command=employeeregistration4_support.esubmitfunction)
        self.esubmitbutton.configure(disabledforeground="#a3a3a3")
        self.esubmitbutton.configure(foreground="#000000")
        self.esubmitbutton.configure(highlightbackground="#d9d9d9")
        self.esubmitbutton.configure(highlightcolor="black")
        self.esubmitbutton.configure(pady="0")
        self.esubmitbutton.configure(text='''Submit''')

        self.eclearbutton = Button(self.Canvas1)
        self.eclearbutton.place(relx=0.41, rely=0.84, height=42, width=108)
        self.eclearbutton.configure(activebackground="#d9d9d9")
        self.eclearbutton.configure(activeforeground="#000000")
        self.eclearbutton.configure(background="#d9d9d9")
        self.eclearbutton.configure(command=employeeregistration4_support.eclearfunction)
        self.eclearbutton.configure(disabledforeground="#a3a3a3")
        self.eclearbutton.configure(foreground="#000000")
        self.eclearbutton.configure(highlightbackground="#d9d9d9")
        self.eclearbutton.configure(highlightcolor="black")
        self.eclearbutton.configure(pady="0")
        self.eclearbutton.configure(text='''Clear''')

        self.ebackbutton = Button(self.Canvas1)
        self.ebackbutton.place(relx=0.7, rely=0.84, height=42, width=108)
        self.ebackbutton.configure(activebackground="#d9d9d9")
        self.ebackbutton.configure(activeforeground="#000000")
        self.ebackbutton.configure(background="#d9d9d9")
        self.ebackbutton.configure(command=employeeregistration4_support.ebackfunction)
        self.ebackbutton.configure(disabledforeground="#a3a3a3")
        self.ebackbutton.configure(foreground="#000000")
        self.ebackbutton.configure(highlightbackground="#d9d9d9")
        self.ebackbutton.configure(highlightcolor="black")
        self.ebackbutton.configure(pady="0")
        self.ebackbutton.configure(text='''Back''')

        self.Label1 = Label(top)
        self.Label1.place(relx=0.19, rely=0.05, height=31, width=467)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''REGISTRATION PORTAL''')

        self.elogoutbutton = Button(top)
        self.elogoutbutton.place(relx=0.91, rely=0.0, height=42, width=68)
        self.elogoutbutton.configure(activebackground="#d9d9d9")
        self.elogoutbutton.configure(activeforeground="#000000")
        self.elogoutbutton.configure(background="#d9d9d9")
        self.elogoutbutton.configure(command=employeeregistration4_support.elogutfunction)
        self.elogoutbutton.configure(disabledforeground="#a3a3a3")
        self.elogoutbutton.configure(foreground="#000000")
        self.elogoutbutton.configure(highlightbackground="#d9d9d9")
        self.elogoutbutton.configure(highlightcolor="black")
        self.elogoutbutton.configure(pady="0")
        self.elogoutbutton.configure(text='''logout''')






if __name__ == '__main__':
    vp_start_gui()



