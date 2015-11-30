from pyo import *

class Controller:
    def __init__(self):
        self.port = 23415

        # Liste des adresses possibles
        self.addresses = ["/controller/{0}".format(str(i)) for i in range(18)]
        # On cree OscDataSend une seule fois        
        self.oscsender = OscDataSend("f", self.port, self.addresses)
        
        self.knobs = [Midictl(ctlnumber=i, minscale=0, maxscale=1) for i in range(18)]

        # Appelle la fonction qui envoit le message
        self.tf = [TrigFunc(Change(self.knobs[i]), function=self.send, arg=i) for i in range(18)]
        
        #print les messages
        self.debug = False 
        
        [self.send(i) for i in range(18)]

        
    def send(self, which):
        self.value = self.knobs[which].get()
        self.oscsender.send([self.value], self.addresses[which])
        
        if(self.debug == True):
            print "{0}: {1}".format(str(self.addresses[which]), str(self.knobs[which].get()))
        
    def play(self):
        # Appelle la fonction qui envoit le message
        self.tf = [TrigFunc(Change(self.knobs[i]), function=self.send, arg=i) for i in range(18)]