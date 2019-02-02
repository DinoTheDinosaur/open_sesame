import pyaudio
import wave
import os
from faker import Faker
from scipy.io import wavfile as wav
from scipy import signal
from python_speech_features import mfcc
from time import sleep

def voice_rec(record_len):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    RECORD_SECONDS = record_len
    WAVE_OUTPUT_FILENAME = "test.wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Please read the following text aloud:")

    #change to 'en_EN' to get English sample
    fake = Faker('ru_RU')

    print()
    print(fake.text())
    print(fake.text())
    print(fake.text())
    print(fake.text())
    print()

    sleep(1.5)
    print(f"recording")

    sleep(3)

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print(f"done recording!")
    stream.stop_stream()
    stream.close()
    wavfile=wave.open(WAVE_OUTPUT_FILENAME,'wb')
    wavfile.setnchannels(CHANNELS)
    wavfile.setsampwidth(p.get_sample_size(FORMAT))
    wavfile.setframerate(RATE)
    wavfile.writeframes(b''.join(frames))
    sampling_frequency, signal_data = wav.read("test.wav")
    wavfile.close()
    os.remove("test.wav")
    return mfcc(signal_data, sampling_frequency)