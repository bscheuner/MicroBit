def on_logo_pressed():
    for Index in range(5):
        if led.point(0, Index) and led.point(1, Index):
            led.plot(4, Index)
        elif not (led.point(0, Index)) and not (led.point(1, Index)):
            led.plot(4, Index)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_received_number(receivedNumber):
    global partnerRunde
    if receivedNumber == 1:
        led.plot(1, partnerRunde)
    partnerRunde += 1
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global meineRunde
    radio.send_number(0)
    meineRunde += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global meineRunde
    radio.send_number(1)
    led.plot(0, meineRunde)
    meineRunde += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

meineRunde = 0
partnerRunde = 0
partnerRunde = 0
meineRunde = 0