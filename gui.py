import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from app import *
from PyQt5 import uic

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

#################### UI 가져오기 ####################
# 메인 페이지 ui
form = resource_path('main.ui')
form_class = uic.loadUiType(form)[0]

# 기숙사생 명단 확인 페이지 ui
form_list = resource_path('list.ui')
form_listWindow = uic.loadUiType(form_list)[0]

# 특정 기숙사생 상태 확인 ui
form_status = resource_path('status.ui')
form_statusWindow = uic.loadUiType(form_status)[0]

# 기숙사생 추가 / 삭제 페이지 ui
form_edit = resource_path('edit.ui')
form_editWindow = uic.loadUiType(form_edit)[0]

# 기숙사생 추가 페이지 ui
form_add = resource_path('add.ui')
form_addWindow = uic.loadUiType(form_add)[0]

# 기숙사생 삭제 페이지 ui
form_delete = resource_path('delete.ui')
form_deleteWindow = uic.loadUiType(form_delete)[0]

# 날짜 별 기숙사생 상태 확인 페이지 ui
form_search = resource_path('search.ui')
form_searchWindow = uic.loadUiType(form_search)[0]

##################### 기능 구현 #####################
# 메인 페이지
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # 종료하기 전 확인
    def closeEvent(self, event):
        quit_msg = "종료하시겠습니까?"
        reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 기숙사생 명단 확인 페이지로 이동
    def btn_main_to_list(self):
        self.hide()
        self.list = listWindow()
        self.list.exec()
        self.show()

    # 특정 기숙사생 상태 확인 페이지로 이동
    def btn_main_to_status(self):
        self.hide()
        self.status = statusWindow()
        self.status.exec()
        self.show()

    # 기숙사생 추가 / 삭제 페이지로 이동
    def btn_main_to_edit(self):
        self.hide()
        self.edit = editWindow()
        self.add = editWindow().exec()
        self.delete = editWindow().exec()
        self.edit.exec()
        self.show()

    # 날짜 별 기숙사생 상태 확인 페이지로 이동
    def btn_main_to_search(self):
        self.hide()
        self.search = searchWindow()
        self.search.exec()
        self.show()

# 기숙사생 명단 페이지
class listWindow(QDialog, QWidget, form_listWindow):
    def __init__(self):
        super(listWindow, self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)

    def show_list(self):
        self.btn_show.hide()
        self.text = checkStudent()
        self.contents = ""
        for i in self.text:
            self.contents += i
            self.contents += "\n"
        self.student_list.setText(self.contents)
# 특정 기숙사생 상태 확인 페이지
class statusWindow(QDialog, QWidget, form_statusWindow):
    def __init__(self):
        super(statusWindow, self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)

# 기숙사생 추가 / 삭제 페이지
class editWindow(QDialog, QWidget, form_editWindow):
    def __init__(self):
        super(editWindow, self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)

    # 기숙사생 추가 페이지로 이동
    def btn_edit_to_add(self):
        self.hide()
        self.add = addWindow()
        self.add.exec()
        self.close

    # 기숙사생 삭제 페이지로 이동
    def btn_edit_to_delete(self):
        self.hide()
        self.delete = deleteWindow()
        self.delete.exec()
        self.close

    # 메인 페이지로 이동
    def btn_edit_to_main(self):
        self.close()

# 기숙사생 추가 페이지
class addWindow(QDialog, QWidget, form_addWindow):
    def __init__(self):
        super(addWindow, self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)

    # 기숙사생 추가 / 삭제 페이지로 이동
    def btn_add_to_edit(self):
        self.close()

# 기숙사생 삭제 페이지로 이동
class deleteWindow(QDialog, QWidget, form_deleteWindow):
    def __init__(self):
        super(deleteWindow, self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)

    # 기숙사생 추가 / 삭제 페이지로 이동
    def btn_delete_to_edit(self):
        self.close()
        
# 날짜 별 기숙사생 상태 확인 페이지
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