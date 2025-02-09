# Integration: Bring It All Together

For our final lesson, we are going to bring together everything that we've learned about during this course. We will us our various inputs to adjust the NeoPixels output.

- We will read the proximity sensor and map the how near an object is to the brightness of the NeoPixels
- We will read the touch sensors to change the color of the NeoPixels

Here's what that code looks like:

```python
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
```

There is a lot going on here, so take a minute to read it through and see if you can understand what is being done. Keep in mind that this code builds on the earlier examples, so you should see some by now familiar elements.

- Bringing in modules with `import` and `from`
- Setting up drivers for inputs and outputs
- Creating a runtime loop
- Reading from sensors and setting NeoPixel colors

## But Wait, There's More!

All of this you have seen before. But you probably also noticed a big chunk of code in the middle of the program. It began with this code:

```python
def map_range(
    x: float, in_min: float, in_max: float, out_min: float, out_max: float
) -> float:
```

This is the start of a *function definition*. Up to now, we have called functions or methods, but this is the first time we are defining one ourselves. Like the control structures we have already seen, such as `while`, `for`, and `if`, a function has a block of code that will be executed when it is called. Recall that blocks in Python are indented, so we can see pretty easily what is in the block and what is not.

What we are doing here is defining the function `map_range()`, which is a utility that we'll use to take values from one range of numbers and return an equivalent value in another range. We need to do this because our proximity sensor returns values from 0 to 255, but our NeoPixel's brigtness is set with a value from 0.0 to 1.0.

We won't go too deeply into the body of the code, but here is how it gets called:

```python
map_range(value, 0, 255, 0, 1.0)
```

The function takes five parameters: the value we want to map, the start and end of the initial range, and the start and end of the new range.

Defining functions like this lets us organize and label bits of functionality. This is really useful when have complex programs. Using functions can make our code much easier to read and understand.

Before we go on, we should take a look at one other thing in the function. Inside its block, there is a note about what the funtion is for. That note is surround by a set of three single quotes. This is how you defined a *multiple line comment* in Python. A *comment* is a piece of code that gets placed in a program but is ignored by the interpreter. It is a note to any coders reading the code. If you look at the top of the code for lession, and for all of the previous ones, you will see a *comment*, which starts with a pound sign, like this:

```python
# No comment.
```

You can place comments anywhere on a line in Python. Everything after the pound sign will be ignored until the next line:

```python
print("This is code that will be run") # This is a comment that will not
```

## Wrapping Up

Armed with everthing we have covered up to know, I hope that you have a pretty good understanding of what this code is going to do. Give it a run on the Proxmity Trinkey and have some fun!