def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
    music.play(music.create_sound_expression(WaveShape.NOISE,
            54,
            54,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("Plug in")
    cuteBot.color_light(cuteBot.RGBLights.ALL, 0xff0000)
    cuteBot.color_light(cuteBot.RGBLights.ALL, 0x00ff00)
    cuteBot.color_light(cuteBot.RGBLights.ALL, 0xff0000)
    cuteBot.color_light(cuteBot.RGBLights.ALL, 0x00ff00)
    cuteBot.forward()
    basic.pause(300)
    cuteBot.backforward()
    basic.pause(300)
    cuteBot.motors(50, -50)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("Cleaned!")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    record.start_recording(record.BlockingState.BLOCKING)
    record.play_audio(record.BlockingState.BLOCKING)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    basic.show_icon(IconNames.DUCK)
    basic.pause(500)
    basic.show_leds("""
        . . . . .
        . # # . .
        # # # . .
        . # # # #
        . # # # .
        """)
    basic.pause(500)
basic.forever(on_forever)
