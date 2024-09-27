from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder 
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root=Tk()
root.title("Phone Number Tracker")
root.geometry("930x784+0+0")
root.resizable(False,False)


#icon image
icon=PhotoImage(file="Image/Phone tracker image logo.png")
root.iconphoto(False,icon)


#logo
logo=PhotoImage(file="Image/Phone tracker image logo.png")

Label(root,image=logo).place(x=300,y=10,width=400,height=400)

Eback=PhotoImage(file="Image/Search Image logo.png")
Label(root,image=Eback).place(x=100,y=280,width=700,height=200)


#heading
Heading=Label(root,text="TRACK NUMBER",font=('arial',22,'bold'))
Heading.place(x=200,y=130)

#botton box
Box=PhotoImage(file="Image/button-icon-png-21058.png")
Label(root,image=Box).place(x=10,y=530,width=900,height=350)

#entry
entry=StringVar()
enter_number=Entry(root,textvariable=entry,width=25,justify="center",bd=0,font=("arial",25))
enter_number.place(x=200,y=320)

#search botton 



root.mainloop()