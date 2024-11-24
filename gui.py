from FreeSimpleGUI import Window

import functions
import FreeSimpleGUI as sg
label =sg.Text("Type in a TO-Do")
input_box= sg.InputText(tooltip="Enter a todo")
add_button= sg.Button("Add")

window: Window=sg.Window('My To-Do App', layout=[[label, input_box, add_button]])
window.read()
window.close()