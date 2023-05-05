# -*- coding: utf-8 -*-  #防中文乱码
import json
import os
import sys
import time
import requests
import subprocess
#
from PySide6.QtWidgets import QApplication,QMainWindow,QLineEdit,QMessageBox
from ui_hust_internet import Ui_MainWindow
import sys
from PySide6 import QtWidgets, QtGui,QtCore

##
from PySide6.QtCore import Signal, QObject,QEventLoop,QTimer


def log(info):
    log_file = os.environ.get('AUTO_NET_RECONNECT_LOG_FILE', "connect.log")
    print(info.strip())
    with open(log_file, "a") as f:
        f.write(info.strip() + "\n")


def login():
    url = 'http://192.168.50.3:8080/eportal/InterFace.do?method=login'
    config_file = os.environ.get('AUTO_NET_RECONNECT_CONFIG_FILE', "content")
    with open(config_file, "r") as f:
        data = f.read().strip('"').strip("'")
    header = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }

    try:
        response = requests.post(url, data, headers=header, timeout=10)
        content = json.loads(response.text)
        encoding = response.encoding
        if content['result'] == 'fail':
            msg = content['message'].encode(encoding).decode('utf-8')
            log(msg)
            if msg == "认证设备响应超时,请稍后再试!":
                time.sleep(120)
            if msg == '正常上网时段为:日常06:00-23:59，请在以上时段内进行认证上网!':
                time.sleep(1200)
        else:
            log("login at --> " + time.asctime(time.localtime(time.time())))
        return
    except Exception as info:
        log("login 连接异常:" + str(info))


def ping(host, n):
    cmd = "ping {} {} {} > ping.log".format(
        "-n" if sys.platform.lower() == "win32" else "-c",
        n,
        host,
    )
    return 0 == subprocess.call(cmd,shell=True)


def pong():
    return ping("202.114.0.242", 4) or ping("8.8.8.8", 4)


class EmittingStr(QtCore.QObject):
    textWritten = QtCore.Signal(str)

    def write(self, text):
        self.textWritten.emit(str(text))
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()
        QApplication.processEvents()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.pix = QtGui.QPixmap('net.jpg')

        size = self.pix.size()
        self.process = QLineEdit(self, readOnly=True)
        # QtWidgets.QLineEdit(self,)
        self.label1 = QtWidgets.QLabel(self)
        # self.label1.setScaledContents(True)
        self.label1.setGeometry(0,20,size.width()/3.3,size.height()/3)
        self.label1.setScaledContents(True) #缩放
        self.label1.setPixmap(self.pix)

        self.ui = Ui_MainWindow()  # UI类的实例化()
        self.ui.setupUi(self)
        self.band()
        ##重定向控制台输出
        sys.stdout = EmittingStr()
        sys.stdout.textWritten.connect(self.outputWritten)

        # self.pushButton.clicked.connect(self.bClicked)
        # self.string = None


    def band(self):
        # self.ui.___ACTION___.triggered.connect(___FUNCTION___)
        # self.ui.___BUTTON___.clicked.connect(___FUNCTION___)
        # self.ui.___COMBO_BOX___.currentIndexChanged.connect(___FUNCTION___)
        # self.ui.___SPIN_BOX___.valueChanged.connect(___FUNCTION___)
        # 自定义信号.属性名.connect(___FUNCTION___)
        self.ui.pushButton.clicked.connect(self.running)
        self.ui.pushButton_2.clicked.connect(self.close)

    def outputWritten(self, text):

        cursor = self.ui.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.textEdit.setTextCursor(cursor)
        self.ui.textEdit.ensureCursorVisible()


    def closeEvent(self, event):
        reply = QMessageBox.question(self, '关闭提示', "是否退出界面？",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            sys.exit(0)
        elif reply == QMessageBox.No:
            event.ignore()


    def running(self):
        judge = True
        while judge:
            if pong():
                print("网络正常")
            else:
                try:
                    login()
                    print("重新连接成功")
                    # time.sleep(2)
                except:
                    print("网络故障")
                    judge=False




if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = MainWindow()  # 实例化主窗口
    window.show()  # 展示主窗口
    sys.exit(app.exec())  # 避免程序执行到这一行后直接退出