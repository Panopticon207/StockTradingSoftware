# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kartolustur.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KartOlustur(object):
    def setupUi(self, KartOlustur):
        KartOlustur.setObjectName("KartOlustur")
        KartOlustur.resize(478, 368)
        self.buton_kartolustur = QtWidgets.QPushButton(KartOlustur)
        self.buton_kartolustur.setGeometry(QtCore.QRect(20, 250, 131, 31))
        self.buton_kartolustur.setObjectName("buton_kartolustur")
        self.layoutWidget = QtWidgets.QWidget(KartOlustur)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 61, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.layoutWidget1 = QtWidgets.QWidget(KartOlustur)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 40, 135, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_ID = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.verticalLayout_2.addWidget(self.lineEdit_ID)
        self.lineEdit_Stokadi = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_Stokadi.setObjectName("lineEdit_Stokadi")
        self.verticalLayout_2.addWidget(self.lineEdit_Stokadi)
        self.lineEdit_Marka = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_Marka.setObjectName("lineEdit_Marka")
        self.verticalLayout_2.addWidget(self.lineEdit_Marka)
        self.lineEdit_Model = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_Model.setObjectName("lineEdit_Model")
        self.verticalLayout_2.addWidget(self.lineEdit_Model)

        self.retranslateUi(KartOlustur)
        QtCore.QMetaObject.connectSlotsByName(KartOlustur)

    def retranslateUi(self, KartOlustur):
        _translate = QtCore.QCoreApplication.translate
        KartOlustur.setWindowTitle(_translate("KartOlustur", "Form"))
        self.buton_kartolustur.setText(_translate("KartOlustur", "KART OLUŞTUR"))
        self.label.setText(_translate("KartOlustur", "ID:"))
        self.label_2.setText(_translate("KartOlustur", "Stok Adı:"))
        self.label_3.setText(_translate("KartOlustur", "Marka:"))
        self.label_4.setText(_translate("KartOlustur", "Model:"))
