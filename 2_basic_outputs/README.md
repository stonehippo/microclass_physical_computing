# Output: Using Physical Computing to Effect The World

Now that we've gotten our first working program, we're going to jump in a bit deeper. One of the main ideas of physical computing is that it bridges the interface of digital systems, i.e. computers, with the physcial world. One way that it can do that is through mechanisms that have an effect on the state of the world. There many such mechanisms, such as motors, actuators, and other mechanical devices. We are going to work with one of the more common first output devices, light emitting diodes, or LEDS.

The LEDs on the Proximity Trinkey that we are using for this course are a special kind on smart device, sometimes called a NeoPixel. They are a bit more complex than a run of the mill LED, for two reason. First, they are really three seperate LEDs—one red, one green, and one blue—all packaged together. Second, they are programmable, which means that we adjust the outputs of the three LEDs to make many colors!

Let's look at a program that will let us make rainbows using the two NeoPixels on the Proximity Trinkey. Take a look at the following program:

```python
# Output: making rainbows with RGB LEDs!
import time
import board
from neopixel import NeoPixel
from rainbowio import colorwheel

pixels = NeoPixel(board.NEOPIXEL, 2, brightness=0.4)

while True:
	for value in range(256):
		pixels.fill(colorwheel(value))
		time.sleep(0.05)
```

Ok, that's a lot more complex that **Hello, World**! There's a few things going on here that we can discuss. Some of those new things are about Python, and some are specific to CircuitPython, a version of the language that is designed to run on the small microprocessors that are often used in physical computing.

Let's look at the first couple of lines in our new program. Notice that they begin with the word `import`. This is a special code to the Python interpreter to load a *module*, which is a bit of code that adds functionality to the core Python language. The first module when load is called `time`:

```python
import time
```

This is a very useful module and one that you'll probably end up using quite a bit if you keep on writing Python code. The `time` module contains functions that help you count and measure time in various scales. As we will see in a minute, we are using a function called `time.sleep()`, which pauses the execution of our program for some number of seconds each time it's called.

We also import the `board` module. This is a special CircuitPython-specific module that gives us access to features of the development board that we're working with. For example, we will use the `board` module to connect to our NeoPixels.

We have a couple of additional imports, but they look a little different from the one aboves. They start with `from`. What's that about?

In Python, you can sometime import just the parts of a module that you want to use. This means importing in a specific function or object from the module. You can even bring in several such components from the module. For example:

```python
from time import sleep
```

Why would you do this, when you can bring the whole module in? There are a couple of reasons. If you only need one or two functions, importing only what you need from the module cuts down on typing; you can refer to `sleep()` rather than `time.sleep()`. Second this can save on working memory in the system: modules sometimes contain components that you don't need, so why import them. This can be especially helpful when working with the tiny amounts of memory in a microcontroller.

In our, we import the *class* `NeoPixel` from the `neopixel` module. This class is *driver*, which means that it contains code that helps us work with some piece of hardware on our development board. As you might have guessed, this is the driver for our NeoPixels.

We also import a function, `colorwheel` from the module `rainbowio`. This function is a sort of utility that lets us specify a color by giving it a numerical value. You'll be able to see how that works when you run the code.

Next up in our code we see a couple more new things. There's this line:

```python
pixels = NeoPixel(board.NEOPIXEL, 2, brightness=0.4)
```

What's up with that?

A few things are happening here. The line starts off with `pixels =…`. This is the assignment of a *variable*. Variables a sometimes described as boxes where you can put things, but I think they're more like the label that you put on the box. Whatever we put on the right side of the equal sign can be retrieved later using the variable name. So what are we putting in the box labelled `pixels`, exactly?

What we are doing is calling the `NeoPixel()` *constructor* (a type of function that makes a concrete thing for us to work with) that we imported from the `neopixel` module, giving it some *parameters* that will be used to set up the hardware. There are three parameters passed to the constructor. The first two parameters are *positional*, which is to say that we can know what they are based on the order we give them to the function. The last one is a *named parameter*, which means that it has an explicit label, or name, for us to use. Python supports both types of parameters, and they can be mixed and matched. We won't go into why that is in this course. But let's take a quick look at what we passed in.

`board.NEOPIXEL` is the first parameter we pass in. We are using a property of the `board` module that refers to a *pin* on the microcontroller that is wired to the physical NeoPixels. This is how the driver will know where to send the signals from the driver to the hardware. The next parameter is the value `2`, which is a liternal integer and represents the number of NeoPixels in the *strand*. Huh?

