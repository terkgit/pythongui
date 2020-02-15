import PySimpleGUI as sg
import os
import logging

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)

executer_dir=os.getcwd()
logging.debug("executer_dir="+executer_dir)

sg.ChangeLookAndFeel('TealMono')

column1 = [[sg.Text('Column 1', background_color='#d3dfda', justification='center', size=(10, 1))],      
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],      
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],      
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]      
layout = [      
    [sg.Text('GUI for CLI execution', size=(30, 1), font=("Helvetica", 25))],      
    [sg.Text('Working Directory', size=(15, 1), auto_size_text=False, justification='right'),      
     sg.InputText(executer_dir, key='dir'), sg.FolderBrowse()],      
    [sg.Text('Here is some text.... and a place to enter text')],      
    [sg.InputText('This is my text')],      
    [sg.Checkbox('My first checkbox!'), sg.Checkbox('My second checkbox!', default=True)],      
    [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],      
    [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3))],      
    [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 3))],       
    [sg.Text('_'  * 80)],
    [sg.Button('Go'),sg.Exit()]
        
]

form = sg.FlexForm("Change Combo Values", default_element_size=(12,1), text_justification='r', auto_size_text=False, 
                    auto_size_buttons=False, default_button_element_size=(12,1))

window = sg.Window('Everything bagel', default_element_size=(40, 1)).Layout(layout)
while True:                             # The Event Loop
    event, values = window.read() 
    # print(event, values)
    logging.info("Go clicked...")
    executer_dir=values['dir']
    logging.debug("executer_dir="+executer_dir)     
    if event in (None, 'Exit'):      
        break      
# sg.Popup(button, values)