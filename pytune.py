# Просто файл для запуску програми.

from threading import Thread
from audio_freq import audio_freq
from widget import widget

# audio_freq() запускається в потоці щоб файл freqs.txt постійно оновлювався.

audio_freq_thrd = Thread(target=audio_freq)
audio_freq_thrd.daemon = True
audio_freq_thrd.start()

widget()
