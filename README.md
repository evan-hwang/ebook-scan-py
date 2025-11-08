# eBook Scan

eBook Scan은 전자책을 PDF로 변환하기 위한 파이썬 기반의 GUI 애플리케이션입니다. 화면의 특정 영역을 캡처하여 페이지별로 저장하고, 이를 하나의 PDF 파일로 병합할 수 있습니다.

## 기능

- GUI 기반의 직관적인 인터페이스
- 화면 특정 영역 캡처
- 자동 페이지 넘김 및 캡처
- 캡처된 이미지를 PDF로 변환
- 캡처 속도 조절 기능

## 설치 방법

### 필수 요구사항

- Python 3.9 이상
- pip 패키지 관리자

### 설치 절차

1. 저장소 클론:
   ```bash
   git clone https://github.com/yourusername/ebook-scan-py.git
   cd ebook-scan-py
   ```

2. 가상 환경 생성 (선택사항):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # 또는
   venv\Scripts\activate  # Windows
   ```

3. 의존성 설치:
   ```bash
   pip install -r requirements.txt
   ```

4. 애플리케이션 실행:
   ```bash
   python -m ebook_scan
   ```

   또는

   ```bash
   ebook-scan
   ```

## 사용법

1. 애플리케이션 실행 후, eBook의 좌측상단과 우측하단 좌표를 설정합니다.
2. 총 페이지 수와 생성할 PDF 파일명을 입력합니다.
3. "PDF로 만들기" 버튼을 클릭하면 캡처 및 변환 작업이 시작됩니다.

## 프로젝트 구조

```
ebook-scan-py/
├── src/
│   └── ebook_scan/
│       ├── __init__.py
│       ├── __main__.py
│       ├── main.py
│       ├── config/
│       │   ├── __init__.py
│       │   └── app_config.py
│       ├── gui/
│       │   ├── __init__.py
│       │   └── main_window.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── coordinate_manager.py
│       │   ├── screen_capture_manager.py
│       │   └── pdf_generator.py
│       └── utils/
│           ├── __init__.py
│           └── helpers.py
├── tests/
├── docs/
├── scripts/
├── requirements.txt
├── requirements-dev.txt
├── setup.py
├── pyproject.toml
├── README.md
├── .gitignore
└── .pre-commit-config.yaml
```

## 개발

### 개발 환경 설정

개발을 위해 추가적인 의존성을 설치하려면 다음 명령을 실행하세요:

```bash
pip install -r requirements-dev.txt
```

### 테스트 실행

프로젝트 루트 디렉토리에서 다음 명령을 실행하여 테스트를 수행할 수 있습니다:

```bash
python -m pytest tests/
```

또는

```bash
python tests/test_ebook_scan.py
```

### 코드 포맷팅

코드를 일관된 스타일로 유지하기 위해 black과 isort를 사용합니다:

```bash
black .
isort .
```

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 기여

버그 리포트, 기능 요청, 풀 리퀘스트를 환영합니다. 기여하려면 다음 단계를 따르세요:

1. 저장소를 포크합니다.
2. 기능 브랜치를 생성합니다 (`git checkout -b feature/AmazingFeature`).
3. 변경 사항을 커밋합니다 (`git commit -m 'Add some AmazingFeature'`).
4. 브랜치에 푸시합니다 (`git push origin feature/AmazingFeature`).
5. 풀 리퀘스트를 오픈합니다.

## 연락처

프로젝트 링크: [https://github.com/yourusername/ebook-scan-py](https://github.com/yourusername/ebook-scan-py)