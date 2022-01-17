import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
import pyqt5ac
from PyQt5 import QtSql
from pyqtgraph import PlotWidget, plot
import matplotlib.pyplot as plt
import pyqtgraph as pg
from PyQt5 import QtCore, QtWidgets, uic, QtChart
import numpy as np
from PyQt5.QtChart import QChart,QChartView,QLineSeries
from PyQt5.QtCore import QPoint,QPointF
from scipy.fft import fft, ifft
from scipy import interpolate
from scipy.signal import hilbert
from PyQt5.QtGui import QPolygonF
from PyQt5.QtChart import QValueAxis
from astropy import modeling

from LogInWindow_ui import Ui_MainWindow

pyqt5ac.main(rccOptions='', uicOptions='--from-imports', force=False, initPackage=False, config='',
             ioPaths=[['*.ui', '%%FILENAME%%_ui.py'], ['*.qrc', '%%FILENAME%%_rc.py']])


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.pushButton_Exit.clicked.connect(QApplication.instance().quit)
        self.ui.pushButton_Exit_2.clicked.connect(QApplication.instance().quit)
        self.openDB()
        self.ui.pushButton.clicked.connect(self.checkUser)
        self.ui.pushButton_loadInterference.clicked.connect(self.loadInterferenceData)
        self.ui.pushButton_loadmovarm.clicked.connect(self.loadMovingArmData_clicked)
        self.ui.pushButton_loadrefarm.clicked.connect(self.loadReferenceArmData_clicked)
        self.ui.pushButton_generatedechirp.clicked.connect(self.dechirpGeneration)
        self.ui.pushButton_generatedechirp.clicked.connect(self.saveTextFile)
        self.ui.pushButton_octparameters.clicked.connect(self.octParameters)

    def show(self):
        self.main_win.showFullScreen()

    def openDB(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data.sqlite")

        if not self.db.open():
            print("Error in Open dB")
        self.query = QtSql.QSqlQuery()

    def loadInterferenceData(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        dialog.setNameFilter(app.tr("Raw Files (*.raw)"))
        dialog.setViewMode(QtWidgets.QFileDialog.Detail)
        if dialog.exec_():
            self.fileNames_Interference = dialog.selectedFiles()

    def loadMovingArmData_clicked(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        dialog.setNameFilter(app.tr("Raw Files (*.raw)"))
        dialog.setViewMode(QtWidgets.QFileDialog.Detail)
        if dialog.exec_():
            self.fileNames_MovingArm = dialog.selectedFiles()


    def loadReferenceArmData_clicked(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        dialog.setNameFilter(app.tr("Raw Files (*.raw)"))
        dialog.setViewMode(QtWidgets.QFileDialog.Detail)
        if dialog.exec_():
            self.fileNames_ReferenceArm = dialog.selectedFiles()


    def dechirpGeneration(self):
        allNormPhase = []
        for itr in self.fileNames_Interference:
            Reference = np.fromfile(itr, dtype=np.int16)
            dataSize = (1000, 2048)
            Reference = Reference.reshape(dataSize)
            singleFringe = Reference[0, :]

            # Fourier Transform
            PSF = fft(singleFringe)
            cropSpectra = PSF[5:-1]
            cropSpectra = abs(cropSpectra[1:int(len(cropSpectra) / 2)])
            peakLoc = np.where(cropSpectra == np.amax(cropSpectra))
            startPeakLoc = int(peakLoc[0] - 35)
            endPeakLoc = int(peakLoc[0] + 35)

            filt_fn = np.zeros(PSF.shape)
            filt_fn[startPeakLoc:endPeakLoc, ] = 1

            # Filter the single Peak
            singlePeak = PSF * filt_fn

            # IFFT
            filteredSignal = ifft(singlePeak)

            # Find Phase
            phaseOCT = np.unwrap(np.angle(hilbert((filteredSignal.imag))))

            # Phase normalization
            normPhase = phaseOCT / max(phaseOCT)

            # Sampling Points
            samplingPoints = 2048
            allNormPhase.append(normPhase * samplingPoints)

        meanPhase = sum(allNormPhase) / len(allNormPhase)

        # Rescaling of Average Phase
        avgPhaseRescale = np.zeros([Reference.shape[1]])

        for i in range(Reference.shape[1]):
            avgPhaseRescale[i] = min(meanPhase) + ((max(meanPhase) - min(meanPhase)) / Reference.shape[1]) * i

        nCameraPixels = 2048
        x = np.arange(nCameraPixels)
        f = interpolate.interp1d(meanPhase, x, 'cubic')
        dechirpData = f(avgPhaseRescale)
        dechirpData[dechirpData < 0] = 0
        polygon = QPolygonF()
        self.dechirpData = dechirpData        # Plot on widget
        series = QLineSeries()

        for i in range(2048):
            series << QPointF(i, dechirpData[i])


        chart = QChart()
        chart.setTheme(QChart.ChartThemeBlueCerulean)
        chart.addSeries(series)
        chart.createDefaultAxes()

        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Dechirp File")
        chartview = QChartView(chart)

        self.ui.widget.setContentsMargins(0, 0, 0, 0)
        lay = QtWidgets.QHBoxLayout(self.ui.widget)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(chartview)

    def saveTextFile(self):
        np.savetxt('Dechirp.txt', self.dechirpData, delimiter=',',fmt='%0.3f')


    def ReadRawOCTFile(self,filenames):
        bScanRawDataStream = np.fromfile(filenames,dtype = np.int16)
        spectroMeterData = bScanRawDataStream.reshape(1000,2048)
        return spectroMeterData

    def octParameters(self):
        nPosition = 5


        chart = QChart()
        chart.setTheme(QChart.ChartThemeBlueCerulean)
        series = QLineSeries()
        chartview = QChartView(chart)


        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("PSF")
        axisX = QValueAxis()
        axisX.setTitleText("Position in mm")
        axisY = QValueAxis()
        axisY.setTitleText("Amplitude")

        self.ui.widget_2.setContentsMargins(0, 0, 0, 0)
        lay = QtWidgets.QHBoxLayout(self.ui.widget_2)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(chartview)

        chart1 = QChart()

        chart1.setTheme(QChart.ChartThemeBlueCerulean)
        series1 = QLineSeries()
        chartview1 = QChartView(chart1)
        chart1.setAnimationOptions(QChart.SeriesAnimations)
        chart1.setTitle("Sensitivity Roll-off")

        axisX = QValueAxis()
        axisX.setTitleText("Position in mm")
        axisY = QValueAxis()
        axisY.setTitleText("Amplitude in dB")

        self.ui.widget_3.setContentsMargins(0, 0, 0, 0)
        lay = QtWidgets.QHBoxLayout(self.ui.widget_3)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(chartview1)

        chart2 = QChart()

        chart2.setTheme(QChart.ChartThemeBlueCerulean)
        series2 = QLineSeries()
        chartview2 = QChartView(chart2)
        chart2.setAnimationOptions(QChart.SeriesAnimations)
        chart2.setTitle("Axial Resolution")

        axisX = QValueAxis()
        axisX.setTitleText("Position in mm")
        axisY = QValueAxis()
        axisY.setTitleText("Resolution")

        self.ui.widget_4.setContentsMargins(0, 0, 0, 0)
        lay = QtWidgets.QHBoxLayout(self.ui.widget_4)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(chartview2)

        calibratedPSFStack = np.zeros((nPosition,2048))

        for iPosition in range(nPosition):
            interferenceArmData = self.ReadRawOCTFile(self.fileNames_Interference[iPosition])
            MovingArmData = self.ReadRawOCTFile(self.fileNames_MovingArm[iPosition])
            RefArmData = self.ReadRawOCTFile(self.fileNames_ReferenceArm[iPosition])

            # Find Mean of Moving Arm and Reference Arm Data
            avgMovingArmData = MovingArmData.mean(axis=0)
            avgRefArmData = RefArmData.mean(axis=0)

            # Find Spectra of addition of Moving arm and Ref arm Data
            meanSpectra = avgMovingArmData + avgRefArmData

            # Background Subtraction
            fringe = interferenceArmData[0] - meanSpectra

            # Resampled De chirp Data
            dechirpData = np.loadtxt('Dechirp.txt')

            # Interpolation of fringe with resampled dechirp Data
            x = np.arange(2048)
            vq = interpolate.interp1d(x, fringe, 'cubic')
            resampledFringe = vq(dechirpData)

            # FFT of Windowed Data & crop it
            nCameraPixels = 2048
            hannWindow = np.hanning(nCameraPixels)
            filtData = resampledFringe * hannWindow
            calibratedPSF = abs(fft(filtData))



            for i in range(5,1024):
                series.append(i, calibratedPSF[i])


            chart.addSeries(series)
            chart.createDefaultAxes()

            for i in range(5,1024):
                series1.append(i, 20 * (np.log10(calibratedPSF[i])))

            chart1.addSeries(series1)
            chart1.createDefaultAxes()



            fitter = modeling.fitting.LevMarLSQFitter()
            model = modeling.models.Gaussian1D()  # depending on the data you need to give some initial values
            x = np.arange(1019)


            fitted_model = fitter(model, x, calibratedPSF[5:1024])
            x1 = fitted_model.stddev.value
            series2.append(iPosition,x1*1.665)
            print("Axial Resolution:", x1 * 1.665)
            chart2.addSeries(series2)
            chart2.createDefaultAxes()
            calibratedPSFStack[iPosition,:] = calibratedPSF
        self.MicronsPerPixel(calibratedPSFStack)

    def MicronsPerPixel(self,calibratedPSFStack):
        calibratedPSFStack1 = np.array(calibratedPSFStack)
        print(type(calibratedPSFStack1))

        numofPosition = calibratedPSFStack1.shape[0]
        nCameraPixels = calibratedPSFStack1.shape[1]
        armMovement = 127
        print(numofPosition)

    def checkUser(self):
        username1 = self.ui.lineEdit.text()
        password1 = self.ui.lineEdit_2.text()

        if len(username1) == 0 or len(password1) == 0:
            self.ui.error.setText("Please input all fields")

        self.query.exec_("select * from userdata where username = '%s' and password = '%s';"%(username1,password1))
        self.query.first()
        if self.query.value("username") != None and self.query.value("password") != None:
            self.ui.error.setText("")
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.error.setText("Invalid User Name or Password")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
