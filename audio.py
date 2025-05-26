import pyaudio
import numpy as np

# Audio parameters
CHUNK = 1024  # Number of frames per buffer
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1  # Mono audio
RATE = 44100  # Sample rate

# Initialize PyAudio
p = pyaudio.PyAudio()

# Analysis function (example: calculate RMS)
def analyze_audio(data):
    audio_data = np.frombuffer(data, dtype=np.int16)
    rms = np.sqrt(np.mean(audio_data**2))
    print(f"RMS: {rms}")

# Callback function
def audio_callback(in_data, frame_count, time_info, status):
    analyze_audio(in_data)  # Analyze the received audio data
    return (in_data, pyaudio.paContinue)

# Open audio stream in callback mode
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                stream_callback=audio_callback,
                frames_per_buffer=CHUNK)

print("Recording and analyzing...")

stream.start_stream()

# Keep the stream active for a desired duration or until a condition is met
try:
    while stream.is_active():
        pass
except KeyboardInterrupt:
    pass

print("Stopping...")

stream.stop_stream()
stream.close()
p.terminate()