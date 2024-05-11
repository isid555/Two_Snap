import sounddevice as sd
import numpy as np
import subprocess
import webbrowser
import random
import time


sound_threshold = 0.1
duration_threshold = 0.1
sample_rate = 44100
duration = 2

lofi_links = [
    'https://youtu.be/Lng9YbFNoxE?list=RDLng9YbFNoxE&t=188',
    'https://youtu.be/zLcrEO-eIOQ?list=RDLng9YbFNoxE&t=196',
    'https://youtu.be/_AGlvdNlS_0?t=14'
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
    search_query = 'ragangal+16+song+'
    webbrowser.open_new_tab(f'https://www.youtube.com/results?search_query={search_query}')
    time.sleep(2)
    random_link = random.choice(lofi_links)
    webbrowser.open_new_tab(random_link)
    subprocess.Popen(['open', '-a', 'Visual Studio Code'])
    subprocess.Popen(['open', '-a', 'Spotify'])


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
