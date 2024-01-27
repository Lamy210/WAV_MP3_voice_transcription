import wave
import struct
import numpy as np
import os
import math
import speech_recognition as sr
import pandas as pd
import tkinter.filedialog
import pydub

recognizer = sr.Recognizer()
'''

def wav_to_text(wav_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)

    
    ## Mozilla Common Voice のエンジンを取得
    ##engine = sr.AudioFile.get_engine("mozilla-common-voice")

    # 音声認識
    transcription = recognizer.recognize_sphinx(audio_data, language='js-JP')

    return transcription

'''
def cut_wav(input_filename, cut_interval):
    if input_filename.endswith(".mp3"):  # MP3ファイルの場合
        sound = pydub.AudioSegment.from_mp3(input_filename)  # MP3読み込み
        wave_filename = input_filename[:-4] + ".wav"  # WAVファイル名作成
        sound.export(wave_filename, format="wav")  # WAVに変換
        wav_file = wave_filename  # WAVファイル名を設定
    else:
        wav_file = input_filename

    wave_reader = wave.open(wav_file, 'r')

    # 全文を取得する
    transcription = ""

    while True:
        audio_data = wave_reader.readframes(wave_reader.getnframes())
        if len(audio_data) == 0:
            break

   # 音声データの長さをチェックする
        audio_length = len(audio_data) / wave_reader.getframerate()

        # 長さが短い場合は、適切な長さに拡張する
        if audio_length < cut_interval:
            audio_data = np.pad(audio_data, (0, int(cut_interval * wave_reader.getframerate() - audio_length)), 'constant')

        audio_data = sr.AudioData(audio_data, 
                              sample_rate=wave_reader.getframerate(), 
                              sample_width=4) 

        transcription += recognizer.recognize_sphinx(audio_data, language='en-US/')
        print(transcription)

output_directory = "output"
directory_exists = os.path.exists(output_directory)

if directory_exists == False:
    os.mkdir(output_directory)

file_types = [("music", "*.wav;*.mp3;")]  # 拡張子を追加
initial_directory = os.path.abspath(os.path.dirname(__file__))
input_filename = tkinter.filedialog.askopenfilename(filetypes=file_types, initialdir=initial_directory)

cut_interval = 10
transcription = cut_wav(input_filename, float(cut_interval))
print(transcription)
# txt出力
#with open(os.path.join(output_directory, input_filename[:-4] + ".txt"), "w") as f:
    #f.write(transcription)
