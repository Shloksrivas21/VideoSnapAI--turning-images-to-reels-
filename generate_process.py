# This folder searches for new files inside uploads if the reel is not generated for that
import os
from text_to_speech import text_to_speech_file
import time
import subprocess
def text_to_speech(folder):
    print("TTA- ",folder)
    with open(f"user_uploads/{folder}/desc.txt") as f:
        text=f.read()
    print(text,folder)
    # text_to_speech_file(text,folder)
    

def create_reel(folder):
    comand=f'''ffmpeg -f concat -safe 0 -i "C:/Users/Shlok/OneDrive/Documents/VideoSnapAI/user_uploads/{folder}/input.txt" -i "C:/Users/Shlok/OneDrive/Documents/VideoSnapAI/user_uploads/{folder}/audio.mp3" -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4'''
    subprocess.run(comand,shell=True,check=True)
    # shell will make sure that this comand is running a shell command as a string
    # check will make sure that this command does not throws a non zero error 

if __name__=="__main__":
    while True:
        print("Processing your request...")
        with open("done.txt","r") as m:
            done_folder=m.readlines()
        done_folder=[f.strip() for f in done_folder]
        folders=os.listdir("user_uploads")
        
        for folder in folders:
            if (folder not in done_folder):
                text_to_speech(folder)#Generate the audio.mp3 for desc.text
                create_reel(folder)#Converts the images and the audio.mp3 present inside the folder to reel
                with open("done.txt","a") as f:
                    f.write(folder+"\n")
        time.sleep(4)

