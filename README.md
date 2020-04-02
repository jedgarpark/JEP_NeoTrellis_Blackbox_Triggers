# NeoTrellis_Blackbox_Triggers & NeoTrellis_M4_Blackbox Triggers
Two versions now! 

NeoTrellis M4 8x4 pad for launching both sequences _and_ samples via USB MIDI on 1010 music Blackbox

[![Trellis demo](http://img.youtube.com/vi/p99yabXg0xk/0.jpg)](https://youtu.be/p99yabXg0xk)

# 8x4 Version Runs on Adafruit NeoTrellis M4 with CircuitPython 5.0.0 or newer.
## Parts
- [NeoTrellis M4](https://www.adafruit.com/product/3938)

- [Elastomer pads x2](https://www.adafruit.com/product/1611)

- [Here's a kit version](https://www.adafruit.com/product/4020) with all the parts you need.


## Setup and Installation:
- Set up the board and enclosure as shown here:
https://learn.adafruit.com/adafruit-neotrellis-m4

 - Install CircuitPython:
https://learn.adafruit.com/adafruit-neotrellis-m4/circuitpython

- Add libraries to /lib directory on NeoTrellis M4 CIRCUITPY drive as shown here:
https://learn.adafruit.com/adafruit-neotrellis-m4/adafruit-circuitpython-trellism4-library

### The libraries you'll need are:
- adafruit_matrixkeypad.mpy
- adafruit_midi
- adafruit_trellism4.mpy
- neopixel.mpy

To get them, [download the 5.x library bundle from here](https://circuitpython.org/libraries), extract the .zip, and drag over the ones you need.

## Code
Adafruit recommends using the **Mu** editor for using your CircuitPython code with the Feather boards. [You can get more info in this guide](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor).

Download the **neotrellis_m4_blackbox_triggers.py** file linked above in this repo and open it into **Mu**. Plug your NeoTrellis M4 into your computer via a known good USB cable. In your operating system's file explorer/finder, you should see a new flash drive named CIRCUITPY. Save the code from Mu to the NeoTrellis M4's CIRCUITPY drive as code.py (that's the name of the program that will automatically run when the board restarts).

## Usage
Plug the NeoTrellis M4 into your Blackbox with a microUSB data/power cable (not power only!).

When the NeoTrellis M4 boots up, it will display magenta pads on the left and cyan sequence triggers on the right.

### Sample Pads 
Press the a sample button and it'll start in sample playback mode, mimicking the Pads screen. To use, press a button to trigger the corresponding blackbox Pads sample. Hold a button to loop the sample, if it's set to loop. Releasing a pad sends a MIDI Note Off message.

### Sequence Trigger mode
Press a cyan button on the right to toggle on the corresponding sequence on the blackbox. Press the button a second time to toggle that sequence off.


# NeoTrellis 4x4 pad for launching sequences or samples (choose a mode at startup) via USB MIDI on 1010 music Blackbox

[![Trellis demo](http://img.youtube.com/vi/ZG33SLi7mFo/0.jpg)](http://www.youtube.com/watch?v=ZG33SLi7mFo)

4x4 Version Runs on Adafruit NeoTrellis 4x4 driver board and Feather M4 with CircuitPython 5.0.0 or newer.
## Parts
- [Feather M4](https://www.adafruit.com/product/3857)

- [NeoTrellis driver board](https://www.adafruit.com/product/3954)

- [Elastomer pad](https://www.adafruit.com/product/1611)

- [Wiring](https://www.adafruit.com/product/3955)

- [rubber bumper feet](https://www.adafruit.com/product/550)


- [Here's a kit version](https://www.adafruit.com/product/4352) with all the parts you need.



## Setup and Installation:
- Wire the NeoTrellis and Feather as shown here:
https://learn.adafruit.com/adafruit-neotrellis/circuitpython-code

 - Install CircuitPython on the Feather:
https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/circuitpython

- Add libraries to /lib directory on Feather CIRCUITPY drive as shown here:
https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/circuitpython-libraries

### The libraries you'll need are:
- adafruit_neotrellis
- adafruit_seesaw
- adafruit_bus_device
- adafruit_midi

To get them, [download the 5.x library bundle from here](https://circuitpython.org/libraries), extract the .zip, and drag over the ones you need.

## Code
Adafruit recommends using the **Mu** editor for using your CircuitPython code with the Feather boards. [You can get more info in this guide](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor).

Download the **neotrellis_blackbox_triggers.py** file linked above in this repo and open it into **Mu**. Plug your Feather M4 into your computer via a known good USB cable. In your operating system's file explorer/finder, you should see a new flash drive named CIRCUITPY. Save the code from Mu to the Feather's CIRCUITPY drive as code.py (that's the name of the program that will automatically run when the board restarts).

## Usage
Plug the NeoTrellis/Feather M4 into your Blackbox with a microUSB data/power cable (not power only!).

When the NeoTrellis boots up it will display all white pixels, and then go to config mode with the bottom left pixel magenta and bottom right cyan.

This is where you can pick either sample pad mode or sequence trigger mode.

### Sample Pads mode
Press the bottom left magenta button and it'll start in sample playback mode, mimicking the Pads screen. To use, press a button to trigger the corresponding blackbox Pads sample. Hold a button to loop the sample, if it's set to loop.

### Sequence Trigger mode
During the config screen choice, hit the bottom right cyan button to choose Sequence Trigger mode. Now, you can press a button to toggle on the corresponding sequence on the blackbox. Press the button a second time to toggle that sequence off.
