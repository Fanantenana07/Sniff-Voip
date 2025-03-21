# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Liste_Audio.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import playsound

class Ui_Liste_Audio(object):
    def setupUi(self, Liste_Audio):
        Liste_Audio.setObjectName("Liste_Audio")
        Liste_Audio.resize(723, 522)
        Liste_Audio.setStyleSheet("background-color: rgb(0, 0, 8);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Liste_Audio)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Liste_Audio)
        self.frame.setMaximumSize(QtCore.QSize(800, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(800, 450))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setMinimumSize(QtCore.QSize(672, 0))
        self.tableWidget.setStyleSheet("QHeaderView::section:horizontal{\n"
        "background-color: rgb(170, 170, 255);\n"
        "color: rgb(0, 0, 8);\n"
        "    font: 75 10pt \"Segoe UI\";\n"
        "}")
        self.tableWidget.setStyleSheet("background-color:white")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        self.list_audio()

        self.retranslateUi(Liste_Audio)
        QtCore.QMetaObject.connectSlotsByName(Liste_Audio)

    def retranslateUi(self, Liste_Audio):
        _translate = QtCore.QCoreApplication.translate
        Liste_Audio.setWindowTitle(_translate("Liste_Audio", "Liste Audio"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Liste_Audio", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Liste_Audio", "Extension"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Liste_Audio", "Jouer"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Liste_Audio", "Supprimer"))
    
    def list_audio(self):
        directory = os.getcwd().replace("\\","/")
        liste = os.listdir(directory+"/Audio")
        self.tableWidget.setRowCount(len(liste))
        extension = " "
        i = 0
        for title in liste:
            for j in range(3):
                extension = extension + title[(len(title)-1)-j]
            self.delete = QtWidgets.QPushButton("x")
            self.play = QtWidgets.QPushButton("+")
            self.play.setStyleSheet("background-color:yellow;width:20px;height:20px;color:white;")
            self.delete.setStyleSheet("background-color:red;width:20px;height:20px;color:white;")
            self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(str(title)))
            self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(extension))
            self.tableWidget.setCellWidget(i,2,self.play)
            self.tableWidget.setCellWidget(i,3,self.delete)
            i= i+1                        
            self.delete.clicked.connect(self.remove)
            self.play.clicked.connect(self.play_audio)
    
    def remove(self):
        row = self.tableWidget.currentRow()
        col = self.tableWidget.currentColumn()
        item = self.tableWidget.item(row,0).text()
        os.remove("Audio/"+item)
        self.list_audio()
    
    def play_audio(self):
        row = self.tableWidget.currentRow()
        col = self.tableWidget.currentColumn()
        item = self.tableWidget.item(row,0).text()
        playsound.playsound("Audio/"+item)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    Liste_Audio = QtWidgets.QWidget()
    ui = Ui_Liste_Audio()
    ui.setupUi(Liste_Audio)
    Liste_Audio.show()
    sys.exit(app.exec_())
