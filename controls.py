import sys
sys.path.append(".")

from valve import Valve
from light import Light

class Controls:
    def __init__(self, settings) -> None:
        self.valves = settings.valves
        self.lights = settings.lights
    
    def startTimers(self):
        for valve in self.valves:
            valve.on = True
            valve.startStopwatch()
        
        for light in self.lights:
            light.on = True
            light.stopwatchOn()
    
    def stopTimers(self):
        for valve in self.valves:
            valve.on = False

        for light in self.lights:
            light.on = False
    
    
    
    def addValve(self):
        self.valves.append(Valve(self.numiter))
        self.valvenumiter += 1

    def modifyValve(self, num, hours, minutes, pour_time):
        self.valves[num].setTime(hours, minutes, pour_time)

    def readValveData(self):
        print("Valve Saved Time Settings:")
        for s in self.valves:
            s.readData()
    
    def addLight(self):
        self.lights.append(Light(self.numiter))
        self.lightnumiter += 1
    
    def modifyLight(self, num, hours_on, minutes_on, hours_off, minutes_off):
        self.lights[num].setTime(self, hours_on, minutes_on, hours_off, minutes_off)
