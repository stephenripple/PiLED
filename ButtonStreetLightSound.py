from gpiozero import LED, Button
from time import sleep
from signal import pause
import pygame

pygame.init()
yellow_led = LED(17);
green_led = LED(27);
red_led = LED(22);
btn = Button(5, True, 0.1, 1, False, None);
beep = pygame.mixer.Sound("Samples/elec_ping.wav")
blip = pygame.mixer.Sound("Samples/elec_beep.wav")
bong = pygame.mixer.Sound("Samples/elec_pop.wav")

green_led.off();
yellow_led.off();
red_led.off();

def LedToggle():
    print("Toggling")
    
    if red_led.is_lit:
        red_led.off();
        green_led.on();
        bong.play()
    else:
        beep.play()
        sleep(1)
        green_led.off();
        beep.play()
        yellow_led.on();
        sleep(1);
        yellow_led.off();
        red_led.on();
        blip.play()
    return

LedToggle()

btn.when_pressed = LedToggle
