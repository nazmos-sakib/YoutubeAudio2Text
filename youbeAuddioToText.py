
import os
from pytube import YouTube
import whisper

def create_and_open_text(txt,fileName):
    with open(fileName,"w") as file:
        file.write(txt)
    #os.startfile(fileName)


url = input("Enter youtube url: ")

yt = YouTube(url)
outputPath = "./youtubeAudio"
fileName = "audio.mp3"
#audioStream = yt.streams.filter(only_audio=True).first()
yt.streams.get_audio_only().download(output_path=outputPath,filename=fileName)


#audioStream().download(output_path=outputPath,filename=fileName)
print(f"Audio downloaded to {outputPath}/{fileName}")

model = whisper.load_model("base")
result = model.transcribe("./youtubeAudio/audio.mp3")

print(result["text"])

create_and_open_text(result["text"],"./youtubeAudio/outpu.txt")