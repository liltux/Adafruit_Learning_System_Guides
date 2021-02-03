"""
NeoPixel example for Pico. Turns the NeoPixels red, green, and blue in sequence.

REQUIRED HARDWARE:
* RGB NeoPixel LEDs connected to pin GP0.
"""
import time
import board
import neopixel

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 30

pixels = neopixel.NeoPixel(board.GP0, num_pixels)
pixels.brightness = 0.5

while True:
    pixels.fill((255, 0, 0))
    time.sleep(0.5)
    pixels.fill((0, 255, 0))
    time.sleep(0.5)
    pixels.fill((0, 0, 255))
    time.sleep(0.5)
