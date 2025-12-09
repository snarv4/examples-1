#funciones
import machine
import time
import neopixel

PIN = 4
NUM_PIX = 3
np = neopixel.NeoPixel(machine.Pin(PIN), NUM_PIX)
np[0] = (100, 50, 20)
np[1] = (0, 255, 0)
np[2] = (0, 0, 255)
np.write()
