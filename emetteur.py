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
        p = GPIO.PWM(OUT, 300)
        p.start(5)
        time.sleep(LEVEL)
        p.stop()
        
    def send_payload(self, payload):
        for char in payload:
            self.send_byte()
            time.sleep(LEVEL)
            binary = bin(ord(char))[2:]
            for i in range(0, len(binary) - 1):
                if binary[i] == '1':
                    self.send_byte()
                else:
                    time.sleep(LEVEL)
                time.sleep(LEVEL)
            while i < 7:
                time.sleep(LEVEL)
                i += 1
                
    def listen(self):
        while True:
            payload = str(input("Chat : "))
            self.send_payload(payload)
            
instance = Emetteur()
instance.listen()
GPIO.cleanup()
