from gpiozero import LED, Button
from time import sleep
from signal import pause

yellow_led = LED(17);
green_led = LED(27);
red_led = LED(22);
btn = Button(5, True, 0.1, 1, False, None);

green_led.off();
yellow_led.off();
red_led.off();

def LedToggle():
    print("Toggling")
    if red_led.is_lit:
        red_led.off();
        green_led.on();
    else:
        green_led.off();
        yellow_led.on();
        sleep(1);
        yellow_led.off();
        red_led.on();
    return

LedToggle()

#while True:
#    btn.wait_for_press()
#    LedToggle()
#    sleep(1)

btn.when_pressed = LedToggle
