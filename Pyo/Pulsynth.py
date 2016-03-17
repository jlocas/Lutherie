from pyo import *
        
#############################################################
class Pulsynth:
    def __init__(self, length, octave):
        self.length = length
        self.size = self.length*self.length
        self.octave = octave
        
        self.blockIndex = [[0 for x in range(self.length)] for z in range(self.length)]
        self.blockFreqs = [[100 for x in range(self.length)] for z in range(self.length)]

        self.freq = SigTo(value=1000, time=0.01, init=1000.00, mul=1, add=0)
        self.env = Adsr(attack=0.01, decay=0.5, sustain=0, release=0.10, dur=0, mul=1, add=0)
        self.src = SineLoop(freq=self.freq, feedback=0, mul=self.env, add=0)
        self.output = self.src
        

    def Pulse(self, x, z):
        self.freq.setValue(self.blockFreqs[x/self.length][z/self.length])
        self.env.play()


    def UpdateNotes(self, notes):
        for x in range(self.length):
            for z in range(self.length):
                self.blockFreqs[x][z] = midiToHz(notes[x][z] + 12 * self.octave)
                
    def GetOutput(self):
        return self.output


class Pulsynth2:
    def __init__(self, octave, voices, spread, mul):
        self.octave = octave

        #how many octaves 
        self.spread = spread
        self.freqs = [100]
        self.decays = [0.125, 0.25]
        self.mul=mul
        
        self.voices = voices
        self.which = 0  #which voice will be used

        self.env = [Adsr(attack=0.01, decay=0.5, sustain=0, release=0.10, dur=0, mul=self.mul, add=0) for i in range(self.voices)]
        self.src = [SineLoop(freq=100, feedback=0.1, mul=self.env[i], add=0) for i in range(self.voices)]
        self.delay = Delay(input=self.src, delay=[0.25, 0.5], feedback=0.25, maxdelay=0.5, mul=1, add=0)
        self.rvb = Freeverb(input=self.src+self.delay, size=0.90, damp=0.50, bal=0.70, mul=1, add=0)

        self.transpo = Harmonizer(input=self.rvb, transpo=12.00, feedback=0, winsize=1, mul=0.2, add=0)

        self.output = Sig(0)

        self.output = self.rvb + self.transpo

    def UpdateNotes(self, notes):
        self.freqs = []

        for i in range(len(notes)):
            self.newFreq = midiToHz(notes[i] % 12 + 12 * self.octave)

            if self.newFreq not in self.freqs:
                self.freqs.append(self.newFreq)
                
                for j in range(self.spread):
                    self.freqs.append(midiToHz(notes[i] % 12 + 12 * (j+1) + 12 * self.octave))
                                                    
    def Pulse(self):
        self.src[self.which].freq = random.choice(self.freqs)
        self.env[self.which].decay = random.choice(self.decays)

        self.env[self.which].play()
        self.which = (self.which + 1) % self.voices

    def GetOutput(self):
        return self.output
