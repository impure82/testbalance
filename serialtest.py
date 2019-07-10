#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import serial
import time
port='/dev/ttyUSB0'

ser = serial.Serial(port,9600)
ser.isOpen()
while 1:
    ser.write(b"\n")
    ser.write(b"Z")
    ser.write(b"\r")
    time.sleep(5)
