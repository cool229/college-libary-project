#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 19, 2018 09:44:52 AM


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
    global title
    title = StringVar()
    global sub
    sub = StringVar()
    global auth
    auth = StringVar()

def eaddlogoutfunction():
    print('addbooks5_support.eaddlogoutfunction')
    sys.stdout.flush()

def ebackfunction():
    print('addbooks5_support.ebackfunction')
    sys.stdout.flush()

def eclearfunction():
    print('addbooks5_support.eclearfunction')
    sys.stdout.flush()

def esubmitfunction():
    print('addbooks5_support.esubmitfunction')
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
    import addbooks5
    addbooks5.vp_start_gui()


