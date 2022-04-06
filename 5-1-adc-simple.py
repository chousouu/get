import RPi.GPIO as GPIO

dac = [26,19,13,6,5,11,9,10]

MaxVoltage = 3.3
comp = 4 
troyka = 17

GPIO.setmode (GPIO.BCM)
GPIO.setup (dac   , GPIO.OUT, initial = GPIO.LOW)
GPIO.setup (troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup (cmp_ptr, GPIO.IN)
 
def dec2bin(value):
    return [int(bin) for bin in bin(value)[2:].zfill(bits)] 

def bin2dac (i):
    signal = dec2bin (i)
    GPIO.output (dac, signal)
    return signal

def adc():
    for i in range (256):
        bin2dac (i)
        time.sleep (0.0005)
        cmpVal = GPIO.input (cmp_ptr)
        if cmpVal == 0:
            return i

try:
    while True:
        const = adc ()
        print ('Цифровое значение =', const, "\n")
        #print (const)    
        Volt = const / 2**8 * 3.3    
        print ('Напряжение =', Volt, "\n")

finally:
    GPIO.output  (dac, GPIO.LOW)
    GPIO.cleanup (dac) 
    