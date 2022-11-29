import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *   
from app import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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

# # 날짜 별 기숙사생 상태 확인 페이지 ui
# form_search = resource_path('search.ui')
# form_searchWindow = uic.loadUiType(form_search)[0]

##################### 기능 구현 #####################
# 메인 페이지
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_search.hide()

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

    # # 날짜 별 기숙사생 상태 확인 페이지로 이동
    # def btn_main_to_search(self):
    #     self.hide()
    #     self.search = searchWindow()
    #     self.search.exec()
    #     self.show()

# 기숙사생 명단 페이지
class listWindow(QDialog, QWidget, form_listWindow):
    def __init__(self):
        super(listWindow, self).__init__()
        self.initUi()
        self.show()
        self.text = checkStudent()
        self.contents = ""
        for i in range(0, len(self.text)) :
            if i == len(self.text) - 1:
                self.contents += self.text[i]
            else:
                self.contents += self.text[i]
                self.contents += "\n"
        self.student_list.setText(self.contents)
        self.scrollArea.setWidget(self.student_list)

    def initUi(self):
        self.setupUi(self)

# 특정 기숙사생 상태 확인 페이지
class statusWindow(QDialog, QWidget, form_statusWindow):
    def __init__(self):
        super(statusWindow, self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)
        self.status_group.hide()
        self.save_status.hide()
        self.groupBox.hide()
        self.status_title.hide()
        self.btn_change_status.hide()

    # 특정 호실 기숙사생 불러오기
    def getText(self):
        self.status_title.show()
        self.groupBox.show()
        self.member1.hide()
        self.member2.hide()
        self.member3.hide()
        self.member4.hide()
        self.names = getParticularStudents(self.room_number.toPlainText())
        if len(self.names) == 1:
            self.status_title.setText("기숙사생의 이름을 선택해주세요.")
            self.status_title.setText("빈 방입니다.")
            self.member1.show()
            self.member1.setText(self.names[0])
        elif len(self.names) == 2:
            self.status_title.setText("기숙사생의 이름을 선택해주세요.")
            self.member1.show()
            self.member2.show()
            self.member1.setText(self.names[0])
            self.member2.setText(self.names[1])
        elif len(self.names) == 3:
            self.status_title.setText("기숙사생의 이름을 선택해주세요.")
            self.member1.show() 
            self.member2.show()
            self.member3.show()
            self.member1.setText(self.names[0])
            self.member2.setText(self.names[1])
            self.member3.setText(self.names[2])
        elif len(self.names) == 4:
            self.status_title.setText("기숙사생의 이름을 선택해주세요.")
            self.member1.show()
            self.member2.show()
            self.member3.show()
            self.member4.show()
            self.member1.setText(self.names[0])
            self.member2.setText(self.names[1])
            self.member3.setText(self.names[2])
            self.member4.setText(self.names[3])
        else:
            self.groupBox.hide()
            self.status_title.setText("빈 방입니다.")

    # 특정 기숙사생 상태 확인하기
    def checkStatus(self):
        self.btn_change_status.show()
        self.names = getParticularStudents(self.room_number.toPlainText())
        if self.member1.isChecked():
            self.get_name = checkParticularStudent(self.member1.text())[0]
            self.get_status = checkParticularStudent(self.member1.text())[1]
        elif self.member2.isChecked():
            self.get_name = checkParticularStudent(self.member2.text())[0]
            self.get_status = checkParticularStudent(self.member2.text())[1]
        elif self.member3.isChecked():
            self.get_name = checkParticularStudent(self.member3.text())[0]
            self.get_status = checkParticularStudent(self.member3.text())[1]
        elif self.member4.isChecked():
            self.get_name = checkParticularStudent(self.member4.text())[0]
            self.get_status = checkParticularStudent(self.member4.text())[1]

        self.selected.setText(f"{self.get_name} : ")
        self.status.setText(self.get_status)

    def changeStatus(self):
        self.btn_change_status.hide()
        self.status_group.show()
        self.save_status.show()

    def saveStatus(self):
        if self.status1.isChecked():
            self.status.setText(changeParticularStudent(self.get_name, "잔류중"))
        elif self.status2.isChecked():
            self.status.setText(changeParticularStudent(self.get_name, "외출중"))
        elif self.status3.isChecked():
            self.status.setText(changeParticularStudent(self.get_name, "외박중"))
        self.status_group.hide()
        self.save_status.hide()
        self.btn_change_status.show()
        
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

    # 기숙사생 추가하기
    def getAddInput(self):
        addStudent(self.add_room_number.toPlainText(), self.add_name.toPlainText())
        quit_msg = "성공적으로 추가되었습니다!"
        QMessageBox.information(self, 'Message', quit_msg)

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

    # 기숙사생 삭제하기
    def getDeleteInput(self):
        deleteStudent(self.delete_room_number.toPlainText(), self.delete_name.toPlainText())
        quit_msg = "성공적으로 삭제되었습니다!"
        QMessageBox.information(self, 'Message', quit_msg)
        
# # 날짜 별 기숙사생 상태 확인 페이지
# class searchWindow(QDialog, QWidget, form_searchWindow):
#     def __init__(self):
#         super(searchWindow, self).__init__()
#         self.initUi()
#         self.show()

#     def initUi(self):
#         self.setupUi(self)

#     # 날짜, 호실, 이름 입력해서 검색하기

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

# 참고 사이트
# 창 닫을 때 팝업 : https://investox.tistory.com/entry/파이썬-PyQt5-창-닫힐-때-이벤트-실행하기
# 버튼 클릭 시 창 전환 : https://trading-for-chicken.tistory.com/23
# QMessageBox 사용 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=huntingbear21&logNo=221825482802
# QRadioButton 사용 : https://wikidocs.net/35486
# QPlainTextEdit 사용 : https://wikidocs.net/35492
# QScrollArea 사용 : https://wikidocs.net/163920