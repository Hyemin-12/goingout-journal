# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\python\외출일지\status.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(16)
        Form.setFont(font)
        self.btn_search_room = QtWidgets.QPushButton(Form)
        self.btn_search_room.setGeometry(QtCore.QRect(310, 130, 171, 51))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(14)
        self.btn_search_room.setFont(font)
        self.btn_search_room.setObjectName("btn_search_room")
        self.status_title = QtWidgets.QLabel(Form)
        self.status_title.setGeometry(QtCore.QRect(130, 220, 561, 51))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(18)
        self.status_title.setFont(font)
        self.status_title.setObjectName("status_title")
        self.selected = QtWidgets.QLabel(Form)
        self.selected.setGeometry(QtCore.QRect(170, 470, 151, 41))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(18)
        self.selected.setFont(font)
        self.selected.setText("")
        self.selected.setObjectName("selected")
        self.status = QtWidgets.QLabel(Form)
        self.status.setGeometry(QtCore.QRect(330, 470, 121, 41))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(18)
        self.status.setFont(font)
        self.status.setText("")
        self.status.setObjectName("status")
        self.btn_change_status = QtWidgets.QPushButton(Form)
        self.btn_change_status.setGeometry(QtCore.QRect(460, 460, 150, 60))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(12)
        self.btn_change_status.setFont(font)
        self.btn_change_status.setObjectName("btn_change_status")
        self.room_number = QtWidgets.QPlainTextEdit(Form)
        self.room_number.setGeometry(QtCore.QRect(450, 60, 221, 50))
        self.room_number.setObjectName("room_number")
        self.status_title_2 = QtWidgets.QLabel(Form)
        self.status_title_2.setGeometry(QtCore.QRect(140, 60, 311, 51))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(18)
        self.status_title_2.setFont(font)
        self.status_title_2.setObjectName("status_title_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(140, 280, 531, 151))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.member4 = QtWidgets.QRadioButton(self.groupBox)
        self.member4.setGeometry(QtCore.QRect(290, 90, 171, 51))
        self.member4.setText("")
        self.member4.setObjectName("member4")
        self.member1 = QtWidgets.QRadioButton(self.groupBox)
        self.member1.setGeometry(QtCore.QRect(70, 20, 171, 51))
        self.member1.setText("")
        self.member1.setObjectName("member1")
        self.member2 = QtWidgets.QRadioButton(self.groupBox)
        self.member2.setGeometry(QtCore.QRect(290, 20, 171, 51))
        self.member2.setText("")
        self.member2.setObjectName("member2")
        self.member3 = QtWidgets.QRadioButton(self.groupBox)
        self.member3.setGeometry(QtCore.QRect(70, 90, 171, 51))
        self.member3.setText("")
        self.member3.setObjectName("member3")
        self.status_group = QtWidgets.QGroupBox(Form)
        self.status_group.setGeometry(QtCore.QRect(450, 430, 221, 161))
        self.status_group.setTitle("")
        self.status_group.setObjectName("status_group")
        self.status1 = QtWidgets.QRadioButton(self.status_group)
        self.status1.setGeometry(QtCore.QRect(40, 20, 141, 31))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(14)
        self.status1.setFont(font)
        self.status1.setObjectName("status1")
        self.status2 = QtWidgets.QRadioButton(self.status_group)
        self.status2.setGeometry(QtCore.QRect(40, 60, 140, 30))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(14)
        self.status2.setFont(font)
        self.status2.setObjectName("status2")
        self.status3 = QtWidgets.QRadioButton(self.status_group)
        self.status3.setGeometry(QtCore.QRect(40, 100, 140, 30))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(14)
        self.status3.setFont(font)
        self.status3.setObjectName("status3")
        self.save_status = QtWidgets.QPushButton(Form)
        self.save_status.setGeometry(QtCore.QRect(640, 480, 100, 50))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(12)
        self.save_status.setFont(font)
        self.save_status.setObjectName("save_status")

        self.retranslateUi(Form)
        self.btn_search_room.clicked.connect(Form.getText) # type: ignore
        self.member1.clicked.connect(Form.checkStatus) # type: ignore
        self.member2.clicked.connect(Form.checkStatus) # type: ignore
        self.member3.clicked.connect(Form.checkStatus) # type: ignore
        self.member4.clicked.connect(Form.checkStatus) # type: ignore
        self.btn_change_status.clicked.connect(Form.changeStatus) # type: ignore
        self.save_status.clicked.connect(Form.saveStatus) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_search_room.setText(_translate("Form", "검색"))
        self.status_title.setText(_translate("Form", "기숙사생의 이름을 선택해주세요."))
        self.btn_change_status.setText(_translate("Form", "상태 변경"))
        self.status_title_2.setText(_translate("Form", "호실 번호 입력 : "))
        self.status1.setText(_translate("Form", "잔류중"))
        self.status2.setText(_translate("Form", "외출중"))
        self.status3.setText(_translate("Form", "외박중"))
        self.save_status.setText(_translate("Form", "저장하기"))
