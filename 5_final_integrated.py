# Bringing it all together!
import time
import board
from neopixel import NeoPixel
from rainbowio import colorwheel

from adafruit_apds9960.apds9960 import APDS9960

import touchio

touch_one = touchio.TouchIn(board.TOUCH1)
touch_two = touchio.TouchIn(board.TOUCH2)

color_index = 0

pixels = NeoPixel(board.NEOPIXEL, 2, brightness=0)
pixels.fill(colorwheel(color_index))

def map_range(
    x: float, in_min: float, in_max: float, out_min: float, out_max: float
) -> float:
    """
    Maps a number from one range to another.
    Note: This implementation handles values < in_min differently than arduino's map function does.

    :return: Returns value mapped to new range
    :rtype: float
    """
    in_range = in_max - in_min
    in_delta = x - in_min
    if in_range != 0:
        mapped = in_delta / in_range
    elif in_delta != 0:
        mapped = in_delta
    else:
        mapped = 0.5
    mapped *= out_max - out_min
    mapped += out_min
    if out_min <= out_max:
        return max(min(mapped, out_max), out_min)
    return min(max(mapped, out_max), out_min)

i2c = board.I2C()
apds = APDS9960(i2c)
apds.proximity_gain = 2 
apds.enable_proximity = True 

print("Measuring distance")

while True:
    if touch_one.value or touch_two.value:
        if touch_one.value:
            if color_index == 255:
                color_index = 0
            else:
                color_index = color_index + 1
        if touch_two.value:
            if color_index == 0:
                color_index = 255
            else:
                color_index = color_index - 1
        pixels.fill(colorwheel(color_index))
    
    proximity = apds.proximity
    if proximity != 0:
        print(proximity)
    pixels.brightness = map_range(proximity, 0, 255, 0, 1.0)
    time.sleep(0.01)