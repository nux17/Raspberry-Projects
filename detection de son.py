import RPi.GPIO as GPIO
import time
import sys


RED=21                          
GREEN=26
SIGNAL=6

class Detection(object):
    def __init__(self):
        self.f = 0
        self.char = []
        self.sync = 0
        self.bit=0
        GPIO.cleanup() # clean anciens reglages
        GPIO.setmode(GPIO.BCM) # definit le type d'adressage
        GPIO.setup(RED, GPIO.OUT,initial=True) # definit comme sortie
        GPIO.setup(GREEN, GPIO.OUT,initial=False) # definit comme sortie
        GPIO.setup(SIGNAL, GPIO.IN) # definit comme entree
        GPIO.output(RED, True)
        GPIO.output(GREEN, False)

    def on(self,caca):
        self.bit = 1
        GPIO.remove_event_detect(SIGNAL)
        GPIO.output(RED, False)
        GPIO.output(GREEN, True)
        time.sleep(0.05)
        GPIO.output(RED, True)
        GPIO.output(GREEN, False)
        GPIO.add_event_detect(SIGNAL,GPIO.RISING,callback=self.on)

    def listen(self):
        GPIO.add_event_detect(SIGNAL,GPIO.RISING,callback=self.on)
        while True:
            cpt = 0
            if self.bit == 1:
                time.sleep(0.05)
                self.char = []
                while cpt < 8:
                    self.bit = 0
                    time.sleep(0.05)
                    if self.bit == 1:
                        self.char.append('1')
                    else:
                        self.char.append('0')
                    cpt += 1
                self.bit = 0
                print (str(self.char))



a = Detection()
a.listen()


    

        


       
        
    
    
    
            
 
