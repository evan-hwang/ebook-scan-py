"""eBook Scan 애플리케이션의 유틸리티 함수들"""

import os
import time
from typing import Tuple


def validate_directory_path(path: str) -> bool:
    """
    디렉토리 경로의 유효성을 검증합니다.

    Args:
        path (str): 검증할 디렉토리 경로

    Returns:
        bool: 경로가 유효하면 True, 그렇지 않으면 False
    """
    if not path or not isinstance(path, str):
        return False

    try:
        # 경로가 존재하는지 확인
        if not os.path.exists(path):
            # 상위 디렉토리가 존재하는지 확인
            parent_dir = os.path.dirname(path)
            if parent_dir and not os.path.exists(parent_dir):
                return False
        elif not os.path.isdir(path):
            return False

        return True
    except Exception:
        return False


def validate_file_path(path: str) -> bool:
    """
    파일 경로의 유효성을 검증합니다.

    Args:
        path (str): 검증할 파일 경로

    Returns:
        bool: 경로가 유효하면 True, 그렇지 않으면 False
    """
    if not path or not isinstance(path, str):
        return False

    try:
        # 파일이 존재하는 경우
        if os.path.exists(path):
            return os.path.isfile(path)

        # 파일이 존재하지 않는 경우, 상위 디렉토리가 존재하는지 확인
        directory = os.path.dirname(path)
        if directory:
            return validate_directory_path(directory)

        return True
    except Exception:
        return False


def format_time(seconds: float) -> str:
    """
    초 단위 시간을 읽기 쉬운 형식으로 변환합니다.

    Args:
        seconds (float): 초 단위 시간

    Returns:
        str: 형식화된 시간 문자열
    """
    if seconds < 60:
        return f"{seconds:.1f}초"
    elif seconds < 3600:
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return f"{int(minutes)}분 {int(remaining_seconds)}초"
    else:
        hours = seconds // 3600
        remaining_minutes = (seconds % 3600) // 60
        remaining_seconds = seconds % 60
        return f"{int(hours)}시간 {int(remaining_minutes)}분 {int(remaining_seconds)}초"


def get_timestamp() -> str:
    """
    현재 시간을 문자열로 반환합니다.

    Returns:
        str: 현재 시간의 문자열 표현
    """
    return time.strftime("%Y-%m-%d %H:%M:%S")


def sanitize_filename(filename: str) -> str:
    """
    파일명에서 부적절한 문자를 제거합니다.

    Args:
        filename (str): 원본 파일명

    Returns:
        str: 안전한 파일명
    """
    if not filename or not isinstance(filename, str):
        return "unnamed"

    # Windows에서 사용할 수 없는 문자들
    invalid_chars = '<>:"/\\|?*'

    # 부적절한 문자를 언더스코어로 대체
    for char in invalid_chars:
        filename = filename.replace(char, '_')

    # 앞뒤 공백 제거
    filename = filename.strip()

    # 빈 문자열인 경우 기본값 반환
    if not filename:
        return "unnamed"

    return filename


def get_safe_output_path(base_path: str, filename: str, extension: str = ".pdf") -> str:
    """
    안전한 출력 파일 경로를 생성합니다.

    Args:
        base_path (str): 기본 디렉토리 경로
        filename (str): 파일명
        extension (str): 파일 확장자

    Returns:
        str: 안전한 출력 파일 경로
    """
    # 파일명 정리
    safe_filename = sanitize_filename(filename)

    # 확장자 추가
    if not safe_filename.endswith(extension):
        safe_filename += extension

    # 전체 경로 생성
    full_path = os.path.join(base_path, safe_filename)

    # 파일이 이미 존재하는 경우 번호를 붙여서 새로운 이름 생성
    counter = 1
    original_path = full_path
    while os.path.exists(full_path):
        name, ext = os.path.splitext(original_path)
        full_path = f"{name}_{counter}{ext}"
        counter += 1

    return full_path