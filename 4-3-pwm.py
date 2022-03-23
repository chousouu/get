import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT, initial = 0)

p=GPIO.PWM(22 ,1000)

def ChangeDutyCycle(dutycycle): 
    p.start(dutycycle)

try: 
    while True: 
        inputst = input("enter 0 - 100; 'q' to quit:" )

        if inputst.isdigit():
            dutycycle= int(inputst)
            if dutycycle > 100:
                print("error")
            ChangeDutyCycle(dutycycle)
            print(str(3.3 * dutycycle/100) + " V")
        elif inputst == 'q':
            break
        else:
            print("error")
finally: 
    p.stop()
    GPIO.cleanup()