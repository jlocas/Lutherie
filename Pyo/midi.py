
# Configuration audio/midi
idev = 4
s = Server()
s.setMidiInputDevice(idev)
s.boot()

# Recoit les notes Midi et les assignes sur 10 voix de polyphonie
self.note = Notein(poly=10, scale=1, first=0, last=127)