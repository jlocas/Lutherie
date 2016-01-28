from pyo import *

class Controller:
    def __init__(self, config):
        self.port = 23415

        self.config = config
        #print les messages
        self.debug = False 
        
        # Liste des adresses possibles
        self.addresses = ["/controller/{0}".format(str(i)) for i in range(18)]
        # On cree OscDataSend une seule fois        
        self.oscsender = OscDataSend("f", self.port, self.addresses)
        
        if config == 0:
            self.ctls = [Midictl(ctlnumber=i, minscale=0, maxscale=1) for i in range(18)]
            # Appelle la fonction qui envoit le message
            self.tf = [TrigFunc(Change(self.ctls[i]), function=self.send, arg=i) for i in range(18)]
            [self.send(i) for i in range(18)]
        
        elif config == 1:
            # Appelle la fonction qui envoit le message
            self.ctls = [Midictl(ctlnumber=i, minscale=0, maxscale=1) for i in [74, 71, 11, 9, 86, 88, 20, 22]]
            self.tf = [TrigFunc(Change(self.ctls[i]), function=self.send, arg=i) for i in range(8)]     
            [self.send(i) for i in range(8)]

        
        [ctl.setInterpolation(False) for ctl in self.ctls]

    def send(self, which):
        self.value = self.ctls[which].get()
        self.oscsender.send([self.value], self.addresses[which])
        
        if(self.debug == True):
            print "{0}: {1}".format(str(self.addresses[which]), str(self.ctls[which].get()))