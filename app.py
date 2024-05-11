import sounddevice as sd
import numpy as np
import subprocess
import webbrowser
import random
import time

# Constants
sound_threshold = 0.1
duration_threshold = 0.1
sample_rate = 44100
duration = 2

lofi_links = [
    'https://www.youtube.com/live/oBwrlePfchs?si=kOm0QaXGQTFsLgIL',
    'https://youtu.be/rtTI1rh9U5M?si=2a86LO8c-4lXdJKN',
    'https://youtu.be/EVF_AuhJgLg?si=_TibxzBQWaiWc30U'
]
def detect_finger_snap():
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()
    rms = np.sqrt(np.mean(np.square(recording)))
    if rms > sound_threshold:
        return True
    else:
        return False


def open_applications():
    webbrowser.open_new_tab('https://www.youtube.com')
    time.sleep(2)
    search_query = 'lofi hip hop beats to relax/study to'
    webbrowser.open_new_tab(f'https://www.youtube.com/results?search_query={search_query}')
    time.sleep(2)
    random_link = random.choice(lofi_links)
    webbrowser.open_new_tab(random_link)
    subprocess.Popen(['open', '-a', 'Visual Studio Code'])
    subprocess.Popen(['open', '-a', 'Spotify'])

# Main function
if __name__ == "__main__":
    print("Listening for two consecutive finger snaps...")
    snap_count = 0
    while True:
        if detect_finger_snap():
            snap_count += 1
            print(f"Finger snap {snap_count} detected!")
            if snap_count >= 2:
                print("Two consecutive finger snaps detected! Setting up workspace...")
                open_applications()
                break
        else:
            snap_count = 0