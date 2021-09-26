#importing libraries & modules
import os
import re 
import cv2
import time
import pyqrcode
import numpy as np
import tkinter as tk
import pyzbar.pyzbar as pyzbar
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from openpyxl.styles import colors
from openpyxl.styles.colors import *
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, Color, PatternFill

#path for excel file
path = "./data/regdata.xlsx"               

#code to maintain event list
"""
sharad please decide how you want this function to work
"""
def eventmgm():
    global values, txt
    values = []

    #code to make changes to events
    def QREventlist():
        #code to add events
        def addevent():
            if (addeventname.get() != ""):
                if (addeventname.get() not in values):
                    values.append(addeventname.get())
                    txt.insert(tk.END, values)
                    print(values)
                else:
                    print("already present")
            else:
                print(values)
            addeventname.set("")                                

        #code to remove events
        def remevent():
            if (reeventname.get() != ""):
                if (reeventname.get() in values):
                    values.remove(reeventname.get())
                    txt.delete(reeventname.get())
                    txt.update()
                    print(values)
                else:
                    print("not present")
            else:
                print(values)
            reeventname.set("")              
                    
        #code to clear GUI fields                    
        def clrevent():
            addeventname.set("")    
            reeventname.set("")              

        #code to create event management GUI
        screen4.withdraw()
        global screen5
        screen5 = Toplevel(screen4)
        screen5.title("Event List")
        screen5.geometry("340x160")
        screen5.config(background="green") 
        label = Label(screen5, text="Existing Events", width='17', bg='green')
        label.grid(row=1, column=1, padx=5, pady=5, columnspan=1)
        
        """
        #view event names as drop down
        cmbx = ttk.Combobox(screen5, width='17', textvariable=eventval, state="readonly")
        cmbx['values'] = values
        cmbx.grid(row=1, column=2, padx=5, pady=5, columnspan=1)
        """
        
        #view event names as list
        txt = Text(screen5, width=20, height=1, state="readonly")
        txt.grid(row=1, column=2, padx=5, pady=5, columnspan=1)
        
        adevent = Entry(screen5, width='17', textvariable=addeventname)
        adevent.grid(row=2, column=1, padx=5, pady=5, columnspan=1)
        btn = Button(screen5, width=13, text="Add Event", command=addevent)
        btn.grid(row=2, column=2, padx=5, pady=5, columnspan=1)
        reevent = Entry(screen5, width='17', textvariable=reeventname)
        reevent.grid(row=3, column=1, padx=5, pady=5, columnspan=1)
        bnt = Button(screen5, width=13, text="Remove Event", command=remevent)
        bnt.grid(row=3, column=2, padx=5, pady=5, columnspan=1)
        nbt = Button(screen5, width=26, text="Clear", command=clrevent)
        nbt.grid(row=4, column=1, padx=5, pady=5, columnspan=2)        

        #code to monitor app close event
        def on_closing(event):
            screen4.deiconify()    
            screen5.destroy()
        screen5.protocol("WM_DELETE_WINDOW", on_closing)
        screen5.bind('<Escape>', on_closing)

    #code to initialze GUI varaiables
    eventval = StringVar()
    addeventname = StringVar()
    addevent = StringVar()
    reeventname = StringVar()
    remevent = StringVar()
    QREventlist()        

eventmgm()

