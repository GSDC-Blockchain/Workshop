# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blockchain.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(427, 266)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-4, -1, 441, 271))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 251, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.groupBox = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 411, 141))
        self.groupBox.setObjectName("groupBox")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 41, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 81, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 120, 121, 16))
        self.label_9.setObjectName("label_9")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(210, 20, 111, 16))
        self.label_16.setIndent(-1)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(210, 40, 71, 16))
        self.label_17.setIndent(-1)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(210, 60, 91, 16))
        self.label_18.setIndent(-1)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(210, 80, 111, 16))
        self.label_19.setIndent(-1)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(210, 100, 101, 16))
        self.label_20.setIndent(-1)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(210, 120, 121, 16))
        self.label_21.setIndent(-1)
        self.label_21.setObjectName("label_21")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 251, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_2.addWidget(self.spinBox_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 30, 411, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(10, 20, 391, 181))
        self.label_15.setObjectName("label_15")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 0, 411, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 30, 411, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 40, 151, 16))
        self.label_11.setObjectName("label_11")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(230, 20, 81, 16))
        self.label_22.setIndent(-1)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(230, 40, 131, 16))
        self.label_23.setIndent(-1)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox_3)
        self.label_24.setGeometry(QtCore.QRect(230, 60, 141, 16))
        self.label_24.setIndent(-1)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.groupBox_3)
        self.label_25.setGeometry(QtCore.QRect(230, 80, 171, 16))
        self.label_25.setIndent(-1)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_3)
        self.label_26.setGeometry(QtCore.QRect(230, 100, 161, 16))
        self.label_26.setIndent(-1)
        self.label_26.setObjectName("label_26")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(10, 80, 171, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(10, 60, 171, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(10, 100, 201, 16))
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter Block ID:"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.groupBox.setTitle(_translate("MainWindow", "Block Information"))
        self.label_4.setText(_translate("MainWindow", "Previous Block Hash:"))
        self.label_5.setText(_translate("MainWindow", "Nonce:"))
        self.label_6.setText(_translate("MainWindow", "Timestamp:"))
        self.label_7.setText(_translate("MainWindow", "Merkle Tree Root:"))
        self.label_8.setText(_translate("MainWindow", "Hashing Target:"))
        self.label_9.setText(_translate("MainWindow", "Number of Transactions:"))
        self.label_16.setText(_translate("MainWindow", "prev block hash value"))
        self.label_17.setText(_translate("MainWindow", "nonce value"))
        self.label_18.setText(_translate("MainWindow", "timestamp value"))
        self.label_19.setText(_translate("MainWindow", "merkle tree root value"))
        self.label_20.setText(_translate("MainWindow", "hashing target value"))
        self.label_21.setText(_translate("MainWindow", "number of txs in a block"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Blocks"))
        self.label_2.setText(_translate("MainWindow", "Enter Block ID:"))
        self.pushButton_2.setText(_translate("MainWindow", "OK"))
        self.groupBox_2.setTitle(_translate("MainWindow", "List of Transactions"))
        self.label_15.setText(_translate("MainWindow", "Lista Transakcija"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Transactions"))
        self.label_3.setText(_translate("MainWindow", "Public Key:"))
        self.pushButton_3.setText(_translate("MainWindow", "OK"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Account Information"))
        self.label_10.setText(_translate("MainWindow", "Balance:"))
        self.label_11.setText(_translate("MainWindow", "Last Transaction Amount Sent:"))
        self.label_22.setText(_translate("MainWindow", "account balance"))
        self.label_23.setText(_translate("MainWindow", "last tx amount sent value"))
        self.label_24.setText(_translate("MainWindow", "last tx amount received value"))
        self.label_25.setText(_translate("MainWindow", "the last public key to receive coins"))
        self.label_26.setText(_translate("MainWindow", "the last public key to send coins"))
        self.label_12.setText(_translate("MainWindow", "Last Transaction Address Sent to:"))
        self.label_13.setText(_translate("MainWindow", "Last Transaction Amount Received:"))
        self.label_14.setText(_translate("MainWindow", "Last Transaction Address Received from:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Accounts"))

        self.pushButton.clicked.connect(lambda: self.updateTab1())
        self.pushButton_2.clicked.connect(lambda: self.updateTab2())
        self.pushButton_3.clicked.connect(lambda: self.updateTab3())

    def updateTab1(self):
        self.label_16.setText("0000043fds39gfsu32rngs86")
        self.label_17.setText("859327943257")
        self.label_18.setText("21.11.2020. 21:05:14")
        self.label_19.setText("f89s8732jfds98632jbfds84")
        self.label_20.setText("000005jtb43ktngrj5n34nt2")
        self.label_21.setText("1000")

    def updateTab2(self):
        self.label_15.setText('''
TX1: PubKey1 --10BTC--> PubKey2
TX2: PubKey3 --20BTC--> PubKey4
TX3: PubKey5 --30BTC--> PubKey6
TX4: PubKey7 --40BTC--> PubKey8
TX5: PubKey9 --50BTC--> PubKey10
        ''')
        
    def updateTab3(self):
        self.label_22.setText("50 BTC")
        self.label_23.setText("10 BTC")
        self.label_24.setText("20 BTC")
        self.label_25.setText("g898gnf89s87a32jfds98632jbfds84")
        self.label_26.setText("89t43njklmio5jtb43ktngrj5n34nt2")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
