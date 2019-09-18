# First install spidev:
# Enable SPI (sudo raspi-config)
# $ sudo apt-get update 
# $ sudo apt-get upgrade
# $ sudo apt-get install python-dev
# $ sudo reboot
# $ wget https://github.com/doceme/py-spidev/archive/master.zip 
# $ unzip master.zip
# $ cd py-spidev-master
# $ sudo python setup.py install
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from spidev import SpiDev

class MCP3008:
    def __init__(self, bus = 0, device = 0):
        self.bus, self.device = bus, device
        
        self.mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(bus, device))

    def open(self):
        self.spi.open(self.bus, self.device)
    
    def read(self, channel = 0):
        data = self.mcp.read_adc(channel)
        return data
            
    def close(self):
       return 
