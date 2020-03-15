import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
	text = input('New data: ')
	print('place data to write')
	reader.write(text)
	print('done')
finally:
	GPIO.cleanup()
