"""
TODO:::
    TEST ADD FUNCTIONALITY THROUGH UI
"""

import tkinter as tk
from tkinter.constants import LEFT, WORD, Y
import sys
sys.path.append(".")
from controls import Controls
from saveData import SaveData

FRAME_WIDTH = 800
FRAME_HEIGHT = 600

class MainFrame(tk.Frame):
    def __init__(self, master=None, controls=None, saveData=None):
        super().__init__(master)
        self.master = master
        self.controls = controls
        self.saveData = saveData
        self.pack()
        self.openMainScreen()
        
        
    def openMainScreen(self):
        self.destroyWidgets()

        self.startButton = tk.Button(self,
                                    text="Start Timers",
                                    command=self.controls.startTimers,
                                    padx = 100,
                                    pady=10).pack(pady=20)

        self.stopButton = tk.Button(self,
                                    text="Stop Timers",
                                    command=self.controls.stopTimers,
                                    padx=100,
                                    pady=10).pack(pady=20)

        self.controlsButton = tk.Button(self,
                                        text="Controls",
                                        command=self.openControlsScreen,
                                        padx=100,
                                        pady=10).pack(pady=50)
    
    def openControlsScreen(self):
        self.destroyWidgets()

        self.showValvesButton = tk.Button(  self,
                                            text="Valve Settings",
                                            command=self.openValvesScreen,
                                            padx = 100,
                                            pady=10).pack(pady=20)
        
        self.showLightsButton = tk.Button(  self,
                                            text="Light Settings",
                                            command=self.openLightsScreen,
                                            padx = 100,
                                            pady=10).pack(pady=20)
    
    def openValvesScreen(self):
        self.destroyWidgets()

        infoscroll = tk.Scrollbar(self)

        self.infoText = tk.Text(         self,
                                    wrap=tk.WORD,
                                    width=15)#,
                                    #yscrollcommand=infoscroll.set)

        self.infoText.insert(tk.END, self.saveData.readValveData())
        self.infoText.pack(side=tk.LEFT)

        
        addValveFrame = tk.Frame(self)
        addValveFrame.pack( side=tk.LEFT,
                            padx = 15)
        addButtonLabel = tk.Label(  addValveFrame,
                                    text="Add Valve: ")
        addButtonLabel.pack(side=tk.TOP, pady=20)

        hoursFrame = tk.Frame(addValveFrame)
        hoursFrame.pack(side=tk.TOP, padx=15)
        hoursLabel = tk.Label(  hoursFrame,
                                text="Hours: ")
        hoursLabel.pack(side=tk.LEFT, padx=10)
        self.hoursEntry = tk.Entry(hoursFrame, width=2)
        self.hoursEntry.pack(side=tk.LEFT, padx=5)

        minutesFrame = tk.Frame(addValveFrame)
        minutesFrame.pack(side=tk.TOP, padx=15)
        minutesLabel = tk.Label(minutesFrame,
                                text="Minutes: ")
        minutesLabel.pack(side=tk.LEFT, padx=10)
        self.minutesEntry = tk.Entry(minutesFrame, width=2)
        self.minutesEntry.pack(side=tk.LEFT, padx=5)

        pourtimeFrame = tk.Frame(addValveFrame)
        pourtimeFrame.pack(side=tk.TOP, padx=15)
        pourtimeLabel = tk.Label(pourtimeFrame,
                                text="Seconds Per Pour: ")
        pourtimeLabel.pack(side=tk.LEFT, padx=10)
        self.pourtimeEntry = tk.Entry(pourtimeFrame, width=2)
        self.pourtimeEntry.pack(side=tk.LEFT, padx=5)

        addValveButton = tk.Button(addValveFrame,
                                    text="Add",
                                    command=self.addValveHandler)
        addValveButton.pack(side=tk.TOP, padx=15, pady=17)

        backButton = tk.Button( addValveFrame,
                                text="Back",
                                command=self.openControlsScreen)
        backButton.pack(side=tk.BOTTOM, padx = 20, pady=20 )


    def openLightsScreen(self):
        self.destroyWidgets()

        infoscroll = tk.Scrollbar(self)

        self.infoText = tk.Text(         self,
                                    wrap=tk.WORD,
                                    width=15)#,
                                    #yscrollcommand=infoscroll.set)

        self.infoText.insert(tk.END, self.saveData.readLightData())
        self.infoText.pack(side=tk.LEFT)

        
        addLightFrame = tk.Frame(self)
        addLightFrame.pack( side=tk.LEFT,
                            padx = 15)
        addButtonLabel = tk.Label(  addLightFrame,
                                    text="Add Light: ")
        addButtonLabel.pack(side=tk.TOP, pady=20)

        hoursOnFrame = tk.Frame(addLightFrame)
        hoursOnFrame.pack(side=tk.TOP, padx=15)
        hoursOnLabel = tk.Label(  hoursOnFrame,
                                text="Hours On: ")
        hoursOnLabel.pack(side=tk.LEFT, padx=10)
        self.lighthoursOnEntry = tk.Entry(hoursOnFrame, width=2)
        self.lighthoursOnEntry.focus_set()
        self.lighthoursOnEntry.pack(side=tk.LEFT, padx=5)

        minutesOnFrame = tk.Frame(addLightFrame)
        minutesOnFrame.pack(side=tk.TOP, padx=15)
        minutesOnLabel = tk.Label(minutesOnFrame,
                                text="Minutes On: ")
        minutesOnLabel.pack(side=tk.LEFT, padx=10)
        self.lightminutesOnEntry = tk.Entry(minutesOnFrame, width=2)
        self.lightminutesOnEntry.focus_set()
        self.lightminutesOnEntry.pack(side=tk.LEFT, padx=5)

        hoursOffFrame = tk.Frame(addLightFrame)
        hoursOffFrame.pack(side=tk.TOP, padx=15)
        hoursOffLabel = tk.Label(  hoursOffFrame,
                                text="Hours Off: ")
        hoursOffLabel.pack(side=tk.LEFT, padx=10)
        self.lighthoursOffEntry = tk.Entry(hoursOffFrame, width=2)
        self.lighthoursOffEntry.focus_set()
        self.lighthoursOffEntry.pack(side=tk.LEFT, padx=5)

        minutesOffFrame = tk.Frame(addLightFrame)
        minutesOffFrame.pack(side=tk.TOP, padx=15)
        minutesOffLabel = tk.Label(minutesOffFrame,
                                text="Minutes Off: ")
        minutesOffLabel.pack(side=tk.LEFT, padx=10)
        self.lightminutesOffEntry = tk.Entry(minutesOffFrame, width=2)
        self.lightminutesOffEntry.focus_set()
        self.lightminutesOffEntry.pack(side=tk.LEFT, padx=5)

        addLightButton = tk.Button(addLightFrame,
                                    text="Add",
                                    command=self.addLightHandler)
        addLightButton.pack(side=tk.TOP, padx=15, pady=17)

        self.errorLabel = tk.Label( addLightFrame,
                                    text="")
        self.errorLabel.pack(side=tk.LEFT, padx=10)

        backButton = tk.Button( addLightFrame,
                                text="Back",
                                command=self.openControlsScreen)
        backButton.pack(side=tk.BOTTOM, padx = 20, pady=20 )

    def addLightHandler(self):
        hourson = self.lighthoursOnEntry.get()
        minuteson = self.lightminutesOnEntry.get()
        hoursoff = self.lighthoursOffEntry.get()
        minutesoff = self.lightminutesOffEntry.get()

        if not hourson or not minuteson or not hoursoff or not minutesoff:
            self.throwError("No Null Entries. ")
        else:
            n = self.controls.lightnumiter
            self.controls.addLight()
            self.controls.modifyLight(  n,
                                        hourson,
                                        minuteson,
                                        hoursoff,
                                        minutesoff)
            self.infoText.insert(tk.END, self.controls.lights[n].readData())
            self.throwError("Light Successfully Added!")


    def addValveHandler(self):
        hours = self.hoursEntry.get()
        minutes = self.minutesEntry.get()
        pourtime = self.pourtimeEntry.get()

        if not hours or not minutes or not pourtime:
            self.throwError("No Null Entries")
        else:
            n = self.controls.lightnumiter
            self.controls.addValve()
            self.controls.modifyValve( n,
                                        hours,
                                        minutes,
                                        pourtime)
            self.infoText.insert(tk.END, self.controls.valves[n].readData())
    def destroyWidgets(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    def throwError(self, errorMessage):
        self.errorLabel.config(text=errorMessage)


                                        
print("Hello WOrld!")

root = tk.Tk()
root.geometry('800x600')
root.resizable(0, 0)
sd = SaveData()
c = Controls(sd)
m = MainFrame(root, c, sd)
root.mainloop()
