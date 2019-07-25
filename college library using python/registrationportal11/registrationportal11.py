#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 18, 2018 05:59:00 PM

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

import registrationportal11_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    registrationportal11_support.set_Tk_var()
    top = Registrationportal (root)
    registrationportal11_support.init(root, top)
    root.mainloop()

w = None
def create_Registrationportal(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    registrationportal11_support.set_Tk_var()
    top = Registrationportal (w)
    registrationportal11_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Registrationportal():
    global w
    w.destroy()
    w = None


class Registrationportal:
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

        top.geometry("857x568+650+150")
        top.title("Registrationportal")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.07, rely=0.14, relheight=0.8, relwidth=0.86)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=733)

        self.nameentry = Entry(self.Canvas1)
        self.nameentry.place(relx=0.35, rely=0.09,height=26, relwidth=0.5)
        self.nameentry.configure(background="white")
        self.nameentry.configure(disabledforeground="#a3a3a3")
        self.nameentry.configure(font="TkFixedFont")
        self.nameentry.configure(foreground="#000000")
        self.nameentry.configure(highlightbackground="#d9d9d9")
        self.nameentry.configure(highlightcolor="black")
        self.nameentry.configure(insertbackground="black")
        self.nameentry.configure(selectbackground="#c4c4c4")
        self.nameentry.configure(selectforeground="black")
        self.nameentry.configure(textvariable=registrationportal11_support.sname)

        self.Label2 = Label(self.Canvas1)
        self.Label2.place(relx=0.14, rely=0.09, height=34, width=72)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Name''')

        self.Label3 = Label(self.Canvas1)
        self.Label3.place(relx=0.14, rely=0.22, height=34, width=77)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Roll No''')

        self.rollentry = Entry(self.Canvas1)
        self.rollentry.place(relx=0.35, rely=0.22,height=26, relwidth=0.5)
        self.rollentry.configure(background="white")
        self.rollentry.configure(disabledforeground="#a3a3a3")
        self.rollentry.configure(font="TkFixedFont")
        self.rollentry.configure(foreground="#000000")
        self.rollentry.configure(highlightbackground="#d9d9d9")
        self.rollentry.configure(highlightcolor="black")
        self.rollentry.configure(insertbackground="black")
        self.rollentry.configure(selectbackground="#c4c4c4")
        self.rollentry.configure(selectforeground="black")
        self.rollentry.configure(textvariable=registrationportal11_support.sroll)

        self.Label4 = Label(self.Canvas1)
        self.Label4.place(relx=0.12, rely=0.35, height=34, width=120)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Department''')

        self.deptentry = Entry(self.Canvas1)
        self.deptentry.place(relx=0.35, rely=0.35,height=26, relwidth=0.5)
        self.deptentry.configure(background="white")
        self.deptentry.configure(disabledforeground="#a3a3a3")
        self.deptentry.configure(font="TkFixedFont")
        self.deptentry.configure(foreground="#000000")
        self.deptentry.configure(highlightbackground="#d9d9d9")
        self.deptentry.configure(highlightcolor="black")
        self.deptentry.configure(insertbackground="black")
        self.deptentry.configure(selectbackground="#c4c4c4")
        self.deptentry.configure(selectforeground="black")
        self.deptentry.configure(textvariable=registrationportal11_support.sdept)

        self.Label5 = Label(self.Canvas1)
        self.Label5.place(relx=0.14, rely=0.49, height=34, width=103)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font9)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Semester''')

        self.semesterentry = Entry(self.Canvas1)
        self.semesterentry.place(relx=0.35, rely=0.49,height=26, relwidth=0.5)
        self.semesterentry.configure(background="white")
        self.semesterentry.configure(disabledforeground="#a3a3a3")
        self.semesterentry.configure(font="TkFixedFont")
        self.semesterentry.configure(foreground="#000000")
        self.semesterentry.configure(highlightbackground="#d9d9d9")
        self.semesterentry.configure(highlightcolor="black")
        self.semesterentry.configure(insertbackground="black")
        self.semesterentry.configure(selectbackground="#c4c4c4")
        self.semesterentry.configure(selectforeground="black")
        self.semesterentry.configure(textvariable=registrationportal11_support.ssem)

        self.batchentry = Entry(self.Canvas1)
        self.batchentry.place(relx=0.35, rely=0.62,height=26, relwidth=0.5)
        self.batchentry.configure(background="white")
        self.batchentry.configure(disabledforeground="#a3a3a3")
        self.batchentry.configure(font="TkFixedFont")
        self.batchentry.configure(foreground="#000000")
        self.batchentry.configure(highlightbackground="#d9d9d9")
        self.batchentry.configure(highlightcolor="black")
        self.batchentry.configure(insertbackground="black")
        self.batchentry.configure(selectbackground="#c4c4c4")
        self.batchentry.configure(selectforeground="black")
        self.batchentry.configure(textvariable=registrationportal11_support.sbatch)

        self.Label6 = Label(self.Canvas1)
        self.Label6.place(relx=0.16, rely=0.62, height=34, width=60)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font9)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Batch''')

        self.Label7 = Label(self.Canvas1)
        self.Label7.place(relx=0.15, rely=0.75, height=34, width=95)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font9)
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Password''')

        self.passwordentry = Entry(self.Canvas1)
        self.passwordentry.place(relx=0.35, rely=0.75,height=26, relwidth=0.5)
        self.passwordentry.configure(background="white")
        self.passwordentry.configure(disabledforeground="#a3a3a3")
        self.passwordentry.configure(font="TkFixedFont")
        self.passwordentry.configure(foreground="#000000")
        self.passwordentry.configure(highlightbackground="#d9d9d9")
        self.passwordentry.configure(highlightcolor="black")
        self.passwordentry.configure(insertbackground="black")
        self.passwordentry.configure(selectbackground="#c4c4c4")
        self.passwordentry.configure(selectforeground="black")
        self.passwordentry.configure(show="*")
        self.passwordentry.configure(textvariable=registrationportal11_support.spassword)

        self.submitbutton = Button(self.Canvas1)
        self.submitbutton.place(relx=0.1, rely=0.88, height=42, width=138)
        self.submitbutton.configure(activebackground="#d9d9d9")
        self.submitbutton.configure(activeforeground="#000000")
        self.submitbutton.configure(background="#d9d9d9")
        self.submitbutton.configure(command=registrationportal11_support.submitfunction)
        self.submitbutton.configure(disabledforeground="#a3a3a3")
        self.submitbutton.configure(foreground="#000000")
        self.submitbutton.configure(highlightbackground="#d9d9d9")
        self.submitbutton.configure(highlightcolor="black")
        self.submitbutton.configure(pady="0")
        self.submitbutton.configure(text='''Submit''')

        self.clearbutton = Button(self.Canvas1)
        self.clearbutton.place(relx=0.42, rely=0.88, height=42, width=138)
        self.clearbutton.configure(activebackground="#d9d9d9")
        self.clearbutton.configure(activeforeground="#000000")
        self.clearbutton.configure(background="#d9d9d9")
        self.clearbutton.configure(command=registrationportal11_support.clearfunction)
        self.clearbutton.configure(disabledforeground="#a3a3a3")
        self.clearbutton.configure(foreground="#000000")
        self.clearbutton.configure(highlightbackground="#d9d9d9")
        self.clearbutton.configure(highlightcolor="black")
        self.clearbutton.configure(pady="0")
        self.clearbutton.configure(text='''Clear''')

        self.backbutton = Button(self.Canvas1)
        self.backbutton.place(relx=0.74, rely=0.88, height=42, width=138)
        self.backbutton.configure(activebackground="#d9d9d9")
        self.backbutton.configure(activeforeground="#000000")
        self.backbutton.configure(background="#d9d9d9")
        self.backbutton.configure(command=registrationportal11_support.backfunction)
        self.backbutton.configure(disabledforeground="#a3a3a3")
        self.backbutton.configure(foreground="#000000")
        self.backbutton.configure(highlightbackground="#d9d9d9")
        self.backbutton.configure(highlightcolor="black")
        self.backbutton.configure(pady="0")
        self.backbutton.configure(text='''Back''')

        self.Label1 = Label(top)
        self.Label1.place(relx=0.18, rely=0.05, height=31, width=517)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''REGISTRATION PORTAL''')






if __name__ == '__main__':
    vp_start_gui()


