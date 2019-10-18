import os
import defaultNumber as dN
import matplotlib.pyplot as plt
import xlsxwriter

def TestFinish(timeCount, dataList, everDataList):
    for i in range(dN.numOfSensor):
        dataList[i].pop(0)

    everDataList.pop(0)

    timeCount -= 1

    x = []
    y = []

    for i in range(timeCount):
        x.append(i)
        y.append(everDataList[i])

    plt.plot(x, y)

    plt.xlabel('Sec')
    plt.ylabel('Dust')

    plt.title("Result")

    path = 'Result'
    fileList = os.listdir(path)
    names = []
    for name in fileList:
        names.append(int(name.split('.')[0]))

    fileName = 0 if len(names) == 0 else max(names) + 1
    plt.savefig(path + '/' + str(fileName) + '.png')
    plt.show()

    workbook = xlsxwriter.Workbook(path + '/' + str(fileName) + '.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write(0, dN.numOfSensor, "Everege")
    worksheet.write(0, dN.numOfSensor + 1, "Time")

    for i in range(dN.numOfSensor):
        worksheet.write(0, i, "Sensor" + str(i + 1))

        for j in range(timeCount):
            worksheet.write(j + 1, i, dataList[i][j])

    for i in range(timeCount):
        worksheet.write(i + 1, dN.numOfSensor, everDataList[i])
        worksheet.write(i + 1, dN.numOfSensor + 1, i + 1)

    workbook.close()

    f = open(path + '/' + str(fileName) + ".txt", "a")

    for i in range(dN.numOfSensor):
        for j in range(timeCount):
            dataList[i][j] = str(dataList[i][j])

    resultTxt = ""
    for i in range(dN.numOfSensor):
        resultTxt += ' '.join(dataList[i]) + " " + str(i + 1) + '\n'

    f.write(resultTxt)
    f.close()