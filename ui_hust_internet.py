# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hust_internet.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QTabWidget,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(480, 320)
        MainWindow.setMinimumSize(QSize(270, 180))
        MainWindow.setMaximumSize(QSize(1080, 1080))
        font = QFont()
        font.setPointSize(22)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.PointingHandCursor))
        MainWindow.setContextMenuPolicy(Qt.ActionsContextMenu)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"QMainWindow->setScaledContents(true);\n"
"void paintEvent(QPaintEvent*) override;			\n"
"\n"
"void Widget::paintEvent(QPaintEvent*)\n"
"{\n"
"    label->resize(ui->widget->size());\n"
"}\n"
"")
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextOnly)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setCursor(QCursor(Qt.ArrowCursor))
        self.centralwidget.setStyleSheet(u"setStyleSheet{\n"
"\"border-image:url(:hust_logo.jpg)\";\n"
"}\n"
"")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 40, 111, 71))
        self.pushButton.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(16)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border:2px solid white;border-radius:10px;\n"
"color:white;\n"
"}\n"
" \n"
"QPushButton :hover{ \n"
"background-color: rgba(255, 255, 255, 150);\n"
"border:2px solid white;border-radius:10px;\n"
"}\n"
" \n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border:2px solid white;border-radius:10px;\n"
"} ")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 170, 111, 71))
        font2 = QFont()
        font2.setFamilies([u"\u9ed1\u4f53"])
        self.lineEdit.setFont(font2)
        self.lineEdit.setCursor(QCursor(Qt.ArrowCursor))
        self.lineEdit.setStyleSheet(u"/********************QLineEdit\u6837\u5f0f\uff0c\u4e5f\u9002\u7528\u4e8eItem\uff08\u5982QListView\u3001QTableView\uff09**********************/\n"
"QLineEdit{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border:2px solid white;border-radius:10px;\n"
"}\n"
" \n"
"QLineEdit :hover{ \n"
"background-color: rgba(255, 255, 255, 150);\n"
"border:2px solid white;border-radius:10px;\n"
"}\n"
" \n"
"QLineEdit:pressed{\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border:2px solid white;border-radius:10px;\n"
"} \n"
"\n"
"/* \u53ea\u8bfb\u6837\u5f0f*/\n"
"QLineEdit:read-only {\n"
"    color: white;\n"
"	font-size:18px;\n"
"\n"
"}")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(True)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(270, 170, 131, 70))
        self.textEdit.setFont(font2)
        self.textEdit.setStyleSheet(u"/********************QLineEdit\u6837\u5f0f\uff0c\u4e5f\u9002\u7528\u4e8eItem\uff08\u5982QListView\u3001QTableView\uff09**********************/\n"
"QTextEdit{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border:2px solid white;border-radius:10px;\n"
"}\n"
" \n"
"QTextEdit :hover{ \n"
"background-color: rgba(255, 255, 255, 150);\n"
"border:2px solid white;border-radius:10px;\n"
"}\n"
" \n"
"QTextEdit:pressed{\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border:2px solid white;border-radius:10px;\n"
"} \n"
"\n"
"/* \u53ea\u8bfb\u6837\u5f0f*/\n"
"QTextEdit:read-only {\n"
"    color:red;\n"
"	font-size:8px;\n"
"}")
        self.textEdit.setReadOnly(True)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 40, 131, 71))
        self.pushButton_2.setMinimumSize(QSize(0, 0))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border:2px solid white;border-radius:10px;\n"
"color:white;\n"
"}\n"
" \n"
"QPushButton :hover{ \n"
"background-color: rgba(255, 255, 255, 150);\n"
"border:2px solid white;border-radius:10px;\n"
"}\n"
" \n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border:2px solid white;border-radius:10px;\n"
"} ")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 22))
        self.menubar.setLayoutDirection(Qt.LeftToRight)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u7edc\u72b6\u6001\uff1a", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u9ed1\u4f53'; font-size:8px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Microsoft YaHei UI'; font-size:16pt;\"><br /></p></body></html>", None))
        self.textEdit.setPlaceholderText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u534e\u4e2d\u79d1\u6280\u5927\u5b66\u6821\u56ed\u7f51", None))
    # retranslateUi

