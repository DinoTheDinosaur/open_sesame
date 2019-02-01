import pyaudio
import wave
import os
from scipy.io import wavfile as wav
from scipy import signal
from python_speech_features import mfcc

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
    print(f"recording...")
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
# record_len = int(input())
# print(voice_rec(record_len).shape)