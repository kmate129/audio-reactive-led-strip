from __future__ import print_function
from __future__ import division
import os

LED_PIN = 18
"""GPIO pin connected to the LED strip pixels (must support PWM)"""

LED_FREQ_HZ = 800000
"""LED signal frequency in Hz (usually 800kHz)"""

LED_DMA = 5
"""DMA channel used for generating PWM signal (try 5)"""

BRIGHTNESS = 255
"""Brightness of LED strip between 0 and 255"""

LED_INVERT = True
"""Set True if using an inverting logic level converter"""

SOFTWARE_GAMMA_CORRECTION = True
"""Set to True because Raspberry Pi doesn't use hardware dithering"""

USE_GUI = True
"""Whether or not to display a PyQtGraph GUI plot of visualization"""

DISPLAY_FPS = True
"""Whether to display the FPS when running (can reduce performance)"""

N_PIXELS = 60
"""Number of pixels in the LED strip (must match ESP8266 firmware)"""

GAMMA_TABLE_PATH = os.path.join(os.path.dirname(__file__), 'gamma_table.npy')
"""Location of the gamma correction table"""

MIC_RATE = 44100
"""Sampling frequency of the microphone in Hz"""

FPS = 60
"""Desired refresh rate of the visualization (frames per second)"""

_max_led_FPS = int(((N_PIXELS * 30e-6) + 50e-6)**-1.0)
assert FPS <= _max_led_FPS, 'FPS must be <= {}'.format(_max_led_FPS)

MIN_FREQUENCY = 200
"""Frequencies below this value will be removed during audio processing"""

MAX_FREQUENCY = 12000
"""Frequencies above this value will be removed during audio processing"""

N_FFT_BINS = 24
"""Number of frequency bins to use when transforming audio to frequency domain"""

N_ROLLING_HISTORY = 2
"""Number of past audio frames to include in the rolling window"""

MIN_VOLUME_THRESHOLD = 1e-7
"""No music visualization displayed if recorded audio volume below threshold"""
