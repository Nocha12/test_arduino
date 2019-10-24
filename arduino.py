import serial
import defaultNumber as dN
import result

PORT = '/dev/cu.usbmodem14101'
BaudRate = 9600

ARD = None

timeCount = 0

isFin = False

def Stop():
    global isFin
    isFin = True

def InputData(window, dataLabel, dataEverLabel, timeLabel, stateLabel):
    global timeCount, isFin, ARD

    dataList = [[] for i in range(dN.numOfSensor)]

    ARD = serial.Serial(PORT, BaudRate)

    for i in range(dN.numOfSensor):
        for j in range(dN.viewDataNum):
            dataLabel[i][j].configure(text="None")
    window.update()

    everDataList = []

    while True:
        if ARD.inWaiting() > 0:
            timeCount += 1
            timeLabel.configure(text="Time : " + str(timeCount))

            sensorDatas = ARD.readline().strip().split()

            ever = 0
            for i in range(dN.numOfSensor):
                dataList[i].append(float(sensorDatas[i]))
                ever += dataList[i][-1]

            ever /= dN.numOfSensor
            everDataList.append(ever)

            dataEverLabel.configure(text="Ever : " + str(ever))

            for i in range(dN.viewDataNum if timeCount > dN.viewDataNum else timeCount):
                for j in range(dN.numOfSensor):
                    dataLabel[j][i].configure(text=str(float(dataList[j][-i - 1])))

            window.update()

            if(isFin):
                isFin = False

                resultTime = timeCount
                timeCount = 0

                stateLabel.configure(text="State : Ready")
                result.TestFinish(resultTime, dataList, everDataList)
                return