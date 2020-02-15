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
    [sg.Text('Dir:', size=(15, 1), auto_size_text=False, justification='right'),      
     sg.InputText(executer_dir, key='dir', size=(80,1)), sg.FolderBrowse()],    
    [sg.InputCombo(('vs13','224', '25', '7'), default_value='vs13', size=(20, 3)), sg.Checkbox('check1'), sg.Checkbox('check2', default=True)],           
    [sg.Multiline(default_text='Console', size=(120, 12), key='console')],      
    [],       
    [sg.Text('_'  * 80)],
    [sg.Button('Go'),sg.Exit()]
        
]

form = sg.FlexForm("Change Combo Values", default_element_size=(12,1), text_justification='r', auto_size_text=False, 
                    auto_size_buttons=False, default_button_element_size=(12,1))
log_file=open("executer.log","r")
log_str=""
for line in log_file:
    log_str+=line
window = sg.Window('Everything bagel', default_element_size=(40, 1)).Layout(layout)
window.refresh
while True:                             # The Event Loop
    event, values = window.read() 
    # print(event, values)
    logging.info("Go clicked...")
    logging.debug(log_str)
    window.FindElement('console').Update(log_str)
    executer_dir=values['dir']
    logging.debug("executer_dir="+executer_dir)     
    if event in (None, 'Exit'):      
        break      
# sg.Popup(button, values)