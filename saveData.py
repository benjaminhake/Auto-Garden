import pickle

#import valve
#import light

class SaveData:
    def __init__(self):
        self.valves = []
        self.valvenumiter = 0

        self.lights = []
        self.lightnumiter = 0

        self.loadData()

    def loadData(self):
        self.loadLights()
        self.loadValves()        

    def saveData(self):
        self.saveValves()
        self.saveLights()

    def saveValves(self):
        # Save Valves
        with open('valves.pl', 'wb') as iterator:
            for valve in self.valves:
                pickle.dump(valve, iterator, pickle.HIGHEST_PROTOCOL)

    def saveLights(self):
        #Save Lights
        with open('lights.pl', 'wb') as iterator:
            for light in self.lights:
                pickle.dump(light, iterator, pickle.HIGHEST_PROTOCOL)

    def loadValves(self):
        # Load Valves
        try:
            with open('valves.pkl', 'rb') as iterator:
                self.valves.append(pickle.load(iterator))
            self.valves.sort(key = lambda x: x.num, reverse = False)
            self.valvenumiter = self.valves[-1].num + 1

        except FileNotFoundError:
            pass
    
    def loadLights(self):
        # Load Lights
        try:
            with open('lights.pkl', 'rb') as iterator:
                self.lights.append(pickle.load(iterator))
            self.lights.sort(key = lambda x: x.num, reverse = False)
            self.lightnumiter = self.lights[-1].num + 1

        except FileNotFoundError:
            pass
    
    def readValveData(self):
        settings = "Valve Saved Time Settings:\n"
        for v in self.valves:
            settings += v.readData()
        return settings

    def readLightData(self):
        settings = "Light Saved Time Settings:\n"
        for l in self.lights:
            settings += l.readData()
        return settings
print("Hello")