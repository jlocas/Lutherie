from pyo import *
import math


class Choir:
    def __init__(self, mul):
        self.mul = mul
        self.sound = 'W:\Projects\Lutherie\Pyo\samples\Choir_Bass_MMMM.wav'
        self.st = SndTable(path=self.sound, chnl=None, start=0, stop=None, initchnls=1)
        self.length = 20
        
        self.amps = SigTo(value=0, time=4, init=0.00, mul=3, add=0)

        self.stfr = [Randi(min=0.99, max=1.01, freq=1.00, mul=1, add=0) for i in range(self.length)]
        self.stf = SigTo(value = self.st.getRate(), time=0.01, init=self.st.getRate(), mul=self.stfr, add=0)
        self.stp = [(i+1.0) / self.length for i in range(self.length)]
        
        self.read = Osc(table=self.st, freq=self.stf, phase=self.stp, mul=self.amps)
        
        self.voiceMix = Mix(input=self.read, voices=2, mul=self.mul, add=0)

        
        self.output = self.voiceMix


    def GetOutput(self):
        return self.output

    def UpdateAverageDeviation(self, avgdev):
        pass
            
    def UpdateAverageHeightDev(self, avgydev):
        if(avgydev > 25):
            self.amps.setValue((avgydev - 25) * 0.01)
        else:
            self.amps.setValue(0)


class VelSynth3:
    def __init__(self, octave, mul):
        self.octave = octave
        self.mul = mul
        

        #1d lists because 2d lists crash the thing
        self.freq = SigTo(value=200, time=1, init=100, mul=1)
        self.amp = SigTo(value=0, time=1, init=0)


        self.src = Sine(freq=self.freq, mul=self.amp, add=0)

        self.dist = Disto(input=self.src, drive=0.5, slope=0.50, mul=1, add=0)

        self.comp = Compress(input=self.dist, thresh=-20, ratio=5, risetime=0.1, falltime=0.2, lookahead=5.00, knee=0, outputAmp=False, mul=4, add=0)
        self.lim = Compress(input=self.comp, thresh=-5, ratio=200, risetime=0.02, falltime=0.2, lookahead=5.00, knee=0, outputAmp=False, mul=1, add=0)
        
        self.output = Mix(input=self.lim, voices=2, mul=self.mul, add=0)
        
   
        
    def UpdateAverageVelocity(self, avgvel):
        self.amp.setValue(max((avgvel - 20), 0))
                        
    def UpdateNotes(self, notes):
        self.freq.setValue(midiToHz(notes[0]))
                        
    def GetOutput(self):
        return self.output

    def UpdateAverageDeviation(self, avgdev):
        pass
        
    def UpdateAverageHeight(self, avgy):
        pass
        
    def UpdateAverageHeightDev(self, avgy):
        pass
        
