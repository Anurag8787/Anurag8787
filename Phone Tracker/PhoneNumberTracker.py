import tkinter
from click import style
from colorama import Style
import tkintermapview
import phonenumbers 
import geocoder
import folium
import opencage

from key import key

from phonenumbers import geocoder
from phonenumbers import carrier

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from opencage.geocoder import OpenCageGeocode

root = tkinter.Tk()
root.geometry("500x500")

labal1 = Label(text="Phone Number Tracker")
labal1.pack()

def getResult():
    num = number.get("1.0", END)
    try: 
       num1 = phonenumbers.parse(num)
    except:
        messagebox.showerror("Error","Number box is empty or the input is not numeric !!")
        
    location = geocoder.description_for_number(num1,"en")
    service_provider = carrier.name_for_number(num1,"en")
  
    ocg = OpenCageGeocode(key)
    query = str(location)
    results = ocg.geocode(query)
    
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    my_labal= LabelFrame(root)
    my_labal.pack(pady=20)
    
    
    folium= tkintermapview.TkinterMapView(my_labal,width=450,height=450,corner_radius=0)
    folium.set_position(lat,lng)
    folium.set_marker(lat,lng,text="Phone Location")
    folium.set_zoom(10)
    folium.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)
    folium.pack()
    
    adr = tkintermapview.convert_coordinates_to_address(lat, lng)
    
    
    result.insert(END,"The Country of this number is:" +location)
    result.insert(END,"\nThe sim card of this number is:" +service_provider)
    
    result.insert(END,"\n Latitude is:" +str(lat))
    result.insert(END,"\n Longitude is:" +str(lng))
    
    result.insert(END,"\n Street Address is:" +adr.street)
    result.insert(END,"\n City Address is:" +adr.city)
    result.insert(END,"\n Postal Code is:" +adr.postal)

    
    

number = Text(height=1)
number.pack()

style =Style()
style.configure("TButton",font=('calibri',20,'bold'),borderwidth='4')
style.map('TButtion',foreground=[('active','!disabled','green')], 
                     background=[('active','black')])


button = Button(text="Search",command=getResult)
button.pack(pady=10,padx=100)

result=Text(height=7)
result.pack()


root.mainloop()
