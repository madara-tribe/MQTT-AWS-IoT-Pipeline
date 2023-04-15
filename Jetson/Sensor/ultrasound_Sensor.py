# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO

class Ultrasound_Sensor():
    def __init__(self, hyp):
        self.__TRIG = hyp['TRIG_PIN'] # 19 pin
        self.__ECHO = hyp['ECHO_PIN'] # 21 pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD) 
        GPIO.setup(self.__TRIG,GPIO.OUT)
        GPIO.setup(self.__ECHO,GPIO.IN)
        self.sound_speed = hyp['sound_speed'] #[cm/s]
        
    def getDistance(self):
        GPIO.output(self.__TRIG, GPIO.LOW)
        # TRIG = HIGH
        GPIO.output(self.__TRIG, True)
        # after 0.01[s], TRIG = LOW
        time.sleep(0.01)        
        GPIO.output(self.__TRIG, False)

        signaloff=0
        signalon=0
        # signal start
        while GPIO.input(self.__ECHO) == 0:
            signaloff = time.time()
        # signal returned
        while GPIO.input(self.__ECHO) == 1:
            signalon = time.time()
        # dist calculation
        return (signalon - signaloff) * int(self.sound_speed /2)

    def __del__(self):
        GPIO.cleanup()
