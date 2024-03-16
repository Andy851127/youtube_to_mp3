from pytube import YouTube
from urllib.parse import urlparse, parse_qs
from moviepy.editor import *
import os

def download_video(url,output_path):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    video.download(output_path=output_path)
    
def rename_mp4_to_mp3(output_path):
    files = os.listdir(output_path)

    # 循环处理每个文件
    for file in files:
        # 检查文件是否是以.mp4结尾的
        if file.endswith('.mp4'):
            # 构建新文件名，将.mp4替换为.mp3
            new_name = file.replace('.mp4', '.mp3')
            # 使用os.rename()函数进行重命名
            os.rename(os.path.join(output_path, file), os.path.join(output_path, new_name))

if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    output_path = input("Enter : Your path：")
    download_video(url,output_path)
    rename_mp4_to_mp3(output_path)
    print("Success!")
    input("Press Enter to exit...")

