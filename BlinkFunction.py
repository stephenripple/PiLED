from gpiozero import LED
from time import sleep

red_led = LED(17);

red_led.blink(0.2, 0.1, None, True);
