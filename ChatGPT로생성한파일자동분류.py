import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\student\Downloads'

# 각 파일 타입에 대한 대상 폴더 경로
destination_folders = {
    'images': r'C:\Users\student\Downloads\images',
    'data': r'C:\Users\student\Downloads\data',
    'docs': r'C:\Users\student\Downloads\docs',
    'archive': r'C:\Users\student\Downloads\archive'
}

# 파일 확장자별로 이동할 폴더 매핑
file_types = {
    'images': ['.jpg', '.jpeg'],
    'data': ['.csv', '.xlsx'],
    'docs': ['.txt', '.doc', '.pdf'],
    'archive': ['.zip']
}

# 폴더가 없으면 생성
for folder in destination_folders.values():
    if not os.path.exists(folder):
        os.makedirs(folder)

# 파일 이동 함수
def move_files_by_extension(download_folder, destination_folders, file_types):
    # 다운로드 폴더에서 파일들을 확인
    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)
        
        # 파일만 처리 (폴더 제외)
        if os.path.isfile(file_path):
            # 파일 확장자 추출
            _, file_extension = os.path.splitext(filename)

            # 각 확장자에 맞는 대상 폴더로 이동
            for folder, extensions in file_types.items():
                if file_extension.lower() in extensions:
                    destination_folder = destination_folders[folder]
                    shutil.move(file_path, os.path.join(destination_folder, filename))
                    print(f'Moved: {filename} -> {destination_folder}')
                    break

# 파일 이동 실행
move_files_by_extension(download_folder, destination_folders, file_types)
