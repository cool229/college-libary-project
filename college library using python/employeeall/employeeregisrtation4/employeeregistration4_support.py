#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 18, 2018 08:19:35 PM


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
def set_Tk_var():
    global ename
    ename = StringVar()
    global empid
    empid = StringVar()
    global epassword
    epassword = StringVar()
    global edept
    edept = StringVar()
    global edoj
    edoj = StringVar()
    global esalary
    esalary = StringVar()

def ebackfunction():
    print('employeeregistration4_support.ebackfunction')
    sys.stdout.flush()

def eclearfunction():
    print('employeeregistration4_support.eclearfunction')
    sys.stdout.flush()

def elogutfunction():
    print('employeeregistration4_support.elogutfunction')
    sys.stdout.flush()

def esubmitfunction():
    print('employeeregistration4_support.esubmitfunction')
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import employeeregistration4
    employeeregistration4.vp_start_gui()


