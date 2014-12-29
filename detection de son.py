import RPi.GPIO as GPIO
import time


RED=21                          
GREEN=26
SIGNAL=6

class Detection(object):
    def __init__(self):
        self.f = 0
        self.char = []
        self.sync = 0
        GPIO.cleanup() # clean anciens réglages
        GPIO.setmode(GPIO.BCM) # définit le type d'adressage
        GPIO.setup(RED, GPIO.OUT,initial=True) # définit comme sortie
        GPIO.setup(GREEN, GPIO.OUT,initial=False) # définit comme sortie
        GPIO.setup(SIGNAL, GPIO.IN) # définit comme entrée
        GPIO.add_event_detect(SIGNAL,GPIO.RISING,callback=self.on)
        self.char = None
        GPIO.output(RED, True)
        GPIO.output(GREEN, False)

    def on(self,caca):
        self.bit = 1
        GPIO.remove_event_detect(SIGNAL)
        GPIO.output(RED, False)
        GPIO.output(GREEN, True)
        time.sleep(0.07)
        GPIO.add_event_detect(SIGNAL,GPIO.RISING,callback=self.on)
        GPIO.output(RED, True)
        GPIO.output(GREEN, False)

    def listen(self):
        while True:
            cpt = 0
            if self.bit == 1:
                self.char = []
                while cpt < 8:
                    self.bit = 0
                    time.sleep(0.07)
                    if self.bit == 1:
                        self.char.append('1')
                    else:
                        self.char.append('0')
                    cpt += 1
                self.bit = 0
                print (self.char)
                
                

try:
    a = Detection().listen()
except:
    print (a.f)

    

        


       
        
    
    
    
            
 
