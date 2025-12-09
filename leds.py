from machine import Pin
import time

led_uno = Pin(12, Pin.OUT)  # Onboard LED for many ESP32 boards

led_uno.on()   # Turn LED on
time.sleep(1)  # Wait for 1 second
led_uno.off()  # Turn LED off
time.sleep(1)  # Wait for 1 second