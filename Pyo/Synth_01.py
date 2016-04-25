from pyo import *
from SpringGridBlock import *
import math

class FMSynth:
    def __init__(self, length, octave, mul):
        self.length = length
        self.size = self.length*self.length
        self.octave = octave
        self.mul = mul
        
        #1d lists because 2d lists crash the thing
        self.freqs = [SigTo(value=100, time=0.015625, init=100) for i in range(self.size)]
        self.amps = [SigTo(value=0, time=0.06, init=0) for i in range(self.size)]
        self.index = SigTo(value=1, time=0.015625, init=1, mul=1)
        
        self.src = FM(carrier=self.freqs, ratio=2, index=self.index, mul=self.amps, add=0)
        self.voiceMix = Mix(input=self.src, voices=2, mul=1, add=0)
        
        self.comp = Compress(input=self.voiceMix, thresh=-20, ratio=12, risetime=0.01, falltime=0.02, lookahead=5.00, knee=0, outputAmp=False, mul=4, add=0)
        self.lim = Compress(input=self.comp, thresh=-1, ratio=100, risetime=0.01, falltime=0.02, lookahead=5.00, knee=0, outputAmp=False, mul=2, add=0)
        
        #self.clip = Clip(input=self.lim, min=-0.99, max=0.99, mul=1, add=0)
        
        self.output = Mix(input=self.lim, voices=2, mul=self.mul)
        
        
    def UpdateHeights(self, heights):
        self.heights = heights
        i = 0
        
        for x in range(self.length):
            for z in range(self.length):
                self.amps[i].setValue(self.heights[x][z] * 0.01)
                i += 1
                        
    def UpdateNotes(self, notes):
        
        self.i = 0
        for x in range(self.length):
            for z in range(self.length):
                self.freqs[self.i].setValue(midiToHz(notes[x][z] + 12 * self.octave))
                self.i += 1
                
        self.src.setCarrier(self.freqs)
        
    def UpdateAverageHeight(self, avgy):
        self.index.setValue(avgy*2)
        pass
        
    def UpdateAverageDeviation(self, avgdev):
        pass
        
    def UpdateAverageHeightDev(self, avgydev):
        #self.index.setValue(avgydev)
        pass

        
    def GetOutput(self):
        return self.output
                
