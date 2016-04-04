from pyo import *
        
#############################################################

class Pulsynth:
    def __init__(self, octave, voices, spread, mul):
        self.octave = octave

        #how many octaves 
        self.spread = spread
        self.freqs = [100]
        self.decays = [0.125, 0.25, 0.5]
        self.mul=mul
        
        self.voices = voices
        self.which = 0  #which voice will be used

        self.env = [Adsr(attack=0.01, decay=0.5, sustain=0, release=0.10, dur=0, mul=1, add=0) for i in range(self.voices)]
        self.src = [SineLoop(freq=100, feedback=0.1, mul=self.env[i], add=0) for i in range(self.voices)]
        self.delay = Delay(input=self.src, delay=[0.25, 0.5], feedback=0.25, maxdelay=0.5, mul=0.7, add=0)
        self.rvb = Freeverb(input=self.src+self.delay, size=0.90, damp=0.50, bal=0.5, mul=1, add=0)

        self.output = Mix(input=self.rvb, voices=10, mul=self.mul, add=0)

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
        
