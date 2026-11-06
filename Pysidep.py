# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Design.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(381, 284)
        Dialog.setWindowOpacity(6.000000000000000)
        Dialog.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"font: italic 14pt \"Vivaldi\";\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainLabel = QLabel(Dialog)
        self.mainLabel.setObjectName(u"mainLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainLabel.sizePolicy().hasHeightForWidth())
        self.mainLabel.setSizePolicy(sizePolicy)
        self.mainLabel.setMinimumSize(QSize(0, 3))
        font = QFont()
        font.setFamilies([u"Symbol"])
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.mainLabel.setFont(font)
        self.mainLabel.setToolTipDuration(1)
        self.mainLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.mainLabel.setStyleSheet(u"color: black;\n"
"font: 24pt \"Symbol\";")
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.mainLabel)

        self.ParoleLabel = QLabel(Dialog)
        self.ParoleLabel.setObjectName(u"ParoleLabel")
        sizePolicy.setHeightForWidth(self.ParoleLabel.sizePolicy().hasHeightForWidth())
        self.ParoleLabel.setSizePolicy(sizePolicy)
        self.ParoleLabel.setMinimumSize(QSize(0, 3))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Symbol"])
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        self.ParoleLabel.setFont(font1)
        self.ParoleLabel.setToolTipDuration(1)
        self.ParoleLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ParoleLabel.setStyleSheet(u"color: black;\n"
"font: 18pt \"Segoe UI Symbol\";")
        self.ParoleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.ParoleLabel.setMargin(1)

        self.verticalLayout.addWidget(self.ParoleLabel)

        self.CopyBut = QPushButton(Dialog)
        self.CopyBut.setObjectName(u"CopyBut")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.CopyBut.sizePolicy().hasHeightForWidth())
        self.CopyBut.setSizePolicy(sizePolicy1)
        self.CopyBut.setMinimumSize(QSize(360, 30))
        self.CopyBut.setSizeIncrement(QSize(20, 400))
        self.CopyBut.setStyleSheet(u"background-color:rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: italic 8pt \"Vivaldi\";")
        self.CopyBut.setAutoRepeat(True)
        self.CopyBut.setAutoRepeatInterval(100)
        self.CopyBut.setAutoDefault(False)

        self.verticalLayout.addWidget(self.CopyBut)

        self.generateButton = QPushButton(Dialog)
        self.generateButton.setObjectName(u"generateButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.generateButton.sizePolicy().hasHeightForWidth())
        self.generateButton.setSizePolicy(sizePolicy2)
        self.generateButton.setMinimumSize(QSize(0, 0))
        self.generateButton.setToolTipDuration(1)
        self.generateButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.generateButton.setStyleSheet(u"color:  rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 0);\n"
"box-shadow: 0 0 0 10px rgba(0, 0, 0, 0.1px);\n"
"font: 700 9pt \"Segoe Script\";")
        self.generateButton.setAutoRepeatDelay(294)

        self.verticalLayout.addWidget(self.generateButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.mainLabel.setText(QCoreApplication.translate("Dialog", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u043f\u0430\u0440\u043e\u043b\u0435\u0439 v5", None))
        self.ParoleLabel.setText(QCoreApplication.translate("Dialog", u"\u0417\u0434\u0435\u0441\u044c \u043f\u043e\u044f\u0432\u0438\u0442\u0441\u044f \u043f\u0430\u0440\u043e\u043b\u044c...", None))
        self.CopyBut.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c \u0432 \u0431\u0443\u0444\u0435\u0440 \u043e\u0431\u043c\u0435\u043d\u0430...", None))
        self.generateButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
    # retranslateUi

