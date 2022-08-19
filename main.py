from time import sleep
from xml.etree.ElementTree import tostring
from metronome import Metronome
from tkinter import *
from tkinter import ttk
import tkinter as tk
metronome = Metronome()
metronome.start()

window=Tk()

window.title('Metronome')
windowWidth = 300
windowHeight = 400
positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)
window.geometry(f"400x300+{positionRight}+{positionDown}")
window.resizable(False, False)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.rowconfigure(3,weight=1)

def set_defaults():
    volume_control.set(100)
    bpm_control.set(120)

def handleStartStop():
    if(metronome.is_playning()):
        metronome.stop()
        play_button.config(text="PLAY")
    else:
        play_button.config(text="STOP")
        metronome.start_play()

def handleChangeVolume(volume):
    metronome.set_volume(int(volume)/100)

def handleChangeBpm(bpm):
    metronome.stop()
    play_button.config(text="PLAY")
    metronome.set_frequency(int(bpm))


def on_bar_change(index, value, op):
    var= bar_control.get()
    bar_value = str(var)[1]
    metronome.set_bar(int(bar_value))
    
    
play_button = ttk.Button(
    window,
    text='PLAY',
    command=handleStartStop
)

play_button.grid(column=1, row=0, sticky=tk.S,pady=10)


volume_control = Scale(window, from_=0, to=100, orient=HORIZONTAL,command=handleChangeVolume)
volume_control.grid(column=1,row=1)
volume_control_label = Label(window,text="Volume")
volume_control_label.grid(column=0,row=1,sticky=tk.NS)

bpm_control = Scale(window, from_=1, to=260, orient=HORIZONTAL,command=handleChangeBpm)
bpm_control.grid(column=1,row=2)
bpm_contro_label = Label(window,text="BPM")
bpm_contro_label.grid(column=0,row=2,sticky=tk.NS)

selectedBar = tk.StringVar()

selectedBar.trace('w',on_bar_change)

bar_control = ttk.Combobox(window, textvariable = selectedBar)

bar_control['values'] = (' 3/4', 
                          ' 4/4',
                          ' 5/4',
                          ' 6/4',
                          )
bar_control.current(1)

bar_control.grid(column=1,row=3)

def on_closing():
    metronome.terminate() 
    window.destroy()

set_defaults()
window.protocol("WM_DELETE_WINDOW", on_closing)


window.mainloop()