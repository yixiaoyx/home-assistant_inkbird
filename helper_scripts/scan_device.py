#!/usr/bin/python3

from sys import argv
from bluepy.btle import Scanner

if len(argv) < 2:
    print('Usage: ./scan_device.py xx:xx:xx:xx:xx:xx (device MAC address)')
    exit(1)

addr = argv[1]

scanner = Scanner()
while True:
    print('Scanning')
    scanner.scan()
    results = scanner.getDevices()
    print(len(results))
    for dev in list(results):
        if dev.addr != addr:
            continue
        print(dev.addr)
        print(dev.getScanData())

