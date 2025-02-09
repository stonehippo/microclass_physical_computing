# Input: Using Capactive Touch Sensing

In our last program, we worked with NeoPixels as outputs, and learned some CircuitPython. This time, we're going to work with a couple of inputs, specifically a pair of capacitive touch sensors.

## A Little About Capacitive Touch

Capacitive touch sensing is a technology that lets us capture one of the most basic physical interactions we can do: touching stuff! This type of sensor measures capacitance, which is sort of like the amount of water in a bucket. When a finger comes near the sensor, the capacitance changes and we can detect that change. 

## Working With Touch

The Proximity Trinkey has two touch sensors on the end of the board. We can right a little code to work with them.

```python
# Input: sennsing with capacitive touch!
import time
import board

import touchio

touch_one = touchio.TouchIn(board.TOUCH1)
touch_two = touchio.TouchIn(board.TOUCH2)

while True:
	if touch_one.value:
		print("Someone is touching the first pad")
	if touch_two.value:
		print("Someone is touching the second pad")
	time.sleep(0.01)
```

What's going on here?

We start off by importing a couple of modules, as we did in the outputs code. We are once again bringing in our old friends `time` and `board`, but we have introduced a new module, `touchio`. This module is, like `neopixel`, a driver. This time it is for the touch sensors.

Once we bring our modules in, things are pretty simple from there. We create two variables, `touch_one` and `touch_two`, each of which refers to one of the touch sensors on the board. For example:

```python
touch_one = touchio.TouchIn(board.TOUCH1)
```

Once we have a way to get at the sensors, it is time for fire up a runtime loop. Recall that we do that with an infinite loop started with `while True:`. The bulk of the work for this example will happen in the block that gets executed in the loop.

We start by checking the value of the first touch sensor. This is pretty simple, since all we have to do is get its value. That looks like this:

```python
touch_one.value
```

If the sensor is being touched, the value returned will be `True`, if not its `False`. Couldn't be simpler!

Because the sensor value is 'truthy', we use the `if` control structure to take action. In this case, if the sensor is touched, we'll print a message to the console saying so.

We repeat this same action for the second sensor, then tell the microcontroller to sleep for 10 milliseconds.

That's all there is to it. We've set up a driver for a couple of sensors, and we're reading the value from those sensors forever. This is about as simple as input gets.

With other hardware, you might have a button or switch to read, but the code would be largely the same. We would need a different driver, but for most sensors where there is a clear on/off, binary state, we will just read its value and act accordingly.