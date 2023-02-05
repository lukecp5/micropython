## Using individually addressable LED strips to simulate a gradient effect ##

#>> Imports
import machine, neopixel

#>> LED strip configuration
n = 18 ## Number of LEDS on strip
p = 14 ## GPIO Pin number
np = neopixel.NeoPixel(machine.Pin(p), n) 


## cycle
def cycle(r, g, b, wait):
  for i in range(n):
    for j in range(n):
      np[j] = (0, 0, 0)
    np[i % n] = (r, g, b)
    np.write()
    time.sleep_ms(wait)


## rainbow 
def rainbow_cycle(wait):
  for j in range(255):
    for i in range(n):
      rc_index = (i * 256 // n) + j
      np[i] = wheel(rc_index & 255)
    np.write()
    time.sleep_ms(wait)
def clear(): # Sets all LEDs on strip to (0,0,0) color to clear set colors
  for i in range(n):
    np[i] = (0, 0, 0)
    np.write()

#>> Main 
np[0] = (255, 0, 0)
np[2] = (125, 204, 223)
np[4] = (120, 153, 23)
np[6] = (255, 0, 153)

np.write()
