import os
import re 
def QRGen():
    import QR
def QRScan():
    import QRS    
import cv2
import time
import pyqrcode
import numpy as np
import tkinter as tk
import pyzbar.pyzbar as pyzbar
from tkinter import *
from PIL import ImageTk, Image
from openpyxl.styles import colors
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, Color, PatternFill
from openpyxl.styles.colors import *
#from tkinter import messagebox

def mgm_page():
    global root
    root = Tk()
    root.title("Select")        
    root.geometry("140x85")
    root.resizable(False, False)
    root.config(background="green")    
    btn = Button(root, width=13, text="QR Generator", pady=5, command=QRGen)
    btn.grid(row=1, column=1, padx=5, pady=5, columnspan=1)
    bnt = Button(root, width=13, text="QR Scanner", pady=5, command=QRScan)
    bnt.grid(row=2, column=1, padx=5, pady=5, columnspan=1)
    
def main_page():
    def register_user():
        username_info = username.get()
        password_info = password.get()
        file = open(username_info,"w")
        file.write(username_info+"\n")
        file.write(password_info)
        file.close()
        label = Label(screen1, text="Registeration Success", font ="green", width='30')
        label.grid(row=1, column=1, columnspan=1)

    def register():
        global screen1
        screen1 = Toplevel(screen)
        screen1.geometry("250x200")
        screen1.title("Register")
        global username 
        global password
        global username_entry
        global password_entry
        username = StringVar()
        password = StringVar()
        label = Label(screen1, text="Please enter your information", width="30")
        label.grid(row=1, column=1, padx=5, pady=5, columnspan=1)
        label = Label(screen1, text="Username", width='30')
        label.grid(row=2, column=1, padx=5, pady=5, columnspan=1)
        username_entry = Entry(screen1, textvariable=username)
        username_entry.grid(row=3, column=1, padx=5, pady=5, columnspan=1)
        label = Label(screen1, text="Password", width='30')
        label.grid(row=4, column=1, padx=5, pady=5, columnspan=1)
        password_entry = Entry(screen1, show="*", textvariable=password)
        password_entry.grid(row=5, column=1, padx=5, pady=5, columnspan=1)
        buutn = Button(screen1, text="Sumbit", width='18', command=register_user)
        buutn.grid(row=6, column=1, padx=5, pady=5, columnspan=1)

    def login():
        global screen2
        global username_verify
        global password_verify
        username_verify = StringVar()
        password_verify = StringVar()
        screen2 = Toplevel(screen)
        screen2.geometry("255x200")
        screen2.title("Login")
        label = Label(screen2, text="Please enter your login information", width='30')
        label.grid(row=1, column=1, padx=5, pady=5, columnspan=1)
        label = Label(screen2, text="Username : ", width='30')
        label.grid(row=2, column=1, padx=5, pady=5, columnspan=1)
        username_entry1 = Entry(screen2, width="30", textvariable=username_verify)
        username_entry1.grid(row=3, column=1, padx=5, pady=5, columnspan=1)
        label = Label(screen2, text="Password : ", width='30')
        label.grid(row=4, column=1, padx=5, pady=5, columnspan=1)
        password_entry1 = Entry(screen2, width='30', show="*", textvariable=password_verify)
        password_entry1.grid(row=5, column=1, padx=5, pady=5, columnspan=1)
        btnn = Button(screen2, text="Login", width="18", command=login_verify)
        btnn.grid(row=6, column=1, padx=5, pady=5, columnspan=1)

    def login_verify():
        global screen3
        screen3 = Toplevel(screen)
        screen3.geometry("150x30")
        username1 = username_verify.get()
        password1 = password_verify.get()
        list_of_dir = os.listdir()
        if username1 in list_of_dir:
            file = open (username1, "r")
            verify = file.read().splitlines()
            if password1 in verify:
                screen3.title("Info")
                screen3.geometry("250x75")
                label = Label(screen3, text="Login Success", width='30')
                label.grid(row=1, column=1, padx=5, pady=5, columnspan=1)
                bttn = Button(screen3, text="OK", width="10", command=mgm_page)
                bttn.grid(row=2, column=1, padx=5, pady=5, columnspan=1)
            else:
                screen3.title("Alert")
                Label(screen3, text="Incorrect Password", height='1', width='30', pady=5).pack()

        else :
            screen3.title("Alert")
            label = Label(screen3, text="Invalid User", width='17')
            label.grid(row=1, column=0, columnspan=1)

    def acc_screen():
        global screen
        screen = Tk()
        screen.title("Event Management")
        screen.geometry("280x150")
        label = Label(text="Sign Up if you are new User, \n Login if existing User.", width='30')
        label.grid(row=0, column=1, padx=5, pady=5)                
        btun = Button(text="Login ", width='30', command=login)
        btun.grid(row=1, column=1, padx=5, pady=5)
        butn = Button(text="Register", width='30', command=register)
        butn.grid(row=3, column=1, padx=5, pady=5)
        screen.mainloop()
        
    acc_screen()

main_page()

