import os
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('main.ui')
form_class = uic.loadUiType(form)[0]

form_list = resource_path('list.ui')
form_listWindow = uic.loadUiType(form_list)[0]

form_status = resource_path('status.ui')
form_statusWindow = uic.loadUiType(form_status)[0]

form_edit = resource_path('edit.ui')
form_editWindow = uic.loadUiType(form_edit)[0]

form_search = resource_path('search.ui')
form_searchWindow = uic.loadUiType(form_search)[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    

    def btn_main_to_list(self):
        self.hide()                     # 메인윈도우 숨김
        self.list = listWindow()
        self.list.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐짐

    def btn_main_to_status(self):
        self.hide()                     # 메인윈도우 숨김
        self.status = statusWindow()    #
        self.status.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐짐

    def btn_main_to_edit(self):
        self.hide()                     # 메인윈도우 숨김
        self.edit = editWindow()
        self.edit.exec()               # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐짐

    def btn_main_to_search(self):
        self.hide()                     # 메인윈도우 숨김
        self.search = searchWindow()    #
        self.search.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐짐

class listWindow(QDialog, QWidget, form_listWindow):
    def __init__(self):
        super(listWindow, self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)

class statusWindow(QDialog, QWidget, form_statusWindow):
    def __init__(self):
        super(statusWindow, self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)

class editWindow(QDialog, QWidget, form_editWindow):
    def __init__(self):
        super(editWindow, self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)

class searchWindow(QDialog, QWidget, form_searchWindow):
    def __init__(self):
        super(searchWindow, self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()