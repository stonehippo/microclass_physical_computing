# Output: making rainbows with RGB LEDs!
import time
import board
from neopixel import NeoPixel
from rainbowio import colorwheel

pixels = NeoPixel(board.NEOPIXEL, 2, brightness=0)

while True:
	for value in range(256):
		pixels.fill(colorwheel(value))
		time.sleep(0.05)