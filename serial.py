import serial
s = serial.Serial('/dev/ttyS0',115200)
s.write("meow".encode('utf-8'))
