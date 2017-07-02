"""Mouse simulation clicker"""

import pyautogui
import time
import threading
import argparse


class ClickingThread(threading.Thread):
    def __init__(self, interval):
        super().__init__()
        self.interval = interval
        self.daemon = True
        self.click = True

    def run(self):
        while True:
            if self.click:
                time.sleep(self.interval)
                print(time.strftime('%H:%M:%S'))
                pyautogui.click()


def main():
    try:
        interval = parse_args().interval
        print(f'Mouse will click every {interval} seconds')
        print('Press Enter for pause and resume program')
        clicker = ClickingThread(interval)
        clicker.start()
        while True:
            input()
            clicker.click = not clicker.click
            print(f'{"Running" if clicker.click else "Paused"}')
    except KeyboardInterrupt:
        print('Exiting by user request')
    except Exception as e:
        print('Unexpected error:', str(e))


def parse_args():
    parser = argparse.ArgumentParser(description='Simulate user mouse click')
    parser.add_argument(
        '-i',
        '--interval',
        type=int,
        default=60,
        help='Time in seconds mouse will click. Default time is 60 secs')
    return parser.parse_args()


if __name__ == '__main__':
    main()
