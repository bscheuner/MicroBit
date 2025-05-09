gegner = 0
zufall = 0

def on_received_number(receivedNumber):
    global gegner
    gegner = receivedNumber
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global zufall, gegner
    zufall = 0
    gegner = 0
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global zufall
    zufall = randint(1, 3)
    if zufall == 1:
        basic.show_leds("""
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            """)
    elif zufall == 2:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
    elif zufall == 3:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
    radio.send_number(zufall)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    if gegner > 0 and zufall > 0:
        if gegner == zufall:
            basic.show_icon(IconNames.NO)
        elif gegner == 1 and zufall == 2:
            basic.show_icon(IconNames.HAPPY)
        elif gegner == 2 and zufall == 3:
            basic.show_icon(IconNames.HAPPY)
        elif gegner == 3 and zufall == 1:
            basic.show_icon(IconNames.HAPPY)
        else:
            basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.B, on_button_pressed_b)