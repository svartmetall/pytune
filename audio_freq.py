# Функція відкриває аудіо потік та вимірює його частоту.
# Повертає значення частоти поки потік відкритий.

import numpy
import pyaudio


def audio_freq():
    note_min = 38   # D2 (перша струна на гітарі в строї Ре)
    note_max = 62   # D4 (шоста струна на гітарі в строї Ре)
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

    # Ініціалізація аудіо.

    stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                    channels=1,
                                    rate=sample_freq,
                                    input=True,
                                    frames_per_buffer=frame_size)

    buf[:-frame_size] = buf[frame_size:]
    buf[-frame_size:] = numpy.fromstring(stream.read(frame_size), numpy.int16)

    fft = numpy.fft.rfft(buf * window)

    freq = (numpy.abs(fft[imin:imax]).argmax() + imin) * freq_step

    return freq
