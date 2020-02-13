# JEP_NeoTrellis_Blackbox_Triggers
NeoTrellis pad for launching sequences or samples via USB MIDI on 1010 music Blackbox

Runs on Adafruit NeoTrellis 4x4 driver board and Feather M4 with CircuitPython 5.0.0 or newer.

Setup and Installation:
- Wire the NeoTrellis and Feather as shown here:
https://learn.adafruit.com/adafruit-neotrellis/circuitpython-code

 - Install CircuitPython on the Feather:
https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/circuitpython

- Add libraries to /lib directory on Feather CIRCUITPY drive as shown here:
https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/circuitpython-libraries

The libraries you'll need are:
- adafruit_neotrellis
- adafruit_seesaw
- adafruit_bus_device
- adafruit_midi


## Code
Adafruit recommends using the Mu editor for using your CircuitPython code with the Feather boards. You can get more info in this guide.

Download the neotrellis_blackbox_triggers.py and open it into Mu. Plug your Feather M4 into your computer via a known good USB cable. In your operating system's file explorer/finder, you should see a new flash drive named CIRCUITPY. Save the code from Mu to the Feather's CIRCUITPY drive as code.py (that's the name of the program that will automatically run when the board restarts).

## Usage
Plug the NeoTrellis/Feather M4 into your Blackbox with a microUSB data/power cable (not power only!).

When the NeoTrellis boots up it will display all white pixels, and then go to config mode with the bottom left pixel magenta and bottom right cyan.

This is where you can pick either sample pad mode or sequence trigger mode.

### Sample Pads mode
Press the bottom left magenta button and it'll start in sample playback mode, mimicking the Pads screen. To use, press a button to trigger the corresponding blackbox Pads sample. Hold a button to loop the sample, if it's set to loop.

### Sequence Trigger mode
During the config screen choice, hit the bottom right cyan button to choose Sequence Trigger mode. Now, you can press a button to toggle on the corresponding sequence on the blackbox. Press the button a second time to toggle that sequence off.
