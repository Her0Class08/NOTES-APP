#import gui
#Note: this is not a preinstalled python modual
#install: pip3 install PySimpleGUI
import PySimpleGUI as sg

#loading screen setup
loading_text = sg.Text("loading...")
loading_sprite = sg.Image(filename="images/TEMP_Loading_Image.jpg", size=(75, 75))

#window setup
window = sg.Window('TO-DO APP', size=(300, 400), layout=[[sg.pin(loading_text)], [loading_sprite]],
                   element_justification='center',
                   font=("Helvetica", 20,))

#runs window
window.read()

#closes app
#window.close()