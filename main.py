def on_button_pressed_a():
    global pixel_x
    if pixel_x > 0:
        led.unplot(pixel_x, 4)
        pixel_x += -1
        led.plot(pixel_x, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global pixel_x
    if pixel_x < 4:
        led.unplot(pixel_x, 4)
        pixel_x += 1
        led.plot(pixel_x, 4)
input.on_button_pressed(Button.B, on_button_pressed_b)

shoot_x = 0
pixel_x = 0
pixel_x = 2
led.plot(pixel_x, 4)

def on_forever():
    global shoot_x
    if pins.analog_read_pin(AnalogPin.P2) > 500:
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        shoot_x = pixel_x
        led.plot(shoot_x, 3)
        basic.pause(100)
        led.unplot(shoot_x, 3)
        led.plot(shoot_x, 2)
        basic.pause(100)
        led.unplot(shoot_x, 2)
        led.plot(shoot_x, 1)
        basic.pause(100)
        led.unplot(shoot_x, 1)
        led.plot(shoot_x, 0)
        basic.pause(100)
        led.unplot(shoot_x, 0)
        pins.analog_write_pin(AnalogPin.P2, 0)
basic.forever(on_forever)
