## Using individually addressable LED strips to simulate a gradient effect ##

# >> Imports
from machine import Pin
import machine
import neopixel
import time


# >> LED strip configuration
n = 18  # Number of LEDS on strip
p = 14  # GPIO Pin number
np = neopixel.NeoPixel(machine.Pin(p), n)

# >> Functions for lighting effects
# Bounce


def bounce(r, g, b, wait):
    for i in range(2 * n):
        for j in range(n):
            np[j] = (r, g, b)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(wait)

# cycle


def cycle(r, g, b, wait):
    for i in range(n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (r, g, b)
        print(i % n)
        np.write()
        time.sleep_ms(wait)

# function to go through all colors


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    """

    Args:
        pos (int): _description_

    Returns:
        _type_: _description_
    """    
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

# rainbow


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(n):
            rc_index = (i * 256 // n) + j
            np[i] = wheel(rc_index & 255)
        np.write()
        time.sleep_ms(wait)


def clear():  # Sets all LEDs on strip to (0,0,0) color to clear set colors
    for i in range(n):
        np[i] = (0, 0, 0)
        np.write()


# >> Main
#while True:
    # print("Cycling...")
    #cycle(38, 0, 45, 85)

    # print("Rainbow Cycling...")
    # todo: debug rainbow_cycle function and integrate it into the program
    # rainbow_cycle(3000)
    # rainbow_cycle(1)
