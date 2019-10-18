import arduino
import tkinter
import tkinter.font
import defaultNumber as dN

window = tkinter.Tk()
window.title("Arduino")
window.geometry("1050x300+100+100")

font = tkinter.font.Font(family="맑은 고딕", size=20)

dataEverLabel = tkinter.Label(window, text="Ever : None", font=font)
dataEverLabel.grid(row=0, column=5)

timeLabel = tkinter.Label(window, text="Time : 0", font=font)
timeLabel.grid(row=1, column=5)

dataLabel = [[] * dN.viewDataNum for i in range(dN.numOfSensor)]
for i in range(dN.numOfSensor):
    for j in range(dN.viewDataNum):
        dataLabel[i].append(tkinter.Label(window, text="None", font=font))
        dataLabel[i][j].grid(row=j+11, column=i + 1)

stateLabel = tkinter.Label(window, text="State : Ready", font=font)
stateLabel.grid(row=2, column=0)

sensorLabel = []
for i in range(dN.numOfSensor):
    sensorLabel.append(tkinter.Label(window, text="Sensor"+str(i + 1), font=font))
    sensorLabel[i].grid(row=10, column=i + 1)

def PressStartBtn():
    if stateLabel['text'] != "State : Ready":
        return

    stateLabel.configure(text="State : Running")

    arduino.InputData(window, dataLabel, dataEverLabel, timeLabel, stateLabel)

def PressStopBtn():
    arduino.Stop()

startBtn = tkinter.Button(window, text="Start", command=PressStartBtn, font=font)
startBtn.config(height=1, width=8)
startBtn.grid(row=0, column=0)

stopBtn = tkinter.Button(window, text="Stop", command=PressStopBtn, font=font)
stopBtn.config(height=1, width=8)
stopBtn.grid(row=1, column=0)

window.mainloop()
