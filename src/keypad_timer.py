import time
import picokeypad as keypad

keypad.init()
NUM_PADS = keypad.get_num_pads()

# send a keypad.get_button_states() value, receive array of pressed indices (0-15)
# by default will reverse the order (so lowest keypad number is first)
def arrayOfPads(state, reversed=True):
    ret = []
    p = NUM_PADS - 1
    while state > 0:
        if state >= 2**p:
            ret.append(p)
            state -= 2**p
        p -= 1
    if reversed:
        ret.reverse()
    return ret

def testtimer():
    duration = 60.0
    elapsed = 0.0
    flash_interval = 0.5
    flash_elapsed = 0.0
    keypad_interval = 0.1
    last_lit = 0
    lit = False
    keypad.init()
    while True:
        # check whether someone is pressing a button; take highest button pressed
        keys = arrayOfPads(keypad.get_button_states())
        if len(keys) > 0:
            last_lit = keys[0] + 1
            lit = True
            elapsed = 0.0
            flash_elapsed = 0.0
        
        # if elapsed time on this button is greater than duration, button off
        if elapsed > duration:
            last_lit -= 1
            lit = False
            elapsed = 0.0
            flash_elapsed = 0.0
        
        # if we've flashed (on or off) to the defined interval, switch and start count again
        if flash_elapsed >= flash_interval:
            lit = not lit
            flash_elapsed = 0.0
        
        # update key status
        for button in range(0, NUM_PADS):
            if last_lit > 0 and button < (last_lit - 1):
                keypad.illuminate(button, 0x00, 0x20, 0x00)
            elif last_lit > 0 and button == (last_lit -1) and lit:
                # establish progress through as a fraction
                progress = elapsed / duration if duration > 0.0 else 0.0
                # colors: green => blue => red
                r = int(64 * max(0, progress - 0.5))
                g = int(64 * max(0, 0.5 - progress))
                b = int(64 * max(0, 0.5 - abs(0.5 - progress)))
                keypad.illuminate(button, r, g, b)
            else:
                keypad.illuminate(button, 0x00, 0x00, 0x00)

        # if any button is lit (last_lit > 0) we need to process timers
        if last_lit > 0:
            elapsed += keypad_interval
            flash_elapsed += keypad_interval
            
        # else last-lit = 0, lets make sure everything is calm ...
        else:
            lit = False
            elapsed = 0.0
            flash_elapsed = 0.0
        
        # update the keypad (show lights!) and sleep until next button check
        keypad.update()
        time.sleep(keypad_interval)

if __name__ == "__main__":
    testtimer()