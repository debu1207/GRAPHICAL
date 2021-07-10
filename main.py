import matplotlib.pyplot as plt
import numpy as np
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QMessageBox, QFileDialog, QComboBox
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt

# from PyQt5.QtCore import QComboBox


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Graphical'
        self.setWindowIcon(QIcon('logo2.png'))
        self.setStyleSheet("background-color: black; color: white")
        self.left = 500
        self.top = 30
        self.width = 1000
        self.height = 900

        self.theme = self.plotDarkTheme
        self.defaultGraphBackground = Qt.black

        self.name = QLabel(self)
        self.name.setFont(QFont("Courier", 20))
        self.name.setText("GRAPHICAL")
        self.name.setStyleSheet("border: 2px solid white; border-radius: 5px;")
        self.name.setGeometry(420, 20, 155, 40)

        self.Label = QLabel(self)
        self.Label.setFont(QFont("Courier", 10))
        self.Label.setText("Enter Points:")
        self.Label.setGeometry(50, 75, 150, 30)

        self.edit = QTextEdit(self)
        self.edit.setGeometry(50, 110, 200, 30)
        self.edit.setStyleSheet("border: 2px solid white; border-radius: 3px;")

        self.yedit = QTextEdit(self)
        self.yedit.setGeometry(50, 145, 200, 30)
        self.yedit.setStyleSheet("border: 2px solid white; border-radius: 3px;")

        self.xlabel = QLabel(self)
        self.xlabel.setGeometry(30, 110, 20, 30)
        self.xlabel.setText("X")
        self.ylabel = QLabel(self)
        self.ylabel.setGeometry(30, 145, 20, 30)
        self.ylabel.setText("Y")

        self.button = QPushButton(self)
        self.button.setGeometry(270, 110, 60, 30)
        self.button.setStyleSheet("border: 1px solid white; border-radius: 7px;")
        self.button.setText("line")
        self.button.clicked.connect(self.line)

        self.button1 = QPushButton(self)
        self.button1.setGeometry(335, 110, 60, 30)
        self.button1.setStyleSheet("border: 1px solid white; border-radius: 7px;")
        self.button1.setText("Scatter")
        self.button1.clicked.connect(self.scatter)

        self.button2 = QPushButton(self)
        self.button2.setGeometry(400, 110, 60, 30)
        self.button2.setStyleSheet("border: 1px solid white; border-radius: 7px;")
        self.button2.setText("Bar")
        self.button2.clicked.connect(self.bar)

        self.button3 = QPushButton(self)
        self.button3.setGeometry(465, 110, 60, 30)
        self.button3.setStyleSheet("border: 1px solid white; border-radius: 7px;")
        self.button3.setText("Pie")
        self.button3.clicked.connect(self.pie)

        self.save_button = QPushButton(self)
        self.save_button.setGeometry(50, 185, 60, 30)
        self.save_button.setStyleSheet("border: 1px solid white; border-radius: 7px;")
        self.save_button.setText('Save')
        self.save_button.clicked.connect(self.showdialog)

        self.clearBtn = QPushButton(self)
        self.clearBtn.setGeometry(115, 185, 60, 30)
        self.clearBtn.setStyleSheet("border: 1px solid white; border-radius: 7px;")
        self.clearBtn.setText('Clear')
        self.clearBtn.clicked.connect(self.clear)

        self.Themes = QComboBox(self)
        self.Themes.setStyleSheet("border: 1px solid white; border-radius: 3px;")
        self.Themes.addItems(["Dark", "Light"])
        self.Themes.move(30, 830)
        self.Themes.resize(65, 20)
        self.Themes.activated[str].connect(self.changeTheme)

        self.lineStyle = 'solid'
        self.marker = 'point'
        self.color = 'blue'

        self.Lines = {'solid': '-', 'dotted': ':', 'dashed':'--', 'dashdot':'-.'}
        self.Markers = {'none': ' ', 'point': '.', 'circle':'o', 'triangle':'^', 'square': 's', 'pentagon': 'p', 'star': '*', 'plus': '+', 'diamond': 'D'}

        self.selectLine = QLabel(self)
        self.selectLine.setFont(QFont("Courier", 10))
        self.selectLine.setGeometry(280, 185, 90, 30)
        self.selectLine.setText("Linestyle ")

        self.line = QComboBox(self)
        self.line.addItems(['solid', 'dotted', 'dashed', 'dashdot'])
        self.line.setStyleSheet("border: 1px solid white; border-radius: 3px;")
        self.line.move(375, 190)
        self.line.resize(80, 20)
        self.line.activated[str].connect(self.changeLineStyle)

        self.selectMarker = QLabel(self)
        self.selectMarker.setFont(QFont("Courier", 10))
        self.selectMarker.setGeometry(475, 185, 70, 30)
        self.selectMarker.setText("Marker ")

        self.mark = QComboBox(self)
        self.mark.addItems(['point', 'circle', 'triangle', 'square', 'pentagon', 'star', 'plus', 'diamond', 'none'])
        self.mark.setStyleSheet("border: 1px solid white; border-radius: 3px;")
        self.mark.move(540, 190)
        self.mark.resize(80, 20)
        self.mark.activated[str].connect(self.changeMarker)

        self.selectColor = QLabel(self)
        self.selectColor.setFont(QFont("Courier", 10))
        self.selectColor.setGeometry(650, 185, 70, 30)
        self.selectColor.setText("Color ")

        self.fillcolor = QComboBox(self)
        self.fillcolor.addItems(['blue', 'green', 'yellow', 'black', 'red', 'pink', 'orange'])
        self.fillcolor.setStyleSheet("border: 1px solid white; border-radius: 3px;")
        self.fillcolor.move(705, 190)
        self.fillcolor.resize(80, 20)
        self.fillcolor.activated[str].connect(self.changeColor)

        self.photo = QLabel(self)
        self.photo.setGeometry(260, 320, 649, 497)
        self.photo.setStyleSheet("border: 7px solid gray; border-radius: 6px")
        # self.photo.setStyleSheet("border-radius: 10px;")

        self.Title = QLabel(self)
        self.Title.setFont(QFont("Courier", 10))
        self.Title.setGeometry(35, 315, 70, 30)
        self.Title.setText("Title:")

        self.titleedit = QTextEdit(self)
        self.titleedit.setGeometry(30, 350, 200, 30)
        self.titleedit.setStyleSheet("border: 2px solid white; border-radius: 3px;")

        self.LabelX = QLabel(self)
        self.LabelX.setFont(QFont("Courier", 10))
        self.LabelX.setGeometry(35, 390, 130, 30)
        self.LabelX.setText("x-axis Label:")

        self.xlabeledit = QTextEdit(self)
        self.xlabeledit.setGeometry(30, 425, 200, 30)
        self.xlabeledit.setStyleSheet("border: 2px solid white; border-radius: 3px;")

        self.LabelY = QLabel(self)
        self.LabelY.setFont(QFont("Courier", 10))
        self.LabelY.setGeometry(35, 455, 130, 30)
        self.LabelY.setText("y-axis Label:")

        self.ylabeledit = QTextEdit(self)
        self.ylabeledit.setGeometry(30, 490, 200, 30)
        self.ylabeledit.setStyleSheet("border: 2px solid white; border-radius: 3px;")

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def clear(self):
        self.edit.setText("")
        self.yedit.setText("")
        self.xlabeledit.setText("")
        self.ylabeledit.setText("")
        self.titleedit.setText("")
        pixmap = QPixmap(649, 497)
        pixmap.fill(self.defaultGraphBackground)
        self.photo.setPixmap(pixmap)

    def showdialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("Graph Saved Successfully!")
        # msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Save grpah")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
        print("value of pressed message box button:", retval)

    def file_save(self):
        name = QFileDialog.getSaveFileName(self, 'Save File')
        try:
            with open(name, 'w') as file:
                text = self.textEdit.toPlainText()
                file.write(text)
        except:
            print("Error")

    def plotDarkTheme(self):
        self.button.setStyleSheet("border: 1px solid white; color: white; border-radius: 7px;")
        self.button1.setStyleSheet("border: 1px solid white; color: white; border-radius: 7px;")
        self.button2.setStyleSheet("border: 1px solid white; color: white; border-radius: 7px;")
        self.button3.setStyleSheet("border: 1px solid white; color: white; border-radius: 7px;")

    def plotLightTheme(self):
        self.button.setStyleSheet("border: 1px solid grey; color: black; border-radius: 7px;")
        self.button1.setStyleSheet("border: 1px solid grey; color: black; border-radius: 7px;")
        self.button2.setStyleSheet("border: 1px solid grey; color: black; border-radius: 7px;")
        self.button3.setStyleSheet("border: 1px solid grey; color: black; border-radius: 7px;")

    def changeTheme(self, text):
        if text == "Dark":
            self.theme = self.plotDarkTheme
            self.defaultGraphBackground = Qt.black
            self.setStyleSheet("background-color: black; color: white")
            self.name.setStyleSheet("border: 2px solid white; border-radius: 5px;")
            self.edit.setStyleSheet("border: 2px solid white; border-radius: 3px;")
            self.yedit.setStyleSheet("border: 2px solid white; border-radius: 3px;")

            self.Themes.setStyleSheet("border: 1px solid white; border-radius: 3px;")
            self.mark.setStyleSheet("border: 1px solid white; border-radius: 3px;")
            self.line.setStyleSheet("border: 1px solid white; border-radius: 3px;")
            self.fillcolor.setStyleSheet("border: 1px solid white; border-radius: 3px;")

            self.button.setStyleSheet("border: 1px solid white; border-radius: 7px;")
            self.button1.setStyleSheet("border: 1px solid white; border-radius: 7px;")
            self.button2.setStyleSheet("border: 1px solid white; border-radius: 7px;")
            self.button3.setStyleSheet("border: 1px solid white; border-radius: 7px;")
            self.save_button.setStyleSheet("border: 1px solid white; border-radius: 7px;")
            self.clearBtn.setStyleSheet("border: 1px solid white; border-radius: 7px;")

        elif text == 'Light':
            self.theme = self.plotLightTheme
            self.defaultGraphBackground = Qt.white
            self.setStyleSheet("background-color: white; color: black")
            self.name.setStyleSheet("border: 2px solid grey; border-radius: 5px;")
            self.edit.setStyleSheet("border: 2px solid grey; border-radius: 3px;")
            self.yedit.setStyleSheet("border: 2px solid grey; border-radius: 3px;")

            self.Themes.setStyleSheet("border: 1px solid grey; border-radius: 3px;")
            self.mark.setStyleSheet("border: 1px solid grey; border-radius: 3px;")
            self.line.setStyleSheet("border: 1px solid grey; border-radius: 3px;")
            self.fillcolor.setStyleSheet("border: 1px solid grey; border-radius: 3px;")

            self.button.setStyleSheet("border: 1px solid grey; border-radius: 7px;")
            self.button1.setStyleSheet("border: 1px solid grey; border-radius: 7px;")
            self.button2.setStyleSheet("border: 1px solid grey; border-radius: 7px;")
            self.button3.setStyleSheet("border: 1px solid grey; border-radius: 7px;")
            self.save_button.setStyleSheet("border: 1px solid grey; border-radius: 7px;")
            self.clearBtn.setStyleSheet("border: 1px solid grey; border-radius: 7px;")

    def changeLineStyle(self, text):
        self.lineStyle = text

    def changeMarker(self, text):
        self.marker = text

    def changeColor(self, text):
        self.color = text

    def line(self):
        self.theme()
        self.button.setStyleSheet("background-color: lightblue; color: black; border: 1px solid grey; border-radius: 7px;")
        arr = self.edit.toPlainText().strip().split()

        arr = [int(i) for i in arr]
        ypoints = np.array(arr)
        fig = plt.figure()
        plt.ion()
        plt.plot(ypoints, self.Lines[self.lineStyle], marker = self.Markers[self.marker], color=self.color)
        plt.xlabel(self.xlabeledit.toPlainText())
        plt.ylabel(self.ylabeledit.toPlainText())
        plt.title(self.titleedit.toPlainText())
        # plt.legend()
        plt.ioff()
        plt.savefig("new_image.png")
        self.photo.setPixmap(QPixmap('new_image.png'))

    def bar(self):
        self.theme()
        self.button2.setStyleSheet("background-color: lightblue; color: black; border: 1px solid grey; border-radius: 7px;")
        arr = self.edit.toPlainText().strip().split()

        arr = [int(i) for i in arr]
        ypoints = np.array(arr)
        xpoints = np.array([(i + 1) for i in range(len(ypoints))])
        fig = plt.figure()
        plt.ion()
        plt.bar(xpoints, ypoints, color=self.color)
        plt.xlabel(self.xlabeledit.toPlainText())
        plt.ylabel(self.ylabeledit.toPlainText())
        plt.title(self.titleedit.toPlainText())
        # plt.legend()
        plt.ioff()
        plt.savefig("new_image.png")

        self.photo.setPixmap(QPixmap('new_image.png'))

    def pie(self):
        self.theme()
        self.button3.setStyleSheet("background-color: lightblue; color: black; border: 1px solid grey; border-radius: 7px;")
        arr = self.edit.toPlainText().strip().split()

        arr = [int(i) for i in arr]
        ypoints = np.array(arr)
        fig = plt.figure()
        plt.ion()
        plt.pie(ypoints)
        plt.xlabel(self.xlabeledit.toPlainText())
        plt.ylabel(self.ylabeledit.toPlainText())
        plt.title(self.titleedit.toPlainText())
        # plt.legend()
        plt.ioff()
        plt.savefig("new_image.png")

        self.photo.setPixmap(QPixmap('new_image.png'))

    def scatter(self):
        self.theme()
        self.button1.setStyleSheet("background-color: lightblue; color: black; border: 1px solid grey; border-radius: 7px;")
        x = self.edit.toPlainText().strip().split()
        y = self.yedit.toPlainText().strip().split()

        xpoints = np.array([int(i) for i in x])
        ypoints = np.array([int(i) for i in y])
        fig = plt.figure()
        plt.ion()
        plt.scatter(xpoints, ypoints, marker = self.Markers[self.marker], color=self.color)
        plt.xlabel(self.xlabeledit.toPlainText())
        plt.ylabel(self.ylabeledit.toPlainText())
        plt.title(self.titleedit.toPlainText())
        # plt.legend()
        plt.ioff()
        plt.savefig("new_image.png")

        self.photo.setPixmap(QPixmap('new_image.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
