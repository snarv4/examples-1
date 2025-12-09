from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
# Pines I2C del ESP32 (por defecto)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
# Mostrar dispositivo I2C detectado
print("Dispositivos I2C encontrados:", i2c.scan())
# Inicializar display OLED 128x64
ancho = 128
alto = 64
oled = SSD1306_I2C(ancho, alto, i2c)
# Mostrar un texto simple
oled.fill(0)  # Limpiar
oled.text("Mocosos feos", 0, 0)
oled.text(":3", 0, 16)
oled.show()