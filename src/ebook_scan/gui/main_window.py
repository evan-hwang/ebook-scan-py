import sys
import os
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMainWindow, QVBoxLayout, \
    QHBoxLayout, QSlider

# 새로 만든 클래스들 임포트
from ebook_scan.core.coordinate_manager import CoordinateManager
from ebook_scan.core.screen_capture_manager import ScreenCaptureManager
from ebook_scan.core.pdf_generator import PDFGenerator
from ebook_scan.config.app_config import ApplicationConfig


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # 새로운 매니저 클래스들 초기화
        self.coordinate_manager = CoordinateManager()
        self.screen_capture_manager = ScreenCaptureManager()
        self.pdf_generator = PDFGenerator()
        self.config = ApplicationConfig()

        # UI 초기화
        self._init_ui()

    def _init_ui(self):
        """UI 요소 초기화"""
        # 앱 타이틀
        self.setWindowTitle(self.config.app_title)

        # 버튼 생성
        self.button1 = QPushButton("좌측상단 좌표 클릭")
        self.button2 = QPushButton("우측하단 좌표 클릭")
        self.button3 = QPushButton("PDF로 만들기")
        self.button3.setFixedSize(QSize(430, 60))
        self.button4 = QPushButton("초기화")

        # 버튼 클릭 이벤트
        self.button1.clicked.connect(self._capture_top_left_coordinate)
        self.button2.clicked.connect(self._capture_bottom_right_coordinate)
        self.button3.clicked.connect(self._start_capture_and_generate_pdf)
        self.button4.clicked.connect(self._reset_all)

        # 속도 slider
        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(int(self.config.min_speed * 10))
        self.speed_slider.setMaximum(int(self.config.max_speed * 10))
        self.speed_slider.setValue(int(self.config.default_speed * 10))
        self.speed_slider.valueChanged.connect(self._change_speed)

        self.speed_label = QLabel(f'캡쳐 속도: {self.config.default_speed:.1f}초')
        self.speed_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        font_speed = self.speed_label.font()
        font_speed.setPointSize(10)
        self.speed_label.setFont(font_speed)

        self.title = QLabel(self.config.app_title, self)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font_title = self.title.font()
        font_title.setPointSize(20)
        self.title.setFont(font_title)

        self.stat = QLabel('', self)
        self.stat.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font_stat = self.stat.font()
        font_stat.setPointSize(18)
        font_stat.setBold(True)
        self.stat.setFont(font_stat)

        self.sign = QLabel('Made By EastShine', self)
        self.sign.setAlignment(Qt.AlignmentFlag.AlignRight)
        font_sign = self.stat.font()
        font_sign.setPointSize(10)
        font_sign.setItalic(True)
        self.sign.setFont(font_sign)

        self.label1 = QLabel('이미지 좌측상단 좌표   ==>   ', self)
        self.label1_1 = QLabel('(0, 0)', self)
        self.label2 = QLabel('이미지 우측하단 좌표   ==>   ', self)
        self.label2_1 = QLabel('(0, 0)', self)
        self.label3 = QLabel('총 페이지 수                       ', self)
        self.label4 = QLabel('PDF 이름                         ', self)

        self.input1 = QLineEdit()
        self.input1.setPlaceholderText("총 페이지 수를 입력하세요.")

        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("생성할 PDF의 이름을 입력하세요.")

        # Box 설정
        box1 = QHBoxLayout()
        box1.addWidget(self.label1)
        box1.addWidget(self.label1_1)
        box1.addWidget(self.button1)

        box2 = QHBoxLayout()
        box2.addWidget(self.label2)
        box2.addWidget(self.label2_1)
        box2.addWidget(self.button2)

        box3 = QHBoxLayout()
        box3.addWidget(self.label3)
        box3.addWidget(self.input1)

        box4 = QHBoxLayout()
        box4.addWidget(self.label4)
        box4.addWidget(self.input2)

        box5 = QHBoxLayout()
        box5.addWidget(self.speed_label)
        box5.addWidget(self.speed_slider)

        box6 = QHBoxLayout()
        box6.addWidget(self.stat)
        box6.addWidget(self.button4)
        box6.addWidget(self.sign)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addStretch(2)
        layout.addLayout(box1)
        layout.addStretch(1)
        layout.addLayout(box2)
        layout.addStretch(1)
        layout.addLayout(box3)
        layout.addStretch(1)
        layout.addLayout(box4)
        layout.addStretch(4)
        layout.addLayout(box5)
        layout.addLayout(box6)
        layout.addWidget(self.button3)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        # 창 크기 고정
        self.setFixedSize(QSize(450, 320))

    def _capture_top_left_coordinate(self):
        """좌측상단 좌표 클릭 캡처"""
        def update_label(x, y):
            self.label1_1.setText(f'({x}, {y})')

        self.stat.setText('좌측상단 좌표를 클릭하세요...')
        self.coordinate_manager.capture_top_left_coordinate(update_label)
        self.stat.setText('')

    def _capture_bottom_right_coordinate(self):
        """우측하단 좌표 클릭 캡처"""
        def update_label(x, y):
            self.label2_1.setText(f'({x}, {y})')

        self.stat.setText('우측하단 좌표를 클릭하세요...')
        self.coordinate_manager.capture_bottom_right_coordinate(update_label)
        self.stat.setText('')

    def _change_speed(self):
        """속도 변경"""
        speed = self.speed_slider.value() / 10.0
        self.config.set_speed(speed)
        self.screen_capture_manager.set_speed(speed)
        self.speed_label.setText(f'캡쳐 속도: {speed:.1f}초')

    def _validate_inputs(self):
        """입력 값 검증"""
        if not self.input1.text():
            self.stat.setText('페이지 수를 입력하세요.')
            self.input1.setFocus()
            return False

        if not self.input2.text():
            self.stat.setText('PDF 제목을 입력하세요.')
            self.input2.setFocus()
            return False

        try:
            total_pages = int(self.input1.text())
            if total_pages <= 0:
                self.stat.setText('페이지 수는 1 이상이어야 합니다.')
                self.input1.setFocus()
                return False
        except ValueError:
            self.stat.setText('올바른 페이지 수를 입력하세요.')
            self.input1.setFocus()
            return False

        return True

    def _start_capture_and_generate_pdf(self):
        """캡처 시작 및 PDF 생성"""
        # 입력 값 검증
        if not self._validate_inputs():
            return

        # 설정 값 업데이트
        total_pages = int(self.input1.text())
        pdf_filename = self.input2.text()

        self.config.set_total_pages(total_pages)
        self.config.set_pdf_filename(pdf_filename)

        try:
            self.stat.setText('캡쳐 중...')
            QApplication.processEvents()  # UI 업데이트를 즉시 반영

            # 좌표 영역 가져오기
            region = self.coordinate_manager.get_region()

            # 스크린 캡처 시작
            self.screen_capture_manager.capture_pages(
                region,
                total_pages,
                self.config.get_image_output_directory()
            )

            self.stat.setText('PDF 변환 중...')
            QApplication.processEvents()  # UI 업데이트를 즉시 반영

            # PDF 생성
            pdf_path = pdf_filename if pdf_filename.endswith('.pdf') else f"{pdf_filename}.pdf"
            self.pdf_generator.convert_images_to_pdf(
                self.config.get_image_output_directory(),
                pdf_path
            )

            # 이미지 디렉토리 정리
            self.pdf_generator.cleanup_image_directory(self.config.get_image_output_directory())

            self.stat.setText('PDF 생성 완료!')

        except Exception as e:
            print('예외 발생. ', e)
            self.stat.setText('오류 발생. 종료 후 다시 시도해주세요.')

    def _reset_all(self):
        """모든 설정 초기화"""
        # 매니저 클래스들 초기화
        self.coordinate_manager.reset()
        self.screen_capture_manager.reset()
        self.pdf_generator.reset()
        self.config.reset()

        # UI 요소 초기화
        self.label1_1.setText('(0, 0)')
        self.label2_1.setText('(0, 0)')
        self.input1.clear()
        self.input2.clear()
        self.stat.clear()
        self.speed_slider.setValue(int(self.config.default_speed * 10))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()