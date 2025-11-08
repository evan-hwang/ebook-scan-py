from pynput import mouse
import time


class Coordinate:
    """좌표 정보를 저장하는 클래스"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class CoordinateManager:
    """좌표 관리 및 마우스 클릭 처리 클래스"""

    def __init__(self):
        self.top_left = Coordinate()
        self.bottom_right = Coordinate()

    def set_top_left(self, x, y):
        """좌측상단 좌표 설정"""
        self.top_left.set_coordinates(x, y)

    def set_bottom_right(self, x, y):
        """우측하단 좌표 설정"""
        self.bottom_right.set_coordinates(x, y)

    def get_top_left(self):
        """좌측상단 좌표 반환"""
        return self.top_left

    def get_bottom_right(self):
        """우측하단 좌표 반환"""
        return self.bottom_right

    def get_region(self):
        """캡처 영역 정보 반환"""
        return {
            'top': self.top_left.get_y(),
            'left': self.top_left.get_x(),
            'width': self.bottom_right.get_x() - self.top_left.get_x(),
            'height': self.bottom_right.get_y() - self.top_left.get_y()
        }

    def capture_top_left_coordinate(self, callback=None):
        """좌측상단 좌표 클릭 캡처"""
        def on_click(x, y, button, pressed):
            if pressed:
                self.set_top_left(int(x), int(y))
                if callback:
                    callback(int(x), int(y))
                print(f'좌측상단 좌표 캡처: ({int(x)}, {int(y)})')
                return False  # 첫 클릭 후 리스너 종료

        with mouse.Listener(on_click=on_click) as listener:
            listener.join()

    def capture_bottom_right_coordinate(self, callback=None):
        """우측하단 좌표 클릭 캡처"""
        def on_click(x, y, button, pressed):
            if pressed:
                self.set_bottom_right(int(x), int(y))
                if callback:
                    callback(int(x), int(y))
                print(f'우측하단 좌표 캡처: ({int(x)}, {int(y)})')
                return False  # 첫 클릭 후 리스너 종료

        with mouse.Listener(on_click=on_click) as listener:
            listener.join()

    def reset(self):
        """좌표 정보 초기화"""
        self.top_left.set_coordinates(0, 0)
        self.bottom_right.set_coordinates(0, 0)