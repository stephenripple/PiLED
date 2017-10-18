from gpiozero import LED
from time import sleep

red_led = LED(17);

red_led.toggle();
sleep(1);
print("Is the LED on? " + str(red_led.is_lit));
red_led.toggle();
sleep(1);
print("Is the LED on? " + str(red_led.is_lit));
