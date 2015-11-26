from pyo import *
s = Server().boot()
s.setMidiInputDevice(4) # enter your device number (see pm_list_devices())

class Controller:
    def __init__(self):
        self.port = 23415

        # Liste des adresses possibles
        self.addresses = ["/controller/knobs/ctl{0}".format(str(i)) for i in range(20)]
        # On cree OscDataSend une seule fois        
        self.oscsender = OscDataSend("f", self.port, self.addresses)
        
        self.knobs = [Midictl(ctlnumber=i+1, minscale=0, maxscale=1) for i in range(18)]

        # Appelle la fonction qui envoit le message
        self.tf = [TrigFunc(Change(self.knobs[i]), function=self.send, arg=0) for i in range(18)]
        
    def send(self, which):
        self.value = self.knobs[which].get()
        self.oscsender.send([self.value], self.addresses[which])

cont = Controller()

# Send various types
a = OscDataSend("s", 23415, "/data/test")
msg = ["jaime mes amis"]
a.send(msg)

s.gui(locals())