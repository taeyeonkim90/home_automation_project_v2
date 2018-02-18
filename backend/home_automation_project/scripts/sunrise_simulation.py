from __future__ import division
import time
import sys
import multiprocessing

import RPi.GPIO as GPIO

from bibliopixel.led import *
from bibliopixel.drivers.LPD8806 import *


WAIT_INTERVAL = 1.17
NUMBER_OF_LED = 96


class SunriseSimulator(multiprocessing.Process):
	"""This class is to interact with LPD8806 digital RGB strip simulating sunrise effect"""
	
	def __init__(self, name):
		multiprocessing.Process.__init__(self)
		self.name = name
		self.driver = DriverLPD8806(NUMBER_OF_LED,c_order=ChannelOrder.GRB)
		self.led = LEDStrip(self.driver)

	def run(self):
		"""turns on all led bulbs gradually from dim red to bright white light"""
		driver = self.driver
		led = self.led
		
		#RGB pixel status
		r=0
		g=0
		b=0
		
		#Gradual red light increase
		for red in range(256):
			r = red
			led.fillRGB(r,g,b)
			led.update()
#			print (r,g,b)
			time.sleep(WAIT_INTERVAL)
		
		#green and blue light intensity increase	
		for n in range(256):
			g = n
			led.fillRGB(r,g,b)
			led.update()
#			print (r,g,b)
			time.sleep(WAIT_INTERVAL)
		
			b = n
			led.fillRGB(r,g,b)
			led.update()
#			print (r,g,b)
			time.sleep(WAIT_INTERVAL)

		while True:
			pass


	def turn_off_led(self):
		"""turns off all the led lights"""
		self.led.all_off()
		self.led.update()

       
class ButtonListener():
	def __init__(self):
		return
		
	def activate_button(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	def button_is_clicked(self):
		input_state = GPIO.input(18)
		if input_state == False:
			print 'Button is clicked'
			return True
		return False

		
if __name__ == "__main__":
	try:
		#initialize led controller and button listener
		sunrise_instance = SunriseSimulator("LED_Controller")
		button_listener = ButtonListener()
		button_listener.activate_button()
		
		#start turning on led with seperate process
		sunrise_instance.start()
		
		#listen for button click event
		while not button_listener.button_is_clicked():
			pass
	
		#terminate the process run and turn off all the light
		sunrise_instance.terminate()
		sunrise_instance.turn_off_led()

	except KeyboardInterrupt:
		pass




