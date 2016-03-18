from pyo import *
        
#############################################################
class Pulsynth:
    def __init__(self, octave, voices, spread, mul):
        self.octave = octave

        #how many octaves 
        self.spread = spread
        self.freqs = [100]
        self.decays = [0.125, 0.250, 0.5, 1]
        self.mul=mul
        
        self.voices = voices
        self.which = 0  #which voice will be used

        self.env = [Adsr(attack=0.01, decay=0.5, sustain=0, release=0.10, dur=0, mul=self.mul, add=0) for i in range(self.voices)]
        self.src = [FM(carrier=100, ratio=0.50, index=5, mul=self.env[i], add=0) for i in range(self.voices)]
        self.rvb = Freeverb(input=self.src, size=0.50, damp=0.50, bal=0.30, mul=1, add=0)

        
        self.output = self.src

    def UpdateNotes(self, notes):
        self.freqs = []

        for i in range(len(notes)):
            self.newFreq = midiToHz(notes[i] % 12 + 12 * self.octave)

            if self.newFreq not in self.freqs:
                self.freqs.append(self.newFreq)
                
                for j in range(self.spread):
                    self.freqs.append(midiToHz(notes[i] % 12 + 12 * (j+1) + 12 * self.octave))
                                                    
    def Pulse(self):
        self.src[self.which].carrier = random.choice(self.freqs)
        self.env[self.which].decay = random.choice(self.decays)
        self.src[self.which].index = random.uniform * 10

        self.env[self.which].play()
        self.which = (self.which + 1) % self.voices

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
        self.delay = Delay(input=self.src, delay=[0.25, 0.5], feedback=0.25, maxdelay=0.5, mul=0.7, add=0)
        self.rvb = Freeverb(input=self.src+self.delay, size=0.90, damp=0.50, bal=0.70, mul=1, add=0)

        self.transpo = Harmonizer(input=self.rvb, transpo=12.00, feedback=0, winsize=1, mul=0.1, add=0)

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
