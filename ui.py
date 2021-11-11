import tkinter as tk
from tkinter.constants import LEFT, WORD, Y
import sys
sys.path.append(".")
from controls import Controls
from saveData import SaveData

class MainFrame(tk.Frame):
    def __init__(self, master=None, controls=None, saveData=None):
        super().__init__(master, width=1600, height=900)
        self.master = master
        self.controls = controls
        self.saveData = saveData
        self.width = 1600
        self.height = 900
        self.pack()
        self.init()
        
        
    def mainScreen(self):
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
        self.pack_forget()

        self.showValvesButton = tk.Button(self,
                                    text="Valve Settings",
                                    command=self.openValvesScreen,
                                    padx = 100,
                                    pady=10).pack(pady=20)
        
        self.showLightsButton = tk.Button(self,
                                    text="Light Settings",
                                    command=self.openLightsScreen,
                                    padx = 100,
                                    pady=10).pack(pady=20)
    
    def openValvesScreen(self):
        self.pack_forget()

        self.infoText = tk.Text(self, wrap=WORD)
        self.infoText.insert('end', self.saveData.readValveData())

        self.sb = tk.Scrollbar(self, command=self.infoText.yview)
        self.sb.pack(side=LEFT, fill=Y)

        self.addButtonLabel = tk.Label(self,
                                        text="Add Button: ")
    
    def openLightsScreen(self):
        pass



class settingsMainFrame(tk.Frame):
    def __init__(self, master=None, controls=None, saveData=None):
        super().__init__(master)
        self.master = master
        self.controls = controls
        self.saveData = saveData
        self.init()
        self.pack()

    def init(self):
        self.showValvesButton = tk.Button(self,
                                    text="Valve Settings",
                                    command=self.controls.startTimers,
                                    padx = 100,
                                    pady=10).pack(pady=20)
        
        self.showLightsButton = tk.Button(self,
                                    text="Light Settings",
                                    command=self.controls.startTimers,
                                    padx = 100,
                                    pady=10).pack(pady=20)

    def openValves(self):
        newroot = tk.Tk()
        newroot.geometry('800x600')
        newroot.resizable(0, 0)
        _ = ValveSettingsFrame(newroot, self.controls, self.saveData)
        self.master.destroy()

    def openLights(self):
        pass

class ValveSettingsFrame(tk.Frame):
    def __init__(self, master=None, controls=None, saveData=None):
        super().__init__(master)
        self.master = master
        self.controls = controls
        self.saveData = saveData
        self.init()
        self.pack()
    
    def init(self):
        self.infoText = tk.Text(self, wrap=WORD)
        self.infoText.insert('end', self.saveData.readValveData())

        self.sb = tk.Scrollbar(self, command=self.infoText.yview)
        self.sb.pack(side=LEFT, fill=Y)

        self.addButtonLabel = tk.Label(self,
                                        text="Add Button: ")
                                        
print("Hello WOrld!")

root = tk.Tk()
root.geometry('800x600')
root.resizable(0, 0)
sd = SaveData()
c = Controls(sd)
m = MainFrame(root, c, sd)
root.mainloop()
