#Fried
#(c) 2023 Erik's Gadgets

import PySimpleGUI as sg #Imports GUI Library
import os 

login = os.getlogin()

sg.theme("DarkTeal12") #Sets theme

sg.Popup("Fried\n(c) 2023 Erik's Gadgets") #IP addition

room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room.png")]]).Read()
