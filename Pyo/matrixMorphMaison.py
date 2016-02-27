from pyo import *
s = Server().boot()

SIZE = 8
m1 = NewMatrix(SIZE, SIZE)
m1.genSineTerrain(1, 4)
m2 = NewMatrix(SIZE, SIZE)
m2.genSineTerrain(2, 8)

inter = SigTo(0, 0.05, 0)

a = Sine(.31).range(1,4)
b = Sine(.25).range(1,4)
def change():
    av = a.get()
    bv = b.get()
    which = int(inter.get())
    if which == 0:
        m2.genSineTerrain(av, bv)
    else:
        m1.genSineTerrain(av, bv)
    inter.value = 1 - which

pat = Pattern(function=change, time=0.06).play()

x = Sine([49,50], 0, .45, .5)
y = Sine([49.49,50.5], 0, .45, .5)
c1 = MatrixPointer(m1, x, y, .2)
c2 = MatrixPointer(m2, x, y, .2)
c = Interp(c1, c2, inter).out()

s.gui(locals())
