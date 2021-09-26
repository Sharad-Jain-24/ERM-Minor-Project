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
    
#code to make organizer taskss
def mgm_page():
    #GUI for organizer management
    screen3.withdraw()
    global screen4
    screen4 = Toplevel(screen3)
    screen4.title("Select")        
    screen4.geometry("140x128")
    screen4.resizable(False, False)
    screen4.config(background="green")    
    btn = Button(screen4, width=13, text="QR Generator", command=QRP)
    btn.grid(row=1, column=1, padx=5, pady=5, columnspan=1)
    bnt = Button(screen4, width=13, text="QR Scanner", command=QRScan)
    bnt.grid(row=2, column=1, padx=5, pady=5, columnspan=1)
    tbn = Button(screen4, width=13, text="Event Management", command=eventmgm)
    tbn.grid(row=3, column=1, padx=5, pady=5, columnspan=1)

    #code to monitor app close event
    def on_closing(event):
        screen2.destroy()
    screen4.protocol("WM_DELETE_WINDOW", on_closing)
    screen4.bind('<Escape>', on_closing)
    
def main_page():
    global username_verify, password_verify, username1, password1        
    
    #code for organizer details verification
    def login_verify():
        screen2.withdraw()
        global screen3        
        screen3 = Toplevel(screen2)
        screen3.geometry("150x30")        

        #code to monitor app close event
        def on_closing(event):
            clrlogin()
            screen2.deiconify()    
            screen3.destroy()        
        screen3.protocol("WM_DELETE_WINDOW", on_closing)
        screen3.bind('<Escape>', on_closing)
        
        username1 = username_verify.get()
        password1 = password_verify.get()
        list_of_dir = os.listdir()
        if username1 in list_of_dir:
            file = open (username1, "r")
            verify = file.read().splitlines()
            if (password1 and "Admin") in verify:
                screen3.title("Info")
                screen3.geometry("250x115")
                label = Label(screen3, text="Login Success", width='30')
                label.grid(row=1, column=1, padx=5, pady=5, columnspan=1)
                bttn = Button(screen3, text="OK", width="10", command=clrlogin)
                bttn.grid(row=2, column=1, padx=5, pady=5, columnspan=1)
                bttn = Button(screen3, text="Add Organizer", width="10", command=register)
                bttn.grid(row=3, column=1, padx=5, pady=5, columnspan=1)
            elif password1 in verify:
                screen3.title("Info")
                screen3.geometry("250x75")
                label = Label(screen3, text="Login Success", width='30')
                label.grid(row=1, column=1, padx=5, pady=5, columnspan=1)
                bttn = Button(screen3, text="OK", width="10", command=clrlogin)
                bttn.grid(row=2, column=1, padx=5, pady=5, columnspan=1)
            else:
                screen3.title("Alert")
                label = Label(screen3, text="Incorrect Password", width='17')
                label.grid(row=1, column=0, columnspan=1)                
        else :
            screen3.title("Alert")
            label = Label(screen3, text="Invalid User", width='17')
            label.grid(row=1, column=0, columnspan=1)
    
    #code to organizer management
    def register_user():
        #code to monitor app close event
        def on_closing(event):
            screen2.deiconify()    
            screen1.destroy()
        screen1.protocol("WM_DELETE_WINDOW", on_closing)
        screen1.bind('<Escape>', on_closing)
        
        #code to disable GUI fields for organizer management
        def disab():
            screen1.geometry("300x80")
            labl.grid_forget()
            username_entry.grid_forget()
            password_entry.grid_forget()
            buutn.grid_forget()
            
        def reab():
            register()                   

        #code for GUI of organizer registration success
        """
        sharad please optimize organizer registration & 
        login technique as you see fit.
        """

        #check if password is strong
        if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password.get()):
            username_info = username.get()
            password_info = password.get()
            file = open(username_info, "w")
            file.write(username_info+"\n")
            file.write(password_info)
            file.close()
            disab()
            label = Label(screen1, text="Registeration Success", font ="green", width='30')
            label.grid(row=1, column=1, columnspan=1)
            bttn = Button(screen1, text="OK", width="15", command=on_closing)
            bttn.grid(row=2, column=1, columnspan=1)
        else:
            disab()
            label = Label(screen1, text="Use Strong Password", font ="green", width='30')
            label.grid(row=1, column=1, columnspan=1)
            bttn = Button(screen1, text="OK", width="15", command=reab)
            bttn.grid(row=2, column=1, columnspan=1)

    #code for organizer adding GUI
    def register():
        global screen1
        screen1 = Toplevel(screen2)
        screen1.geometry("250x200")
        screen1.title("Register")
        screen2.withdraw()
        screen3.withdraw()
        global labl
        global buutn
        global username
        global password
        global username_entry
        global password_entry
        username = StringVar()
        password = StringVar()
        labl = Label(screen1, text="Please enter user information", width="30")
        labl.grid(row=1, column=1, padx=5, pady=5, columnspan=1)
        labl = Label(screen1, text="Username", width='30')
        labl.grid(row=2, column=1, padx=5, pady=5, columnspan=1)
        username_entry = Entry(screen1, textvariable=username)
        username_entry.grid(row=3, column=1, padx=5, pady=5, columnspan=1)
        username_entry.focus_set()
        labl = Label(screen1, text="Password", width='30')
        labl.grid(row=4, column=1, padx=5, pady=5, columnspan=1)
        password_entry = Entry(screen1, show="*", textvariable=password)
        password_entry.grid(row=5, column=1, padx=5, pady=5, columnspan=1)
        buutn = Button(screen1, text="Sumbit", width='18', command=register_user)
        buutn.grid(row=6, column=1, padx=5, pady=5, columnspan=1)
        screen1.bind('<Return>', lambda event=None: buutn.invoke())

        #code to monitor app close event
        def on_closing(event):
            clrlogin()
            screen2.deiconify()    
            screen1.destroy()
        screen1.protocol("WM_DELETE_WINDOW", on_closing)
        screen1.bind('<Escape>', on_closing)

    #code to clear login data fields after successful login
    def clrlogin():
        username_entry1.focus_set()
        username_verify.set("")
        password_verify.set("")
        mgm_page()

    #code for organizer login GUI
    def login():
        global screen2, username_verify, password_verify, username_entry1
        screen2 = Tk()
        screen2.geometry("255x200")
        screen2.title("Login")
        username_verify = StringVar()
        password_verify = StringVar()    
        label = Label(text="Please enter your login information", width='30')
        label.grid(row=1, column=1, padx=5, pady=5, columnspan=1)
        label = Label(text="Username : ", width='30')
        label.grid(row=2, column=1, padx=5, pady=5, columnspan=1)
        username_entry1 = Entry(width="30", textvariable=username_verify)
        username_entry1.grid(row=3, column=1, padx=5, pady=5, columnspan=1)
        username_entry1.focus_set()        
        label = Label(text="Password : ", width='30')
        label.grid(row=4, column=1, padx=5, pady=5, columnspan=1)
        password_entry1 = Entry(width='30', show="*", textvariable=password_verify)
        password_entry1.grid(row=5, column=1, padx=5, pady=5, columnspan=1)
        btnn = Button(text="Login", width="18", command=login_verify)
        btnn.grid(row=6, column=1, padx=5, pady=5, columnspan=1)        
        screen2.bind('<Return>', lambda event=None: btnn.invoke())
        
        #monitor app close
        def on_closing(event):
            sys.exit()
        screen2.bind('<Escape>', on_closing)
        
        screen2.mainloop()

    login()

main_page()

