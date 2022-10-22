input.onButtonPressed(Button.A, function () {
    if (pixel_x > 0) {
        led.unplot(pixel_x, 4)
        pixel_x += -1
        led.plot(pixel_x, 4)
    }
})
input.onButtonPressed(Button.B, function () {
    if (pixel_x < 4) {
        led.unplot(pixel_x, 4)
        pixel_x += 1
        led.plot(pixel_x, 4)
    }
})
let shoot_x = 0
let pixel_x = 0
pixel_x = 2
led.plot(pixel_x, 4)
basic.forever(function () {
    if (pins.analogReadPin(AnalogPin.P2) > 500) {
        music.playTone(262, music.beat(BeatFraction.Whole))
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
        pins.analogWritePin(AnalogPin.P2, 0)
    }
})
