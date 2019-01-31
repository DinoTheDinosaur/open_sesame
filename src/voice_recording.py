import pyaudio
import wave

def voice_rec(path_to_wav):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    RECORD_SECONDS = 3.8
    WAVE_OUTPUT_FILENAME = path_to_wav + ".wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    print(f"recording {path_to_wav}")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print(f"done recording {path_to_wav}!")
    stream.stop_stream()
    stream.close()
    wavfile=wave.open(WAVE_OUTPUT_FILENAME,'wb')
    wavfile.setnchannels(CHANNELS)
    wavfile.setsampwidth(p.get_sample_size(FORMAT))
    wavfile.setframerate(RATE)
    wavfile.writeframes(b''.join(frames))
    wavfile.close()

path = input()
voice_rec(path)
