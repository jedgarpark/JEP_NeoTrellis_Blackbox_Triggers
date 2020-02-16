# NeoTrellis M4 8x4 Blackbox Trigger Samples/Sequences
# John Park
# February 16, 2020
# version 0.3

import time
import adafruit_trellism4
import usb_midi
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff

# create the trellis
trellis = adafruit_trellism4.TrellisM4Express()

led_on = []

for x in range(trellis.pixels.width):
    led_on.append([])
    for y in range(trellis.pixels.height):
        led_on[x].append(False)

# color definitions
OFF = (0, 0, 0)
CYAN = (0, 16, 16)
ORANGE = (30, 20, 0)
MAGENTA = (15, 0, 30)
PINK = (20, 0, 15)
AQUA = (0, 8, 18)
# WHITE = (5, 5, 6)

COLOR_A = AQUA
COLOR_B = PINK
COLOR_C = MAGENTA
COLOR_D = CYAN

for x in range(4):
    for y in range(4):
        trellis.pixels[x, y] = COLOR_B
        time.sleep(0.02)

for x in range(4, 8):
    for y in range(4):
        trellis.pixels[x, y] = COLOR_D
        time.sleep(0.02)

current_press = set()

midi_channel = 1  # change this if you want to send on a different MIDI channel

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=midi_channel-1)


# button mappings into logical grids of MIDI notes for blackbox

note_map = {
    (0,3): (36),  # left 16 corresond to blackbox PADS sample cells
    (1,3): (37),
    (2,3): (38),
    (3,3): (39),

    (0,2): (40),
    (1,2): (41),
    (2,2): (42),
    (3,2): (43),

    (0,1): (44),
    (1,1): (45),
    (2,1): (46),
    (3,1): (47),

    (0,0): (48),
    (1,0): (49),
    (2,0): (50),
    (3,0): (51),


    (4,3): (52),  # right 16 correspond to blackbox SEQS sequence launch cells
    (5,3): (53),
    (6,3): (54),
    (7,3): (55),

    (4,2): (56),
    (5,2): (57),
    (6,2): (58),
    (7,2): (59),

    (4,1): (60),
    (5,1): (61),
    (6,1): (62),
    (7,1): (63),

    (4,0): (64),
    (5,0): (65),
    (6,0): (66),
    (7,0): (67)
    }

while True:
    pressed = set(trellis.pressed_keys)  # a button is pressed

    for press in pressed - current_press:  # press down event
        x, y = press  # get the address of the pressed button
        print(" ")
        print("Pressed: ", press)

        # Send MIDI Note On message
        if press in note_map:  # send MIDI message
            midi.send(NoteOn(note_map[press], 64))  # midi on, velocity 64
            print("MIDI On: ", note_map[press])

        # Simple color change for momentary pads
        if x < 4:  # left pads
            trellis.pixels[x, y] = COLOR_A
            print("Pad LED press blue:", press)

        # Change the color & toggle state of sequence buttons
        else:
            if not led_on[x][y]:
                print("Toggle Sequence LED on:", press)
                trellis.pixels[x, y] = COLOR_C
                led_on[x][y] = True
            else:
                print("Toggle Sequence LED off:", press)
                trellis.pixels[x, y] = COLOR_D
                led_on[x][y] = False


    for release in current_press - pressed:  # release up event
        x, y = release  # get the address of the released button
        print(" ")
        print("Released: ", release)
        if release in note_map:
            if x < 4:  # only send message for Pads, not sequences
                trellis.pixels[x, y] = COLOR_B
                midi.send(NoteOff(note_map[release], 0))  # midi off, velocity 0
                print("MIDI Off: ", note_map[release])
                print("Pad LED release pink: ", release)


    current_press = pressed
