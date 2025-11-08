from PyQt5.QtWidgets import QMainWindow

class UiWindow(QMainWindow):

    def __init__(self):
        self.setWindowTitle("이북 추출기")
        self.statusBar().showMessage("순서대로 진행하세요. 버튼에 마우스를 올리면 설명이 나옵니다.")