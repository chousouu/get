import RPi.GPIO as GPIO

dac = [26,19,13,6,5,11,9,10]
bits = len(dac)
level = 2**bits
maxU = 3.3


def dec2bin(value):
    return [int(bin) for bin in bin(value)[2:].zfill(bits)] 

def dec2dec(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)


try: 
    while True: 
        inputStr = input("Enter number 0 - 255; press 'q' for quit " )

        if inputStr.isdigit():
            value = int(inputStr)
            if value >= level :
                print("Error")
                continue 
            print(str((maxU/ 2**8)*int(inputStr)) + " V")
            dec2dec(value)
        elif inputStr == 'q': 
            break
        else:  
            print("Error")
finally:
    GPIO.output(dac, 0)
