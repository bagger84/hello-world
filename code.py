

import RPi.GPIO as GPIO
import time

P1_Button = 17
P2_Button = 18
P3_Button = 27
P3_LED = 10
P2_LED = 9
P1_LED = 11
P1u2_LED = 11,9 # 2 LED werden gleichzeitg geschalten
P2u3_LED = 9,10
P1u2u3_LED = 11,9,10 #3 LED werden gleichzeitig geschalten

def setup():
    GPIO.setmode(GPIO.BCM)   #BCM beschreibt das die GPIO NR. verwendet wird, nicht die Zaehlweise
    GPIO.setup(P1_Button, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(P2_Button, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(P3_Button, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(P3_LED, GPIO.OUT)
    GPIO.setup(P2_LED, GPIO.OUT)
    GPIO.setup(P1_LED, GPIO.OUT)
    GPIO.setup(P1u2_LED, GPIO.OUT)
    GPIO.setup(P2u3_LED, GPIO.OUT)
    GPIO.setup(P1u2u3_LED, GPIO.OUT)

    
    
setup()
isLedOn = False
isButtonReady = True

while True:
    if isButtonReady and GPIO.input(P1_Button) == GPIO.LOW:
                isButtonReady = False          
                if not isLedOn:
                    isLedOn = True
                    GPIO.output(P1_LED, GPIO.HIGH)
                    GPIO.output (P2u3_LED, GPIO.LOW)
                else:
                   isLedOn = False
                   GPIO.output(P1_LED, GPIO.LOW)

    if GPIO.input(P1_Button) == GPIO.HIGH:
        isButtonReady = True
        time.sleep(0.01)


    if isButtonReady and GPIO.input(P2_Button) == GPIO.LOW:
                isButtonReady = False          
                if not isLedOn:
                    isLedOn = True
                    GPIO.output(P1u2_LED, GPIO.HIGH)
                    GPIO.output(P3_LED, GPIO.LOW)
                else:
                   isLedOn = False
                   GPIO.output(P1u2_LED, GPIO.LOW)

    def jls_extract_def():
        if GPIO.input(P2_Button) == GPIO.HIGH:
            isButtonReady = True
            time.sleep(0.01)
        return isButtonReady


    isButtonReady = jls_extract_def()


    if isButtonReady and GPIO.input(P3_Button) == GPIO.LOW:
                isButtonReady = False          
                if not isLedOn:
                    isLedOn = True
                    GPIO.output(P1u2u3_LED, GPIO.HIGH)
                else:
                   isLedOn = False
                   GPIO.output(P1u2u3_LED, GPIO.LOW)


#     if GPIO.input(P1_Button) == GPIO.HIGH:
#         isButtonReady = True
#         time.sleep(0.01)

#     if GPIO.input(P2_Button) == GPIO.HIGH:
#         isButtonReady = True
#         time.sleep(0.01)

    if GPIO.input(P3_Button) == GPIO.HIGH:
        isButtonReady = True
        time.sleep(0.01)
