#!/usr/bin/python3

# Konfiguration der Bits: 2^0 -> GPIO12, ... 2^3 -> GPIO21
Bits = [12, 16, 20, 21]


def HexDisplay(Ziffer):
    global Bits
    if Ziffer > 15 or Ziffer < 0:
        # Hex-Ziffern können nur zwischen 0 und F liegen
        return -1
    for b in range(4):
        if Ziffer % 2 == 1:
            G.output(Bits[b], G.HIGH)
        else:
            G.output(Bits[b], G.LOW)
        Ziffer = Ziffer >> 1
    return 0

import time

try:
    import RPi.GPIO as G
except:
    print("Arbeitest Du gerade unter Windows?")

# Benennung der Pins mit den Signalnamen
G.setmode(G.BCM)
G.setup(12, G.OUT, initial=G.LOW)
G.setup(16, G.OUT, initial=G.LOW)
G.setup(20, G.OUT, initial=G.LOW)
G.setup(21, G.OUT, initial=G.LOW)

for i in range(16):
    print("Anzeige:", i)
    HexDisplay(i)
    time.sleep(1)

time.sleep(9)
G.cleanup()