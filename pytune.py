# Просто файл для запуску програми.

import threading
from audio_freq import audio_freq
from widget import widget

# audio_freq() запускається в потоці щоб файл freqs.txt постійно оновлювався.

audio_freq_thrd = threading.Thread(target=audio_freq)
audio_freq_thrd.daemon = True
audio_freq_thrd.start()

widget()
