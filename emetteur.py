import RPi.GPIO as GPIO
import time
import sys
import random
import os

OUT = 16
LEVEL = 0.05

class Emetteur(object):
    def __init__(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(OUT, GPIO.OUT, initial=False)

    def send_byte(self):
        p = GPIO.PWM(OUT, 120)
        p.start(20)
        time.sleep(LEVEL)
        p.stop()
        
    def send_payload(self, payload):
        for char in payload:
            self.send_byte()
            time.sleep(LEVEL)
            binary = bin(ord(char))[2:]
            while len(binary) < 8:
                binary = "0" + binary
            for i in range(0, len(binary)):
                if binary[i] == '1':
                    self.send_byte()
                else:
                    time.sleep(LEVEL)
            
    def listen(self):
        while True:
            payload = str(input("Chat : ")) + "\n"
            self.send_payload(payload)
            
instance = Emetteur()
instance.listen()
GPIO.cleanup()
