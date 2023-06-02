# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'leachUI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(729, 445)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(729, 445))
        MainWindow.setMaximumSize(QSize(729, 445))
        self.actionHow_it_works = QAction(MainWindow)
        self.actionHow_it_works.setObjectName(u"actionHow_it_works")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionCheck_for_Updates = QAction(MainWindow)
        self.actionCheck_for_Updates.setObjectName(u"actionCheck_for_Updates")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(323, 316))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(25, 90, 71, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(25, 156, 171, 16))
        self.label_2.setTextFormat(Qt.RichText)
        self.doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(160, 88, 62, 22))
        self.doubleSpinBox_2 = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setGeometry(QRect(160, 154, 62, 22))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(25, 248, 71, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(15, 20, 291, 16))
        self.label_4.setTextFormat(Qt.RichText)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 90, 131, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(230, 156, 131, 16))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 271, 301, 81))
        self.textEdit.setReadOnly(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(640, 360, 71, 31))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 360, 111, 31))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(340, 20, 371, 331))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 50, 301, 20))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(340, 360, 91, 31))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(67, 248, 71, 16))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 200, 91, 30))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(25, 119, 91, 16))
        self.doubleSpinBox_3 = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setEnabled(True)
        self.doubleSpinBox_3.setGeometry(QRect(160, 116, 62, 22))
        self.doubleSpinBox_3.setDecimals(2)
        self.doubleSpinBox_3.setMinimum(-100000000000000004764729344.000000000000000)
        self.doubleSpinBox_3.setMaximum(5.000000000000000)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(230, 119, 131, 16))
        self.label_9.setTextFormat(Qt.RichText)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 729, 21))
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuInfo.menuAction())
        self.menuInfo.addAction(self.actionHow_it_works)
        self.menuInfo.addAction(self.actionCheck_for_Updates)
        self.menuInfo.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionHow_it_works.setText(QCoreApplication.translate("MainWindow", u"How it works", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionCheck_for_Updates.setText(QCoreApplication.translate("MainWindow", u"Check for Updates", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Koc in mL/g:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>DegT50<span style=\" vertical-align:sub;\">soil </span>(@12 \u00b0C) in d:</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Result:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Calculate Leachability of a Substance:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"within [0; 10,000]", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"within [1; 365]", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Copy to Clipboard", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Save Figure", None))
        self.label_7.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Calculate List", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"log Koc/(mL/g):", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"within (-\u221e; 4]", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
    # retranslateUi

