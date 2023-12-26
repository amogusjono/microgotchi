input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Heart)
    music.play(music.createSoundExpression(WaveShape.Noise, 54, 54, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("Plug in")
    cuteBot.colorLight(cuteBot.RGBLights.ALL, 0xff0000)
    cuteBot.colorLight(cuteBot.RGBLights.ALL, 0x00ff00)
    cuteBot.colorLight(cuteBot.RGBLights.ALL, 0xff0000)
    cuteBot.colorLight(cuteBot.RGBLights.ALL, 0x00ff00)
    cuteBot.forward()
    basic.pause(300)
    cuteBot.backforward()
    basic.pause(300)
    cuteBot.motors(50, -50)
})
input.onButtonPressed(Button.B, function () {
    basic.showString("Cleaned!")
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    record.startRecording(record.BlockingState.Blocking)
    record.playAudio(record.BlockingState.Blocking)
})
basic.forever(function () {
    basic.showIcon(IconNames.Duck)
    basic.pause(500)
    basic.showLeds(`
        . . . . .
        . # # . .
        # # # . .
        . # # # #
        . # # # .
        `)
    basic.pause(500)
})
