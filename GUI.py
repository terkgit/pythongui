import PySimpleGUI as sg
import os

mytext = 'my text...'

# All the stuff inside your window. 
layout = [  [sg.Button('Build Lib')], 
            [sg.Button('Build Test Lib')], 
            [sg.Button('Build Test App')], 
            [sg.Button('Exit')],
            [sg.Text(mytext)] ]
# Create the Window
window = sg.Window('MyGUI', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:             
    event, values = window.read()
    if event in (None, 'Exit'):  
        break
    if event in (None, 'Build Lib'):   
        os.system("echo building lib...")
        os.system("date /t > mylib.a")
        mytext = 'done'
        os.system("echo done")
    if event in (None, 'Build Test Lib'):   
        os.system("echo building lib...")
        os.system("echo fail")
    if event in (None, 'Build Test App'):   
        print(values)
    

window.close()
