import os
try:
    from PIL import Image
except ImportError:
    import Image
import shutil


class PDFGenerator:
    """이미지 파일들을 PDF로 변환하는 클래스"""

    def __init__(self):
        self.image_list = []

    def _get_sorted_image_files(self, directory):
        """디렉토리에서 이미지 파일들을 정렬하여 반환"""
        # 이미지 파일 리스트
        file_list = os.listdir(directory)

        # 숫자 순서대로 정렬 (natsort 대신 간단한 구현)
        numbered_files = []
        for filename in file_list:
            if filename.endswith('.png') and filename.startswith('img_'):
                try:
                    # img_0001.png 형식에서 숫자 추출
                    num = int(filename.split('_')[1].split('.')[0])
                    numbered_files.append((num, filename))
                except:
                    pass

        # 숫자 순서대로 정렬
        numbered_files.sort(key=lambda x: x[0])
        return [filename for num, filename in numbered_files]

    def convert_images_to_pdf(self, image_directory, output_filename):
        """이미지 파일들을 PDF로 변환"""
        try:
            # 디렉토리에서 이미지 파일들 가져오기
            file_list = self._get_sorted_image_files(image_directory)

            if not file_list:
                raise Exception("이미지 파일을 찾을 수 없습니다.")

            # 이미지 리스트 초기화
            self.image_list = []

            # 첫 페이지 이미지 로드
            first_image_path = os.path.join(image_directory, file_list[0])
            first_image = Image.open(first_image_path)
            first_image_rgb = first_image.convert('RGB')

            # 나머지 이미지들 로드
            for filename in file_list[1:]:
                image_path = os.path.join(image_directory, filename)
                image = Image.open(image_path)
                image_rgb = image.convert('RGB')
                self.image_list.append(image_rgb)

            # PDF로 저장
            if not output_filename.endswith('.pdf'):
                output_filename += '.pdf'

            first_image_rgb.save(output_filename, save_all=True, append_images=self.image_list)
            print(f"PDF 변환 완료: {output_filename}")

            return True

        except Exception as e:
            print(f'PDF 변환 중 오류 발생: {e}')
            raise e

    def cleanup_image_directory(self, directory):
        """이미지 디렉토리 정리"""
        try:
            if os.path.exists(directory):
                shutil.rmtree(directory)
                print(f"{directory} 디렉토리 정리 완료")
        except Exception as e:
            print(f'디렉토리 정리 중 오류 발생: {e}')
            raise e

    def reset(self):
        """상태 초기화"""
        self.image_list = []