#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 18, 2018 05:55:10 PM


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

def logoutfunction():
    print('optionportal13_support.logoutfunction')
    sys.stdout.flush()

def searchbooksfunction():
    print('optionportal13_support.searchbooksfunction')
    sys.stdout.flush()

def viewbookslistfunction():
    print('optionportal13_support.viewbookslistfunction')
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
    import optionportal13
    optionportal13.vp_start_gui()