#############################################################
class WTSynth:
    def __init__(self, length, octave, mul):
        self.length = length
        self.size = self.length*self.length
        self.octave = octave
        self.mul = mul
        
        self.voices = 4
        self.heights = [[0.0 for x in range(self.length)] for z in range(self.length)]

        self.m1 = NewMatrix(width=self.length, height=self.length, init=self.heights)
        self.m2 = NewMatrix(width=self.length, height=self.length, init=self.heights)
        self.inter = SigTo(0, 0.02, 0)
 
        self.freqDev = SigTo(value=0.01, time=1, init=0.01, mul=1, add=0)
        self.freqDevFreq = SigTo(value=1, time=1, init=1, mul=1, add=0)
        
        self.xfreqRand = Randi(min=1 - self.freqDev, max=1 + self.freqDev, freq=self.freqDevFreq, mul=[1 for i in range(self.voices)])
        self.zfreqRand = Randi(min=1 - self.freqDev, max=1 + self.freqDev, freq=self.freqDevFreq, mul=[1 for i in range(self.voices)])
        self.xfreq = SigTo(value=50, time=0.015625, init=50, mul=self.xfreqRand, add=0)
        self.zfreq = SigTo(value=50, time=0.015625, init=50, mul=self.zfreqRand, add=0)

        #+ ou - le mul autour du add
        self.x = Sine(freq=self.xfreq, mul=0.25, add=0.5)
        self.z = Sine(freq=self.zfreq, mul=0.25, add=0.5)
        
        self.ptr1 = MatrixPointer(matrix=self.m1, x=self.x, y=self.z, mul=1, add=0)
        self.ptr2 = MatrixPointer(matrix=self.m2, x=self.x, y=self.z, mul=1, add=0)
        self.ptr = Interp(self.ptr1, self.ptr2, self.inter)
        
        self.voiceMix = Mix(input=self.ptr, voices=2, mul=self.mul, add=0)
        
        self.drive = SigTo(value=0, time=2, init=0.00, mul=1, add=0)
        self.dist = Disto(input=self.voiceMix, drive=self.drive, slope=0.5, mul=1, add=0)

        self.lpfreq = SigTo(value=18000, time=0.01, init=18000.00, mul=1, add=0)
        self.lpf = Biquadx(input=self.dist, freq=5000, q=1, type=0, stages=4, mul=1, add=0)
        self.hpf = Biquadx(input=self.lpf, freq=30, q=2, type=1, stages=2, mul=1, add=0)
        
        self.flgexpr = SigTo(value=0, time=1, init=0.00, mul=1, add=0)
        self.flgmul = SigTo(value=1, time=0.01, init=1.00, mul=self.flgexpr, add=0)
        self.flgfreq = SigTo(value=0.01, time=4, init=10, mul=self.flgexpr, add=0)
        self.flgfeed = SigTo(value=0.8, time=0.01, init=0.8, mul=self.flgexpr, add=0)


        self.flglfo = Sine(freq=self.flgfreq, mul=.0045, add=.005)
        self.flg = Delay(input=self.dist, delay=self.flglfo, feedback=self.flgfeed, maxdelay=1, mul=self.flgmul, add=0)
        
        self.comp = Compress(input=self.dist + self.flg, thresh=-15, ratio=12, risetime=0.01, falltime=0.02, lookahead=5.00, knee=0, outputAmp=False, mul=4, add=0)
        self.lim = Compress(input=self.comp, thresh=-5, ratio=100, risetime=0.01, falltime=0.02, lookahead=5.00, knee=0, outputAmp=False, mul=4, add=0)

        self.output = self.lim

        
    def UpdateHeights(self, heights):

        for x in range(self.length):
            for z in range(self.length):
                self.heights[x][z] = heights[x][z]

        self.which = int(self.inter.get())
        
        if self.which == 0:
            self.m2.replace(self.heights)
        else:
            self.m1.replace(self.heights)
        
        self.inter.setValue(1 - self.which)


    def UpdateNotes(self, notes):
        self.freq = midiToHz(notes[0] + 12 * self.octave)
        
        for i in range(self.voices):
            self.xfreq.setValue(self.freq)
            self.zfreq.setValue(self.freq)
        
    def GetOutput(self):
        return self.output
        
    def UpdateAverageDeviation(self,avgdev):
        pass

    def UpdateAverageHeightDev(self, avgydev):
        minht = 10
        if(avgydev > minht):
            self.freqDev.setMul( 1 + (avgydev - minht))
            self.freqDevFreq.setMul(1 + (avgydev - minht) * 20)
            self.drive.setValue(min((avgydev - minht) * 0.5, 0.5))
            self.flgexpr.setValue(min((avgydev - minht) * 0.5, 1))
        else:
            self.freqDev.setMul(1)
            self.freqDevFreq.setMul(1)
            self.drive.setValue(0)
            self.flgexpr.setValue(0)
        pass

    def UpdateAverageVelocity(self,avgvel):
        pass
        

