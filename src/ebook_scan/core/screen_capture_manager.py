import time
import random
import os
import mss
import mss.tools
from pynput.keyboard import Key, Controller
from pynput import mouse


class ScreenCaptureManager:
    """스크린 캡처 및 페이지 넘김 기능을 관리하는 클래스"""

    def __init__(self, speed=0.1):
        self.speed = speed
        self.kb_control = Controller()
        self.mouse_controller = mouse.Controller()
        self.mouse_button_left = mouse.Button.left
        self.current_page = 1

    def set_speed(self, speed):
        """캡처 속도 설정"""
        self.speed = speed

    def _generate_random_speed(self, speed, percent):
        """랜덤 속도 생성"""
        # 퍼센트를 소수로 변환 (예: 50% -> 0.5)
        percent = percent / 100

        # 최소값과 최대값 계산
        min_value = speed - (speed * percent)
        max_value = speed + (speed * percent)

        # 랜덤값 생성 및 반환
        return random.uniform(min_value, max_value)

    def capture_screen_region(self, region, output_path):
        """지정된 영역을 캡처하여 파일로 저장"""
        with mss.mss() as sct:
            # Grab the data
            img = sct.grab(region)
            # Save to the picture file
            mss.tools.to_png(img.rgb, img.size, output=output_path)

    def turn_page(self):
        """페이지 넘기기"""
        self.kb_control.press(Key.right)
        self.kb_control.release(Key.right)

    def click_position(self, x, y):
        """지정된 위치 클릭"""
        original_position = self.mouse_controller.position
        self.mouse_controller.position = (x, y)
        time.sleep(0.1)
        self.mouse_controller.click(self.mouse_button_left)
        time.sleep(0.1)
        self.mouse_controller.position = original_position

    def capture_pages(self, region, total_pages, output_dir='pdf_images'):
        """페이지별로 스크린 캡처 수행"""
        # 출력 디렉토리 생성
        if not os.path.isdir(output_dir):
            os.mkdir(os.path.join(output_dir))

        self.current_page = 1

        try:
            # 파일 저장
            while self.current_page <= total_pages:
                # 랜덤 지연 시간 적용
                time.sleep(self._generate_random_speed(self.speed, 50))

                # 캡쳐하기
                output_path = f'{output_dir}/img_{str(self.current_page).zfill(4)}.png'
                self.capture_screen_region(region, output_path)

                # 마지막 페이지가 아니면 페이지 넘기기
                if self.current_page < total_pages:
                    self.turn_page()

                self.current_page += 1

            print("캡쳐 완료!")
            return True

        except Exception as e:
            print('예외 발생. ', e)
            raise e

    def reset(self):
        """상태 초기화"""
        self.current_page = 1