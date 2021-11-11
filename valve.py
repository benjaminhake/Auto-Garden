import time

class Valve:
    def __init__(self, num) -> None:
        self.num = num
        self.time = None
        self.hours = None
        self.minutes = None
        self.pour_time = None
        self.on = False
        
    def startStopwatch(self):
        self.start = time.time()
        elapsed = 0
        while elapsed < self.time and self.on:
            elapsed = time.time() - self.start
            #print ("loop cycle time: %f, seconds count: %02d" % (.11 , elapsed))
            time.sleep(5)
        if self.on:
            self.startPour()
    
    def startPour(self):
        self.start = time.time()
        elapsed = 0
        while elapsed < self.pour_time and self.on:
            elapsed = time.time() - self.start
            #print ("loop cycle time: %f, seconds count: %02d" % (.11 , elapsed))
            time.sleep(1)
        if self.on:
            self.startStopwatch()

    def setTime(self, hours, minutes, pour_time):
        self.hours = hours
        self.minutes = minutes
        self.time = (minutes * 60) + (hours * 60 * 60)
        self.pour_time = pour_time
    
    def readData(self):
        if self.time is None:
            return "\tValve %d: No Time Alotted.\n".format(self.num)
        else:
            return "\tValve %d: \n\t\tTime Between Pours:\n\t\t%d Hours and %d Minutes.\n\t\tPour Time:\n\t\t%d Seconds.".format(self.num, self.hours, self.minutes, self.time)