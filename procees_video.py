#convert videos to mp3
import os
import subprocess
files =os.listdir("videos")

for file in files:
    
    tutorial_number=file.split("Tutorial")[1].split(".mp4")[0].split("#")[1]
    
    file_name=file.split(" ｜ ")[0]
    print(tutorial_number,file_name)
    subprocess.run(['ffmpeg', '-i', f'videos/{file}',f'audios/{tutorial_number}_{file_name}.mp3'])
