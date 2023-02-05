####################################################################
#############          Cycling LED Gradient            #############
####################################################################

# >> Imports
from machine import Pin
from lightingEffects import cycle
import machine
import neopixel

# from lightingEffects import bounce, clear as clr, cycle, wheel, rainbowCycle


# >> Constants

n = 18 # Number of LEDs
p = 14 # GPIO Pin connected to the LED strip

np = neopixel.NeoPixel(machine.Pin(p), n) # Create NeoPixel object

# Iterates through the LEDs in order to create the gradient


# Empty list to store the RGB values
colors = []


def generateGradient(color = "red"):  
    # [(18, 0, 0), (36, 0 0), (54, 0 0), (72, 0, 0), (90, 0, 0), (108, 0, 0), (126, 0, 0), (144, 0, 0), 
    # (162, 0, 0), (180, 0, 0), (198, 0, 0), (216, 0, 0), (234, 0, 0), (252, 0, 0)
            
    pix = divmod(255, n) # 255/14 = 18 r 2
    print(pix)
    
    for i in range(1, n):
        # for j in pix[1]:
    #         # return list of RGB values
            if color == "red":
                cycle(255, 0, 255, 15)
                np[i] = (pix[0] * i, 0, 0)
            elif color == "green":
                np[i] = (0, pix[0] * i, 0)
            else:
                np[i] = (0, 0, pix[0] * i)
            colors.append(np[i])
            np.write()
    return colors
print(generateGradient("blue"))
# print(generateGradient(green))