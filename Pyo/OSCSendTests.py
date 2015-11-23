from pyo import *
s = Server().boot()
s.setMidiInputDevice(4) # enter your device number (see pm_list_devices())

class Controller:
    def __init__(self):
        self.port = 23415
        
        self.r1 = Midictl(ctlnumber=0, minscale=0, maxscale=1)
        self.r2 = Midictl(ctlnumber=1, minscale=0, maxscale=1)
        self.r3 = Midictl(ctlnumber=2, minscale=0, maxscale=1)
        self.r4 = Midictl(ctlnumber=3, minscale=0, maxscale=1)
        self.r5 = Midictl(ctlnumber=4, minscale=0, maxscale=1)
        self.r6 = Midictl(ctlnumber=5, minscale=0, maxscale=1)
        self.r7 = Midictl(ctlnumber=6, minscale=0, maxscale=1)
        self.r8 = Midictl(ctlnumber=7, minscale=0, maxscale=1)
        self.r9 = Midictl(ctlnumber=8, minscale=0, maxscale=1)

        self.s1 = Midictl(ctlnumber=9, minscale=0, maxscale=1)
        self.s2 = Midictl(ctlnumber=10, minscale=0, maxscale=1)
        self.s3 = Midictl(ctlnumber=11, minscale=0, maxscale=1)
        self.s4 = Midictl(ctlnumber=12, minscale=0, maxscale=1)
        self.s5 = Midictl(ctlnumber=13, minscale=0, maxscale=1)
        self.s6 = Midictl(ctlnumber=14, minscale=0, maxscale=1)
        self.s7 = Midictl(ctlnumber=15, minscale=0, maxscale=1)
        self.s8 = Midictl(ctlnumber=16, minscale=0, maxscale=1)
        self.s9 = Midictl(ctlnumber=17, minscale=0, maxscale=1)
        
        self.knobs = [self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7, self.r8, self.r9] 
        self.sliders = [self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, self.s7, self.s8, self.s9] 
        
        self.oldKnobs = [self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7, self.r8, self.r9] 
        self.oldSliders = [self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, self.s7, self.s8, self.s9] 

    def CheckValues(self):
        
        for (i, item) in enumerate(self.knobs):
            
            if self.knobs[i] != self.oldKnobs[i]:
                self.send = OscDataSend("f", self.port, "/controller/knobs/r{0}".format(str(i)))

cont = Controller()

# Send various types
a = OscDataSend("s", 23415, "/data/test")
msg = ["jaime mes amis"]
a.send(msg)

s.gui(locals())