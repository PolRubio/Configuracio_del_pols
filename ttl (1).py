import time
import serial
import serial.tools.list_ports


# CABLE BLANC (+) CABLE VERD (-)

def lecturaPorts():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)


def comunicacion(puerto, periode, nombrePols):
    control = 0

    # on = bytes ('1','utf-8')

    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = puerto
    ser.open()

    while control < nombrePols:
        ser.setRTS(True)
        time.sleep(periode / 2)
        ser.setRTS(False)
        time.sleep(periode / 2)
        control += 1
    ser.close()

# lecturaPorts()

# comunicacion('COM3',10,30)
# print ('finished')
