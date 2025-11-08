#!/usr/bin/env python3
"""
리팩토링된 ebook-scan-py 프로젝트의 컴포넌트들을 테스트하는 스크립트
"""

import os
import sys
import tempfile
import shutil
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ebook_scan.core.coordinate_manager import CoordinateManager, Coordinate
from ebook_scan.config.app_config import ApplicationConfig
from ebook_scan.core.screen_capture_manager import ScreenCaptureManager


def test_coordinate_manager():
    """CoordinateManager 테스트"""
    print("Testing CoordinateManager...")

    cm = CoordinateManager()

    # 좌표 설정 테스트
    cm.set_top_left(100, 200)
    cm.set_bottom_right(300, 400)

    top_left = cm.get_top_left()
    bottom_right = cm.get_bottom_right()

    assert isinstance(top_left, Coordinate)
    assert isinstance(bottom_right, Coordinate)
    assert top_left.get_x() == 100
    assert top_left.get_y() == 200
    assert bottom_right.get_x() == 300
    assert bottom_right.get_y() == 400

    # 영역 정보 테스트
    region = cm.get_region()
    expected_region = {
        'top': 200,
        'left': 100,
        'width': 200,
        'height': 200
    }

    assert region == expected_region

    # 리셋 테스트
    cm.reset()
    assert cm.get_top_left().get_x() == 0
    assert cm.get_top_left().get_y() == 0
    assert cm.get_bottom_right().get_x() == 0
    assert cm.get_bottom_right().get_y() == 0

    print("CoordinateManager tests passed!")


def test_application_config():
    """ApplicationConfig 테스트"""
    print("Testing ApplicationConfig...")

    config = ApplicationConfig()

    # 기본 값 테스트
    assert config.get_speed() == config.default_speed
    assert config.get_total_pages() == 1

    # 속도 설정 테스트
    assert config.set_speed(2.5) == True
    assert config.get_speed() == 2.5

    # 잘못된 속도 값 테스트
    assert config.set_speed(-1) == False
    assert config.set_speed(10) == False

    # 페이지 수 설정 테스트
    assert config.set_total_pages(100) == True
    assert config.get_total_pages() == 100

    # 잘못된 페이지 수 테스트
    assert config.set_total_pages(-5) == False
    assert config.set_total_pages(0) == False

    # PDF 파일명 설정 테스트
    assert config.set_pdf_filename("test.pdf") == True
    assert config.get_pdf_filename() == "test.pdf"

    # 잘못된 파일명 테스트
    assert config.set_pdf_filename("") == False
    assert config.set_pdf_filename(None) == False

    # 리셋 테스트
    config.reset()
    assert config.get_speed() == config.default_speed
    assert config.get_total_pages() == 1
    assert config.get_pdf_filename() == "output.pdf"

    print("ApplicationConfig tests passed!")


def test_screen_capture_manager():
    """ScreenCaptureManager 테스트"""
    print("Testing ScreenCaptureManager...")

    scm = ScreenCaptureManager()

    # 속도 설정 테스트
    scm.set_speed(1.0)
    assert scm.speed == 1.0

    # 랜덤 속도 생성 테스트
    random_speed = scm._generate_random_speed(1.0, 50)
    assert 0.5 <= random_speed <= 1.5

    # 리셋 테스트
    scm.reset()
    assert scm.current_page == 1

    print("ScreenCaptureManager tests passed!")


def main():
    """메인 테스트 함수"""
    print("Starting component tests...\n")

    try:
        test_coordinate_manager()
        print()

        test_application_config()
        print()

        test_screen_capture_manager()
        print()

        print("All tests passed successfully!")

    except Exception as e:
        print(f"Test failed with error: {e}")
        raise e


if __name__ == "__main__":
    main()