# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\scripts\pyplotter\pyplotter\ui\dialogs\dialogMenuDatabaseDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MenuDataBaseDisplay(object):
    def setupUi(self, MenuDataBaseDisplay):
        MenuDataBaseDisplay.setObjectName("MenuDataBaseDisplay")
        MenuDataBaseDisplay.resize(248, 263)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(MenuDataBaseDisplay)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxColumnDisplay = QtWidgets.QGroupBox(MenuDataBaseDisplay)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxColumnDisplay.setFont(font)
        self.groupBoxColumnDisplay.setObjectName("groupBoxColumnDisplay")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBoxColumnDisplay)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayoutColumnDisplay = QtWidgets.QVBoxLayout()
        self.verticalLayoutColumnDisplay.setObjectName("verticalLayoutColumnDisplay")
        self.verticalLayout_4.addLayout(self.verticalLayoutColumnDisplay)
        self.verticalLayout.addWidget(self.groupBoxColumnDisplay)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(MenuDataBaseDisplay)
        QtCore.QMetaObject.connectSlotsByName(MenuDataBaseDisplay)

    def retranslateUi(self, MenuDataBaseDisplay):
        _translate = QtCore.QCoreApplication.translate
        MenuDataBaseDisplay.setWindowTitle(_translate("MenuDataBaseDisplay", "Database display"))
        self.groupBoxColumnDisplay.setTitle(_translate("MenuDataBaseDisplay", "Column to display"))