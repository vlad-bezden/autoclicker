"""Mouse simulation clicker"""

import pyautogui
import time
from threading import Thread
from threading import Event
import argparse


class ClickingThread(Thread):
    def __init__(self, interval, ev):
        super().__init__()
        self.interval = interval
        self.daemon = True
        self.ev = ev

    def run(self):
        while True:
            self.ev.wait()
            time.sleep(self.interval)
            if self.ev.is_set():
                print(time.strftime('%H:%M:%S'))
                pyautogui.click()


def main():
    try:
        interval = parse_args().interval
        print(f"Mouse will click every {interval} seconds\n"
              "Press Enter for pause and resume program")
        ev = Event()
        ev.set()
        clicker = ClickingThread(interval, ev)
        clicker.start()
        while True:
            input()
            ev.clear() if ev.is_set() else ev.set()
            print(f'{"Running" if ev.is_set() else "Paused"}')
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
