# import RPi.GPIO as GPIO
# from mfrc522 import SimpleMFRC522

# def listen_for_rfid():
#     reader = SimpleMFRC522()
#     try:
#         id, text = reader.read()
#         print(id)
#         print(text)
#     finally:
#         GPIO.cleanup()
