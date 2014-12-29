import RPi.GPIO as GPIO
import time


RED=21                          
GREEN=26
SIGNAL=6

class Detection(object):
    def __init__(self):
        self.f = 0
        GPIO.cleanup() # clean anciens réglages
        GPIO.setmode(GPIO.BCM) # définit le type d'adressage
        GPIO.setup(RED, GPIO.OUT,initial=True) # définit comme sortie
        GPIO.setup(GREEN, GPIO.OUT,initial=False) # définit comme sortie
        GPIO.setup(SIGNAL, GPIO.IN) # définit comme entrée
        GPIO.add_event_detect(SIGNAL,GPIO.RISING,callback=self.on)
        self.char = None
        self.mode = 0
        GPIO.output(RED, True)
        GPIO.output(GREEN, False)

    def on(self,caca):
        self.bit = 1
        self.mode = 1
        GPIO.remove_event_detect(SIGNAL)
        GPIO.output(RED, False)
        GPIO.output(GREEN, True)
        time.sleep(0.07)
        self.mode = 0
        GPIO.add_event_detect(SIGNAL,GPIO.RISING,callback=self.on)
        GPIO.output(RED, True)
        GPIO.output(GREEN, False)

    while True
        

        while

try:
    a = Detection()
except:
    print (a.f)

    

        


       
        
    
    
    
            
 
