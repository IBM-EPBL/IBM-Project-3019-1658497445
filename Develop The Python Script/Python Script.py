import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

organization = "h9rxc6"
deviceType = "b11m4edevicetype"
deviceId = "b11m4edeviceid"
authMethod = "token"
authToken = "ycBQk4OrBEFkL_FSrf"

def myCommandCallback(cmd):
    print("Command receied: %s" %cmd.data['command'])
    status = cmd.data['command']
    if status=="lighton":
        print("led is on")
    else:
        print("led is off")


try:
    deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-Method": authMethod, "auth-Token": authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
    print("Caught exception connecting device: %s" %str(e))
    sys.exit()

deviceCli.connect()

while True:
    temp=random.randint(0,100)
    humd=random.randint(0,100)
    data={'temp':temp, 'Humid': humd}
    def myOnPublishCallback():
        print("Published Temperature = %s C" % temp, "Humidity= %s %%" % humd, "to IBM Watson")

    success=deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
    if not success:
        print("Not Connected to IoTF")
    time.sleep(1)

    deviceCli.commandCallback=myCommandCallback


deviceCli.disconnect()
