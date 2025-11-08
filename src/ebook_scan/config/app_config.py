class ApplicationConfig:
    """애플리케이션 설정을 관리하는 클래스"""

    def __init__(self):
        # 기본 설정 값
        self.default_speed = 0.1
        self.min_speed = 0.1
        self.max_speed = 5.0
        self.speed_step = 0.1

        # 디렉토리 설정
        self.image_output_directory = 'pdf_images'

        # 애플리케이션 정보
        self.app_title = "E-Book PDF 생성기"
        self.app_version = "1.0.0"

        # 현재 설정 값
        self.current_speed = self.default_speed
        self.total_pages = 1
        self.pdf_filename = "output.pdf"

    def set_speed(self, speed):
        """속도 설정 (범위 검증 포함)"""
        if self.min_speed <= speed <= self.max_speed:
            self.current_speed = speed
            return True
        else:
            print(f"속도 값이 유효 범위를 벗어났습니다. ({self.min_speed} ~ {self.max_speed})")
            return False

    def get_speed(self):
        """현재 속도 값 반환"""
        return self.current_speed

    def set_total_pages(self, pages):
        """총 페이지 수 설정"""
        if pages > 0:
            self.total_pages = pages
            return True
        else:
            print("페이지 수는 1 이상이어야 합니다.")
            return False

    def get_total_pages(self):
        """총 페이지 수 반환"""
        return self.total_pages

    def set_pdf_filename(self, filename):
        """PDF 파일명 설정"""
        if filename and isinstance(filename, str):
            self.pdf_filename = filename
            return True
        else:
            print("유효한 파일명을 입력해주세요.")
            return False

    def get_pdf_filename(self):
        """PDF 파일명 반환"""
        return self.pdf_filename

    def get_image_output_directory(self):
        """이미지 출력 디렉토리 반환"""
        return self.image_output_directory

    def reset(self):
        """설정 초기화"""
        self.current_speed = self.default_speed
        self.total_pages = 1
        self.pdf_filename = "output.pdf"