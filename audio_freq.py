# Робота з аудіо потоком та повернення значення, готового для відображення ноти у вікні тюнера.

import numpy
from pyaudio import PyAudio, paInt16

from get_note import get_note


# Функція для запису значень у файл freqs.txt
# freqs.txt кожного разу оновлюється або створюється новий, якщо його не було створено.

def freq_save(note):
    freq_file = open('freqs.txt', 'w')
    freq_file.write(note)
    freq_file.close()


# Функція відкриває аудіо потік та вимірює його частоту.
# Виміряна частота перетворюється на ноту та покажчик настройки, що і записується у файл.

def audio_freq():

    # Значення крайніх нот у моєму випадку (шестиструнна гітара в строї Ре)

    note_min = 60           # Нота До 4-ї октави
    note_max = 71           # Нота Сі 4-ї октави

    sample_freq = 22050     # Частота кадру в герцах

    # Від збільшення цих констант залежить швидкість оновлення частоти.

    frame_size = 2048       # Кількість зразків у кадрі
    frames_per_fft = 16     # Кількість кадрів для середнього значення ШПФ

    samples_per_fft = frame_size * frames_per_fft   # Кількість зразків на ШПФ
    freq_step = sample_freq / samples_per_fft       # Крок частоти

    # Отримання мінімального та максимального показника для наших нот в межах ШПФ.

    def note_to_fftbin(n):
        return 440 * 2.0 ** ((n - 69) / 12.0) / freq_step

    imin = max(0, int(numpy.floor(note_to_fftbin(note_min - 1))))
    imax = min(samples_per_fft, int(numpy.ceil(note_to_fftbin(note_max + 1))))

    # Визначення простору для ШПФ.

    buf = numpy.zeros(samples_per_fft, dtype=numpy.float32)

    # Функція вікна Хеннінга.

    window = 0.5 * (1 - numpy.cos(numpy.linspace(0, 2*numpy.pi, samples_per_fft, False)))

    # Відкриваємо аудіо потік.

    stream = PyAudio().open(format=paInt16,
                            channels=1,
                            rate=sample_freq,
                            input=True,
                            frames_per_buffer=frame_size)

    stream.start_stream()

    # Отримуємо дані, поки потік відкритий.

    while stream.is_active():

        # Оновлюємо буфер та приймаємо нові дані.

        buf[:-frame_size] = buf[frame_size:]
        buf[-frame_size:] = numpy.fromstring(stream.read(frame_size), numpy.int16)

        # Запускаємо ШПФ в буфері в межах вікна.

        fft = numpy.fft.rfft(buf * window)

        # Отримуємо максимально повторювану частоту в діапазоні.

        freq = (numpy.abs(fft[imin:imax]).argmax() + imin) * freq_step

        # Запис відображення ноти (get_note) у файл freqs.txt

        freq_save(get_note(freq))

    # Правильно закриваємо аудіо потік.

    stream.stop_stream()
    stream.close()
    stream.terminate()


if __name__ == '__main__':
    audio_freq()    # Файл має оновлюватись, функція не зупиняється.
