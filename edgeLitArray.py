## Using individually addressable LED strips to simulate a gradient effect ##

# >> Imports
import time, machine, neopixel
from machine import Pin
from effects import cycle

# >> Constants
n = 17  # Number of LEDS on strip
p = 14  # GPIO Pin number
np = neopixel.NeoPixel(machine.Pin(p), n)

# Cycle
def cycle(r, g, b, wait):
    for i in range(n//2):
        for j in range(n):
            np[j] = (0, 0, 0)
        cnt = i%n
        print((n - cnt))
        # TUrn the next led on
        np[i % n] = (r, g, b)
        np[i % n + 7] = (r, g, b)
        
        print(cnt, "np[i % n]", list(np[i % n]))
        print(cnt, "np[n - cnt]", list(np[2 * cnt]))
        np.write()
        time.sleep_ms(wait)
        

def clear():  # Sets all LEDs on strip to (0,0,0) color to clear set colors
    for i in range(n):
        np[i] = (0, 0, 0)
        np.write()


# >> Main
while True:
    #print("Cycling...")
    cycle(30, 30, 30, 1000)
    #rainbow_cycle(100)
    # print("Rainbow Cycling...")
    # todo: debug rainbow_cycle function and integrate it into the program
    # rainbow_cycle(3000)
    # rainbow_cycle(1)

