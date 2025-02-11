# Microclass: Physical Computing

What's more fun than programming software? Programming software that interacts with the real world!

![alt text](physical_computing.png)

This is microclass is a very brief introduction to physical computing, a domain of application development the bridges the digital and physical worlds. In this microclass, we will introduce some of the basic concepts of physical computing, especially working with inputs (sensing the physical world) and outputs (effecting the physical world). We'll walk through several example, building up a little working knowledge of the [CircuitPython](https://circuitpython.org) programming language, a development board hardware, and a few programming concepts.

This microclass does not assume that you have a lot of software development experience, or any at all. While this is not an in depth coding tutorial, we will try to highlight so of the main things you need to know. And at the end of the course, there are some resources to help you dig and go deeper, if you wish.

The running time for this microclass is about an hour.

I hope that you enjoy this microclass and find it useful. If you have any questions or feedback, please reach out to me at stonehippo@gmail.com.

## Lessons

- [What You Will Need](#what-you-will-need)
- [Getting Set Up](#getting-set-up)
- [Hello, World](/1_hello_world/README.md)
- [Output: Using Physical Computing to Effect The World](/2_basic_outputs/README.md)
- [A Brief Interlude: A Little About CircuitPython and Microcontrollers](/interlude/README.md)
- [Input: Using Capacitive Touch Sensing](/3_basic_inputs/README.md)
- [Input: Reading A Distance Sensor](/4_sensor_inputs/README.md)
- [Integration: Bring It All Together](/5_integrating_inputs_and_outputs/README.md)
- [Appendix A: Other CircuitPython IDEs](#appendix-a-other-circuitpython-ides)
- [Appendix B: Installing CircuitPython On Your Proximity Trinkey](#appendix-b-installing-circuitpython-on-your-proximity-trinkey)
- [Appendix C: Addtional Resources](#appendix--additional-resources)

## What You Will Need

- [Visual Studio Code](https://code.visualstudio.com/)
- [CircuitPython V2 extension for VSCode](https://marketplace.visualstudio.com/items?itemName=wmerkens.vscode-circuitpython-v2)
- [Adafruit Proximity Trinkey](https://www.adafruit.com/product/5022)

If your computer does not have USB-A ports, you will also need a [USB-A to USB-C adapter](https://www.adafruit.com/product/5030).

## Getting Set Up

### Installing Visual Studio Code

Before we get started, you will need to instal VSCode and the CircuitPython V2 extension. VSCode is a programming-friendly text editor that can act as an integrated development environment (IDE). With the CircuitPython V2 extension installed, VSCode will have a number of tools that make it simpler to work with a CircuitPython development board like the Proximity Trinkey.

### Plugging In Your Development Board

We are using the Proximity Trinkey for this class. It is a small development board that you can plug right into your computer to get started. If you have a USB-A port, you can just plug it in. If not, you'll need to put the board into a USB-A to USB-C adapter to plug in it.

Go ahead and plug the board in now. After a few seconds, you may notice that a new drive is showing up on your system, CIRCUITPY. You might get a message about a new device being added to your system before it will show up. If the CIRCUITPY drive does show up., you're all set and we are almost ready to go.

If you do not see CIRCUITPY, don't panic! Your system may be locked down and will not load external drives (this happens on my work laptop). We can usually still get to development board via the serial port. We'll see how to do that now.

[TK figuring out the board's serial port label]

With VSCode installed and the Proximity Trinkey plugged in, it is time to [get started learning physical computing](/1_hello_world/README.md)!

## Appendix A: Other CircuitPython IDEs

There are a few beginner IDEs for Python out there, that have streamlined interfaces meant to help focus on the task of working with Python. A few of these even have support for CircuitPython and it's progenitor, MicroPython.

Here are a couple that I like:

- [Thonny](https://thonny.org/)
- [Mu](https://codewith.mu/)

I use Thonny quite a bit in when developing and it is my usual first choice for teaching physical computing with CircuitPython. I choose not to use it for this course for a couple of reasons. I am teaching this in a professional environment where many of the attedees of this session may already be programmers and are likely to have VSCode.

Thonny is great, but it does some tricks when talking to the board that make code execution simpler for development, but doesn't play that well with the relatively low-power SAM21 microcontroller at the heart of the Proximity Trinkey. 

With these factors in mind, the closer-to-the-metal VSCode + CircuitPython V2 extension is a slightly better choice for this class. That said, I really recommend getting Thonny or Mu (or both!). They will help you learn and code CircuitPython.

## Appendix B: Installing CircuitPython on Your Proximity Trinkey

The Adafruit Proximity Trinkey ships with a pre-installed example, built using Arduino. To use that development board, you need to install CircuitPython on it. Fortunately, this is pretty easy to do.

- [Installing CircuitPython on the Proximity Trinkey](https://learn.adafruit.com/adafruit-proximity-trinkey/circuitpython)
- [The latest CircuitPython firmware for the Proximity Trinkey](https://circuitpython.org/board/adafruit_proxlight_trinkey_m0/)

## Appendix C: Additional Resources

If you want to go further, here are a few resources that you can use to learn more about physical computing with CircuitPython.

- [CircuitPython.org](https://circuitpython.org) - the home site for CircuitPython, including links to downloads, libraries, documentation, and more.
- [Awesome CircuitPython](https://circuitpython.org/awesome) - A catalog of CircuitPython Resources.
- [Welcome to CircuitPython!](https://learn.adafruit.com/welcome-to-circuitpython) - an ideal place to get started learning about CircuitPython. 
- [CircuitPython Essentials](https://learn.adafruit.com/circuitpython-essentials) - The next level of CircuitPython learning, with guides on how to do specific tasks, including multiple types of inputs and outputs.
- [CircuitPython Documentation] - in-depth docs on CircuitPython and its built-in modules.
- [Learn Guide: Adafruit Proximity Trinkey](https://learn.adafruit.com/adafruit-proximity-trinkey) - guide focused on the development board that we use in this class.
-


### A Brief Note On CircuitPython Development Boards

Lastly, I choose the Proxmity Trinkey for this class because it is simple, has integrated devices for input and output, and is cheap. It is a good choice for an introduction to physical computing, but it is hardly the device I would recommend if you to do more. For that, you have a whole host of choices; the CircuitPython.org site lists [dozens of compatible devices](https://circuitpython.org/downloads). There are several good choices, but I recommend starting with the [Adafruit Feather RP2040](https://www.adafruit.com/product/4884).

The Feather RP2040 is built around the [RP2040 microcontroller](https://www.raspberrypi.com/products/rp2040/), designed by Raspberry Pi. It has decent speed, peripherals, and is not too expensive. Adafruit has built a nice selection of add-on boards for their Feather line, known as FeatherWings, the can expand the functionality of the development board. And they also have several variants of the basic Feather RP2040 for specific uses. One of my favorites is the [Feather RP2040 PropMaker](https://www.adafruit.com/product/5768), which is set up for lots of fun outputs and inputs, including audio

-----

Microclass: Physical Computing copyright &copy; 2025 George White