import time

class Light:
    def __init__(self, num) -> None:
        self.num = num

        self.time_on = None
        self.hours_on = None
        self.minutes_on = None

        self.time_off = None
        self.hours_off = None
        self.minutes_off = None

        # Manually toggles whether a component is on or off
        self.on = False
        
    def stopwatchOn(self):
        if self.time_on is None:
            return
        self.start = time.time()
        elapsed = 0
        while elapsed < self.time_on and self.on:
            elapsed = time.time() - self.start
            print ("loop cycle time: %f, seconds count: %02d" % (time.clock(), elapsed))
            time.sleep(5)
        if self.on:
            self.stopwatchOff()
    
    def stopwatchOff(self):
        self.start = time.time()
        elapsed = 0
        while elapsed < self.time_off and self.on:
            elapsed = time.time() - self.start
            #print ("loop cycle time: %f, seconds count: %02d" % (time.clock(), elapsed))
            time.sleep(5)
        if self.on:
            self.stopwatchOn()

    def setTime(self, hours_on, minutes_on, hours_off, minutes_off):
        self.hours_on = hours_on
        self.minutes_on = minutes_on
        self.time_on = (minutes_on * 60) + (hours_on * 60 * 60)

        self.hours_off = hours_off
        self.minutes_off = minutes_off
        self.time_off = (minutes_off * 60) + (hours_off * 60 * 60)
    
    def readData(self):
        if self.time is None:
            print("\tLight %d:" % self.num)
            print("\t\tNo Time Alotted.\n")
        else:
            print("\tLight %d: \n\t\tOn: \n\t\t%d Hours and %d Minutes.\n\t\tOff: \n\t\t%d Hours and %d Minutes.\n" % (self.num, self.hours_on, self.minutes_on, self.hours_off, self.minutes_off))
