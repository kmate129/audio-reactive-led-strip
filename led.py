from __future__ import print_function
from __future__ import division

import platform

from numpy import tile, load, roll, clip, left_shift, bitwise_or, array_equal, copy
import config
import neopixel
    
strip = neopixel.NeoPixel(config.LED_PIN, config.N_PIXELS)
strip.fill((0,255,0))

_gamma = load(config.GAMMA_TABLE_PATH)
"""Gamma lookup table used for nonlinear brightness correction"""

_prev_pixels = tile(253, (3, config.N_PIXELS))
"""Pixel values that were most recent ly displayed on the LED strip"""

pixels = tile(1, (3, config.N_PIXELS))
"""Pixel values for the LED strip"""

def update():
    """Writes new LED values to the Raspberry Pi's LED strip
    """
    global pixels, _prev_pixels
    # Truncate values and cast to integer
    pixels = clip(pixels, 0, 255).astype(int)
    # Optional gamma correction
    p = _gamma[pixels] if config.SOFTWARE_GAMMA_CORRECTION else copy(pixels)
    # Encode 24-bit LED values in 32 bit integers
    r = left_shift(p[0][:].astype(int), 8)
    g = left_shift(p[1][:].astype(int), 16)
    b = p[2][:].astype(int)
    rgb = bitwise_or(bitwise_or(r, g), b)
    # Update the pixels
    for i in range(config.N_PIXELS):
        # Ignore pixels if they haven't changed (saves bandwidth)
        if array_equal(p[:, i], _prev_pixels[:, i]):
            continue
        strip[i] = int(rgb[i])
    _prev_pixels = copy(p)
    strip.show()()


if __name__ == '__main__':
    import time
    pixels *= 0
    pixels[0, 0] = 255 
    pixels[1, 1] = 255
    pixels[2, 2] = 255 
    print('Starting LED strand test')
    while True:
        pixels = roll(pixels, 1, axis=1)
        update()
        time.sleep(.1)
