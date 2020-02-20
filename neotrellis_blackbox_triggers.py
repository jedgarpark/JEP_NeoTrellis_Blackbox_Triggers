# NeoTrellis Blackbox Triggers for Samples/Sequences
# John Park
# February 20, 2020
# version 0.5
# GPL 3.0 License

# NeoTrellis 4x4 driver board + Feather M4 Express
# running CircuitPython 5 or newer

import time
from board import SCL, SDA
import busio
from adafruit_neotrellis.neotrellis import NeoTrellis
import usb_midi
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff

# create the i2c object for the trellis
i2c_bus = busio.I2C(SCL, SDA)

# create the trellis
trellis = NeoTrellis(i2c_bus)

# color definitions
OFF = (0, 0, 0)
CYAN = (0, 16, 16)
ORANGE = (30, 20, 0)
MAGENTA = (15, 0, 30)
WHITE = (5, 5, 6)

STARTUP_COLOR = WHITE
COLOR_A = MAGENTA
COLOR_B = CYAN

midi_channel = 1  # change this if you want to send on a different MIDI channel

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=midi_channel-1)

button_mode = 0  # mode 0 for samples / mode 1 for sequences
config_mode = 1  # state for startup config

# remap NeoTrellis physical buttons to logical buttons that start at lower left as 0
button_map = [12, 13, 14, 15,
               8,  9, 10, 11,
               4,  5,  6,  7,
               0,  1,  2,  3]

# variable list to store toggled state of button presses
button_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# function called during configuration to map the MIDI notes
def set_button_mode(mode):
    global button_mode
    global note_map
    if mode is 0:
        button_mode = 0
        note_map = [36, 37, 38, 39,  # this corresponds to 1010music blackbox pads, 0 index is lower left
                    40, 41, 42, 43,
                    44, 45, 46, 47,
                    48, 49, 50, 51]
    elif mode is 1:
        button_mode = 1
        note_map = [52, 53, 54, 55,  # this corresponds to 1010music blackbox sequences, 0 index is lower left
                    56, 57, 58, 59,
                    60, 61, 62, 63,
                    64, 65, 66, 67]

# function called when one of the config buttons is used
def config_check(event):
    global config_mode
    global COLOR_A
    global COLOR_B
    if event.edge == NeoTrellis.EDGE_FALLING:  # when button is released
        if event.number is 12:
            print("Sample Pad mode.")
            set_button_mode(0)
            config_mode = 0
            COLOR_A = CYAN
            COLOR_B = MAGENTA
            for i in range(16):
                trellis.pixels[i] = COLOR_B
                time.sleep(.05)

        elif event.number is 15:
            print("Sequence Trigger mode.")
            set_button_mode(1)
            config_mode = 0
            COLOR_A = MAGENTA
            COLOR_B = CYAN
            for i in range(16):
                trellis.pixels[i] = COLOR_B
                time.sleep(.05)

# this will be called when button events are received
def trigger(event):
    if config_mode is 1:
        config_check(event)

    elif config_mode is 0:
        # sampler mode actions
        if button_mode is 0:
            # trigger on when a rising edge is detected
            if event.edge == NeoTrellis.EDGE_RISING:
                trellis.pixels[event.number] = COLOR_A
                button = button_map[event.number]  # use the reindexed button numbering
                note = note_map[button]
                # print("Pixel "+str(event.number)+" pressed.")  # debug only of physical buttons
                print("Button "+str(button)+" pressed.")
                midi.send(NoteOn(note, 127))
                print("Note On: "+str(note))

            # trigger off when a rising edge is detected for pad mode
            elif event.edge == NeoTrellis.EDGE_FALLING:
                trellis.pixels[event.number] = COLOR_B
                button = button_map[event.number]
                note = note_map[button]
                # print("Button "+str(event.number)+" released")
                print("Button "+str(button)+" released.")
                midi.send(NoteOff(note, 0))
                print("Note Off: "+str(note))

        # sequencer mode actions
        elif button_mode is 1:
            # trigger on when a rising edge is detected
            if event.edge == NeoTrellis.EDGE_RISING:
                if button_state[event.number] is 0:
                    trellis.pixels[event.number] = COLOR_A
                    button_state[event.number] = 1
                else:
                    trellis.pixels[event.number] = COLOR_B
                    button_state[event.number] = 0
                button = button_map[event.number]  # use the reindexed button numbering
                note = note_map[button]
                # print("Pixel "+str(event.number)+" pressed.")  # debug only of physical buttons
                print("Button "+str(button)+" pressed.")
                midi.send(NoteOn(note, 127))
                print("Note On: "+str(note))


for i in range(16):
    # activate rising edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    # activate falling edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    # set all keys to call the trigger callback
    trellis.callbacks[i] = trigger

    # cycle the LEDs on startup
    trellis.pixels[i] = STARTUP_COLOR
    time.sleep(.05)

for i in range(16):
    trellis.pixels[i] = WHITE
    time.sleep(.05)

trellis.pixels[12] = COLOR_A  # light bottom left pixel for picking mode 0
trellis.pixels[15] = COLOR_B  # light bottom right pixel for picking mode 1


while True:
    # call the sync function call any triggered callbacks
    trellis.sync()
    # the trellis can only be read every 17 milliseconds or so
    time.sleep(.02)