Ok, a quick thing about NeoPixels. Not only are they smart, but they can be chained together, end to end, so that we can control a whole bunch of the using one pin on our microcontroller. This is a great thing, because it means we can use other pins for other stuff. It also means that we can have chains, or strands, that are arbitrarily long. In this case, our strand has two NeoPixels.

The last parameter we pass in is `brightness=0.4`. This is a named parameter and you can probably guess what it does. We can control how bright the overall pixels are by reducing the amount of power we send. This parameter takes a *floating point* value from 0.0 to 1.0. 0.0 is off, and 1.0 is 100% on. To save our vision, we'll set the incredibly bright NeoPixels to 0.4, or 40% of the maximum brightness.

We've got out pixels set up, we can refer to them using the `pixels` variable. Now what?

Now we can set the color of the pixels to whatever like. They are literally millions of possible choices! We could pick anything we like using a numerical value. For exmaple, we could choose to make both NeoPixels red:

```python
pixels.fill(0xFF0000)
```

This tells the driver to make all of the pixels in the strand red. If you are familiar with using hexidecimal values to specifiy colors, you might recognize the value we passed to the `pixels.fill()` method (a *method* is a function associated with a object, which is bundle of functions and data). The `Ox` at the start of the number indicates that is is a hexidecimal value, and the rest is a number in base 16 (the values 01-15 expressed as the number 0-F; in base 16 A, B, C, D, E, and F are numbers). In this case, every two number represent reprenst 8 bits of information, which enough to hold a value from 0-255. FF in hex is the same as 255 in decimal. In this, it means "all the way on". And because it's the first pair of numbers, it means the red LED in our NeoPixels. The next two pairs are 00, which means 0, of course, or "all the way off". So this is sayinng "turn the red LED all the way on, and the green and blue LEDs all the way off".

Let's take a second to try this out. And we'll what other colers we can make.

...

Ok, back to our program. After we set up the NeoPixels, we see a couple of new Python things. Here's what that looks like again:

```python
while True:
	for value in range(256):
		pixels.fill(colorwheel(value))
		time.sleep(0.05)
```

The first is a `while` control structure. `while` is a sort of loop that gets checked for *truth* in a condition. If it's true in some way, the code move on to execute everything "inside" the `while`. If not, the loop is broken and the code moves on. In our code, the condition we're checking is to see if the *constant* `True` is true. As you might guess, it is.

In fact, it always will be, so barring outside intervention our loop will run forever. It's a infinite loop. In the parlance of CircuitPython, this is our *runtime loop*. In most physical computing, we want our little bit of hardware to perform a task over and over and over again. The infinite runtime loop is how we make that happen.

After the `while` statement, there's a colon. This is one of the special bits of punctuation that Python have and it's used to indicate the start of a *block* of code, which is a way of saying a collection of code that's grouped together. In Python, we use indentation to indicate blocks, typically a tab. And we can nest them, or put blocks inside of other blocks, as we'll see in a second.

The block inside of our `while` starts with another control structure, `for`. Like `while`, `for` is a loop. Unlike `while`, `for` only runs one for each elements of some sort of group of things. In this case, our `for` is going to run one time for each `value` in a `range()` with 256 values in it. `range()` is function that makes an object that knows how to count some number of values. In this case, our `range()` starts at 0 and counts up to 255. This could also be written as `range(0,256)`, but when a range starts with 0, it is common practice in Python to leave it off. Note that the maximum value in the range is 255, not 256. The maximum value in the range is not counted. I find it easiset to think of this as the number of times it will count, starting at zero.

Alright, so our little program is going to do something 256 times. That something is to set the color of our NeoPixels. For each pass through the `for` loop, it's going to call that `colorwheel()` function we imported earlier. Recall that the function generates a color value when we give it a number. If we were to look at the output of the function, it woudld be a number like `1653119`. This is just a decial number version of a hex value like the one we saw earlier. Don't worry too much about that, though. Just know that this will cause the color of our NeoPixels to get set to various colors of the rainbow, working around a colorwheel, starting with red.

The last bit of code here calls `time.sleep()` and tells the microcontroller to stop doing anything much for the next 0.05 seconds, or 50 milliseconds.

When we run this code on our board, we should see our NeoPixels strobe through a lovely rainbow of colors.