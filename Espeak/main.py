import os


if __name__ == "__main__":
    print('Welcome to Espeak 1.4(press q to exit)')
    while True:
        x = input('Enter what you want to speak: ')
        if x == 'q':
            break
        command = f"espeak '{x}'"
        os.system(command)