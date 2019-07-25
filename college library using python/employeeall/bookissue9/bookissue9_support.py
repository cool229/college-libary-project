#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 18, 2018 07:34:30 PM


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
    global sroll
    sroll = StringVar()
    global bid
    bid = StringVar()

def ebackfunction():
    print('bookissue9_support.ebackfunction')
    sys.stdout.flush()

def elogoutfunction():
    print('bookissue9_support.elogoutfunction')
    sys.stdout.flush()

def esubmitfunction():
    print('bookissue9_support.esubmitfunction')
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
    import bookissue9
    bookissue9.vp_start_gui()


