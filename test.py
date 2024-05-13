import time
import board
import neopixel


pixpin = board.D18

numpix = 144

strip = neopixel.NeoPixel(pixpin, numpix)

def wheel(pos):
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

while True:
    for j in range(255*100):
        for i in range(numpix):
            strip[i]=wheel((i+j))
        strip.show()
        time.sleep(1)

    



            