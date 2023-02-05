## Neopixel Library Testing
#>> Imports
import machine, neopixel

#>> Functions
n = 18 ## Number of LEDS on strip
p = 14 ## GPIO Pin number

#* Create a NeoPixel object called np on the GPIO you’ve defined earlier
np = neopixel.NeoPixel(machine.Pin(p), n) 

np[0] = (255, 0, 0)
np[2] = (125, 204, 223)
np[4] = (120, 153, 23)
np[6] = (255, 0, 153)
np.write()