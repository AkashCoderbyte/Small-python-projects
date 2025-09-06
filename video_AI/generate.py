import os 
from text_to_audio import text_to_speech_file
import subprocess

def text_to_audio(folder):
    with open(f"user_uploads/{folder}/des.txt") as f:
        text = f.read()
    text_to_speech_file(text, folder)
   

# def create_video(folder):
#     command = f'''
#                 ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920: force_original_aspect_ratio=decrease, pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v
#                 libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels{folder}.mp4
#                 '''
#     subprocess.run(command, shell=True,check=True)
def create_video(folder):
    command = f'''
ffmpeg -f concat -safe 0 -i user_uploads/75464b53-88e8-11f0-ba78-3ef35a027725/input.txt -i user_uploads/75464b53-88e8-11f0-ba78-3ef35a027725/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p reel.mp4
'''
    subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    
if __name__ == "__main__":
    while True:
        with open("done.txt","r") as f:
            done_folder = f.readlines()

        done_folder =[f.strip() for f in done_folder]
        folders = os.listdir("user_uploads")
        for folder in folders:
                if (folder not in done_folder):
                    text_to_audio(folder)
                    create_video(folder)
                    with open("done.txt","a") as f:
                        f.write(folder+"\n")