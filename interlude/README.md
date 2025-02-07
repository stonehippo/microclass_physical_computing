# A Brief Interlude: A Little About CircuitPython and Microcontrollers

CircuitPython is a version of the popular Python programming language, design to work on microcontrollers like the little SAMD21 on the Proximity Trinkey we're working with today.

Microcontrollers are tiny computers that are particularly suited to physical computing because of their "real time" nature. They don't have an operating system and the usually have peripherals that make it easy to work with the real world.

There are a lot of microcontrollers out there and over the past couple of decades, development boards and programming tools and languages have been created to make it easier and more accesible to get started with them. The popular Arduino series of tools was responsible for lowering this bar a lot, and things have only gotten simpler in the time since they appeared.

CircuitPython is a nice evolution of these tools for a few reasons. One, it uses Python, which is great language for all levels of coders. Two, CircuitPython is *interpreted*, which means that code code be written and run immediately. This means you do not have to do the write-compile-upload-test loop that a *compiled* toolset like Arduino requires. This makes working with the development board simpler and getting up to speed faster. Lastly, CircuitPython *usually* support native USB access, which means that the development board shows on like a tiny thumd drive when plugged in to a computer. You can drag and drop files on the drive or edit them direcly. This means you don't need any fancy custom tools to program a microcontroller—a decent text editor will do the trick.

Another nice thing about CircuitPython is the REPL, or Read-Evaluate-Print-Loop, that lets you write code line by line and have it execute immediately. This is a great way to test out code or see errors.