class VelSynth:
    def __init__(self, length, octave, mul):
        self.length = length
        self.size = self.length*self.length
        self.octave = octave
        self.mul = mul
        

        #1d lists because 2d lists crash the thing
        self.freqs = [SigTo(value=200, time=0.25, init=100, mul=1) for i in range(self.size)]
        self.amps = [SigTo(value=0, time=0.25, init=0) for i in range(self.size)]
        self.formants = [710, 1100, 2640]
        
        #am settings
        self.amfreq = SigTo(value=0, time=0.02, init=0)
        self.ammod = SineLoop(freq=self.amfreq, feedback=0.01, mul=0.5, add=0.5)
        
        self.lpfreq = SigTo(value=500, time=0.06, init=0)


        self.src = SineLoop(freq=self.freqs, feedback=0.1, mul=self.amps, add=0)

        self.form = Biquad(input=self.src, freq=self.formants, q=25, type=2, mul=[2, 1, 0.5], add=0)
        self.mouth = Biquadx(input=self.form, freq=self.lpfreq, q=1, type=0, stages=2, mul=self.ammod, add=0)
        
        self.comp = Compress(input=self.mouth, thresh=-15, ratio=5, risetime=0.1, falltime=0.2, lookahead=5.00, knee=0, outputAmp=False, mul=4, add=0)
        self.lim = Compress(input=self.comp, thresh=-1, ratio=200, risetime=0.02, falltime=0.2, lookahead=5.00, knee=0, outputAmp=False, mul=1, add=0)
        

        self.output = Mix(input=self.lim, voices=2, mul=self.mul, add=0)
        
   
        
    def UpdateSpeeds(self, speeds):
                
        for i in range(self.size):
            val = speeds[i]                
            self.amps[i].setValue(min(val * 0.1, 1))
                        
    def UpdateNotes(self, notes):
        
        i = 0
        for x in range(int(self.length)):
            for z in range(int(self.length)):
                self.freqs[i].setValue(midiToHz((notes[x][z] % 12) + 12 * self.octave))

                i += 1
                

                        
    def GetOutput(self):
        return self.output

    def UpdateAverageDeviation(self, avgdev):
        self.amfreq.setValue(avgdev*2)
        #self.lpfreq.setValue(avgdev * 500 + 1000)
        
    def UpdateAverageHeightDev(self, avgydev):
        pass
        
    def UpdateAverageHeight(self, avgy):
        pass
        #self.lpfreq.setValue(avgy * 500 + 1000)
        



class VelSynth2:
    def __init__(self, octave, voices, mul):
        self.octave = octave
        self.mul = mul
        
        self.voices = voices

        self.freqrandexpr = SigTo(value=0, time=0.03, init=0.00, mul=1, add=0)
        self.freqrandfreq = SigTo(value=50, time=0.01, init=0.00, mul=self.freqrandexpr, add=0)
        self.freqrand = Randi(min=0.99, max=1.01, freq=self.freqrandfreq, mul=1, add=[0 for i in range(self.voices)])
        
        #1d lists because 2d lists crash the thing
        #self.rndFreq = [Randi(min=0.99, max=1.01, freq=0.50, mul=1, add=0) for i in range(self.voices)]
        self.freqs = [100]
        self.freqsigs = [SigTo(value=200, time=0.015625, init=200, mul=self.freqrand + self.freqrandexpr) for i in range(self.voices)]
        self.amps = [SigTo(value=0, time=4, init=0, mul=1) for i in range(self.voices)]
        

        self.src = Sine(freq=self.freqsigs, mul=self.amps, add=0)
        self.voiceMix = Mix(input=self.src, voices=2, mul=1, add=0)

        self.deg = Degrade(input=self.voiceMix, bitdepth=4, srscale=1, mul=1, add=0)
        self.rvb = Freeverb(input=self.deg, size=0.90, damp=0.20, bal=0.80, mul=1, add=0)

        self.comp = Compress(input=self.rvb, thresh=-10, ratio=5, risetime=0.1, falltime=0.2, lookahead=5.00, knee=0, outputAmp=False, mul=4, add=0)
        self.lim = Compress(input=self.comp, thresh=-1, ratio=200, risetime=0.01, falltime=0.02, lookahead=5.00, knee=0, outputAmp=False, mul=1, add=0)
        
        self.output = Mix(input=self.lim, voices=2, mul=self.mul, add=0)
        
        self.avgydev = 0
   
        
    def UpdateAverageVelocity(self, avgvel):
        val = max((avgvel - 15) * 0.01, 0)
        for i in range(self.voices):
            self.amps[i].setValue(min(val, 1))
                        
    def UpdateNotes(self, notes):
        self.freqs = []
        
        for i in range(len(notes)):
            self.newFreq = midiToHz(notes[i] % 12 + 12 * self.octave)

            if self.newFreq not in self.freqs:
                self.freqs.append(self.newFreq)
                    
        for i in range(self.voices):
            self.freqsigs[i].setValue(self.freqs[i % len(self.freqs)])
                        
    def GetOutput(self):
        return self.output

    def UpdateAverageDeviation(self, avgdev):
        pass

    def UpdateAverageHeight(self, avgy):
        pass

    def UpdateAverageHeightDev(self, avgydev):
        minht = 15
        if(avgydev > minht):
            self.freqrandexpr.setValue(min((avgydev - minht) * 0.001, 1))
        else:
            self.freqrandexpr.setValue(0)
