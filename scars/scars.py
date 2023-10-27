#!/usr/bin/env python3
import sys

def process_speed(speed):
    if speed < 50:
        print("nothing")
    if 50 <= speed <= 55:
        print("warning")
    if 55 < speed <= 60:
        print("fine")
    if speed > 60:
        print("license_suspended ")

def main(argv):
    if len(argv) != 2:
        print("Usage: ./scars.py <input number>")
        return
    try:
        speed = int(argv[1])
    except ValueError:
        print("Usage: ./scars.py <input number>; where the input is an integer")
        return
    process_speed(speed)


if __name__ == '__main__':
    main(sys.argv)
