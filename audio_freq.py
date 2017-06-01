# Функція відкриває аудіо потік та вимірює його частоту.
# Повертає значення частоти поки потік відкритий.

from pyaudio import PyAudio, paInt16
import numpy
from get_note import get_note


def audio_freq():
    note_min = 60   # Нота До 4-ї октави
    note_max = 71   # Нота Сі 4-ї октави
    sample_freq = 22050
    frame_size = 2048
    frames_per_fft = 16

    samples_per_fft = frame_size * frames_per_fft
    freq_step = sample_freq / samples_per_fft

    def note_to_fftbin(n):
        return 440 * 2.0 ** ((n - 69) / 12.0) / freq_step

    imin = max(0, int(numpy.floor(note_to_fftbin(note_min - 1))))
    imax = min(samples_per_fft, int(numpy.ceil(note_to_fftbin(note_max + 1))))

    buf = numpy.zeros(samples_per_fft, dtype=numpy.float32)

    window = 0.5 * (1 - numpy.cos(numpy.linspace(0, 2*numpy.pi, samples_per_fft, False)))

    # Відкриваємо аудіо потік.

    stream = PyAudio().open(format=paInt16,
                            channels=1,
                            rate=sample_freq,
                            input=True,
                            frames_per_buffer=frame_size)

    stream.start_stream()

    # Поки потік відкритий йде запис у файл.

    while stream.is_active():

        buf[:-frame_size] = buf[frame_size:]
        buf[-frame_size:] = numpy.fromstring(stream.read(frame_size), numpy.int16)

        fft = numpy.fft.rfft(buf * window)

        freq = (numpy.abs(fft[imin:imax]).argmax() + imin) * freq_step  # Значення частоти.

        freq_save(get_note(freq))   # Запис відображення ноти (get_note) у файл freqs.txt

    # Правильно закриваємо аудіо потік.

    stream.stop_stream()
    stream.close()
    stream.terminate()


# Функція для запису значень у файл freqs.txt
# freqs.txt кожного разу оновлюється або створюється новий, якщо його не було створено.

def freq_save(note):
    freq_file = open('freqs.txt', 'w')
    freq_file.write(note)
    freq_file.close()

if __name__ == '__main__':
    audio_freq()    # Файл має оновлюватись, функція не зупиняється.
