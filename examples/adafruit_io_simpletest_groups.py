"""
Example of performing group operations
"""
import board
import busio
from digitalio import DigitalInOut

# ESP32 SPI
from adafruit_esp32spi import adafruit_esp32spi, adafruit_esp32spi_wifimanager

# Import Adafruit IO REST Client
from adafruit_io.adafruit_io import RESTClient

# Get wifi details and more from a wifi_settings.py.py file
try:
    from wifi_settings import settings
except ImportError:
    print("WiFi settings are kept in wifi_settings.py.py, please add them there!")
    raise


# ESP32 Setup
esp32_cs = DigitalInOut(board.D9)
esp32_ready = DigitalInOut(board.D10)
esp32_reset = DigitalInOut(board.D5)
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)
wifi = adafruit_esp32spi_wifimanager.ESPSPI_WiFiManager(esp, settings, board.NEOPIXEL)

"""
# PyPortal ESP32 Setup
import microcontroller
esp32_cs = DigitalInOut(microcontroller.pin.PB14)
esp32_ready = DigitalInOut(microcontroller.pin.PB16)
esp32_reset = DigitalInOut(microcontroller.pin.PB17)
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)
wifi = adafruit_esp32spi_wifimanager.ESPSPI_WiFiManager(esp, settings, board.NEOPIXEL)
"""

# Set your Adafruit IO Username and Key in wifi_settings.py
# (visit io.adafruit.com if you need to create an account,
# or if you need your Adafruit IO key.)
ADAFRUIT_IO_USER = settings['adafruit_io_user']
ADAFRUIT_IO_KEY = settings['adafruit_io_key']

# Create an instance of the Adafruit IO REST client
io = RESTClient(ADAFRUIT_IO_USER, ADAFRUIT_IO_KEY, wifi)

# Create a new group
print('Creating a new Adafruit IO Group...')
sensor_group = io.create_new_group('envsensors', 'a group of environmental sensors')

# Add the 'temperature' feed to the group
print('Adding feed temperature to group...')
io.add_feed_to_group(sensor_group['key'], 'temperature')

# Get info from the group
print(sensor_group)

# Delete the group
print('Deleting group...')
io.delete_group('envsensors')