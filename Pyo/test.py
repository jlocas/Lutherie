from pyo import *
s = Server().boot()
s.start()
tab = SndTable(path='samples/SHD_808HH_01.wav')
tim = Phasor([-0.2,-0.25], mul=tab.getDur()-0.005, add=0.005)
rst = Metro(tim).play()
a = OscTrig(tab, rst, freq=tab.getRate(), mul=.4).out()
s.gui(locals())