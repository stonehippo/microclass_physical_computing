# Input: measuring disttance with a proximity sensor!
import time
import board

from adafruit_apds9960.apds9960 import APDS9960

i2c = board.I2C()
apds = APDS9960(i2c)
apds.proximity_gain = 2 
apds.enable_proximity = True

while True:
	print(apds.proximity)
	time.sleep(0.25)