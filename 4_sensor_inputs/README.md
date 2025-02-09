# Input: Reading A Distance Sensor

We have now seen how simple it can be to get data from the real world via an input like a touch sensor. Let's try a different type of sensor now, something a little more excting than a fancy button. This time, we'll read distance from a sensor on the Proximity Trinkey.

The APDS9660 is a simple, short range distance sensor. It uses a small infrared LED to send out pulses, sort of like a little radar. Normally, those pulses of invisible light will go quite a distance before they hit something and the sensor stays quiet. But when an object is a few inches from the sensor, that light bounces back and the sensor is triggered.

Unlike the touch sensors we used before, the proximity sensor can give us more information than on/off. Some distance sensors can give precise measurements of how far an object might be. Our sensor isn't quite that smart, but it can tell us with something is nearer or farther away within its sensor range. For this sensor, the maximum distance it will pick up anything is a few inches, depending on the gain (power) the sensor is set to.

Let's see some code that makes it work and then we will break it down a little.

```python
import time
import board

from adafruit_apds9960.apds9960 import APDS9960

i2c = board.I2C()
apds = APDS9960(i2c)
apds.proximity_gain = 2 
apds.enable_proximity = True

while True:
	print(f"Distance signal: {apds.proximity}")
	time.sleep(0.25)
```

Once again, we use `import` to bring in the `time` and `board` moudles. As you might have guessed by now, these are pretty useful and if you will encounter them in almost every CircuitPython program.

We also import the driver for the APDS9960 sensor. We use `from` so we can get the driver instead of the whole module, since that is all we need.

Before we set up the device, we need to do something new. The APDS9960 sensor uses a special interface called [Inter-Integrated Circuit](https://en.wikipedia.org/wiki/I%C2%B2C), or I2C, to communicate with our microcontroller. I2C is a common way to connect sensors and other peripherals in devices, because it uses a simple bus-type connectivity and can support dozens of devices using only a couple of pins on the microcontrollers. For example, your phone most likely has several devices that use I2C to connect.

In our code, we assign the I2C *singleton* from the `board` module to the variable `i2c`. A singleton special structure for getting an object where you want to be sure you always get the same one. In this case, the `board.I2C()` method ensures that we get the right setup of pins needed to talk to the sensor. There are other ways to do this in CircuitPython, but we will use this simple method here.

```python
i2c = board.I2C()
```

We don't have to create the `i2c` variable, we could just pass the singleton directly to the driver. But it is a good practice to use the variable when working with multiple I2C devices, so we will do that here, too.

Now we can set up the sensor:

```python
apds = APDS9960(i2c)
apds.proximity_gain = 2 
apds.enable_proximity = True
```

We are doing a few things here. First, we are getting access to the sensor itself, telling the driver it can find the actual hardware connected to I2C. Next, we set the gain of the sensor, which is its power level. By default, the sensor is at 1x. This setting uses the least amount of energey, but it is also fairly short ranged. We will turn up the gain to 4x, which increases the sensing distance. The value `2` is a flag that tells the driver that is what we want. Finally, we tell the sensor to start checking for nearby objects.

## A Short Note About The APDS9960

The proximity sensor we are using here is more clever that it might at first appear. In this lession, we are using the sensor to measure distance to a nearby object. However, it can do more than that. This sensor is also able to detect some simple gestures, such as a hand moving from right to left or vice versa. It can also read color information from a object in front of it.

Many sensors you might work with will begin getting data as soon as they're on and you only need to set up the driver before you can get to it. Because the APDS9960 can do several things, all with the same sensor hardware, but an only do one thing at a time, we need to enable the function we want. That's why we need to set `enable_proximity` to `True`.

## Back To The Code!

We've got the proximity sensor up and running. But we want to read from it continuously and report distances to us. Sounds like a job for a runtime loop!

```python
while True:
	print(f"Distance signal: {apds.proximity}")
	time.sleep(0.25)
```

The loop here is one of the simplest we've seen. For each pass through the runtime loop, we read and print the proximity value from the sensor, then sleep for a 250 milliseconds (a quarter of a second). Easy, right?

But if you look closely, there's something new here. Inside of the `print()` function, we are giving it the argument `f"Distance signal: {apds.proximity}"`. This is a fancy little thing in Python called a *format string*. the 'f' at the beginning tells the Python interpreter to substitute anything we put in curly braces ('{}') with the value of whatever is inside those braces.

In this case, that will be the proximity reported by the sensor, which can be from 0-255, with 0 meaning nothing is detected, 255 meaning something is more-or-less touching the sensor, and values in between giving as a relative measure.

The format string is a nice way for us to format data when we output it to the console.

Now that we have worked through some outputs and inputs, lets [bring it all together](../5_integrating_inputs_and_outputs/README.md).