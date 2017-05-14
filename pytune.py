import numpy
import pyaudio

NOTE_MIN = 38   #D2
NOTE_MAX = 62   #D4
FSAMP = 22050
FRAME_SIZE = 2048
FRAMES_PER_FFT = 16

SAMPLES_PER_FFT = FRAME_SIZE * FRAMES_PER_FFT
FREQ_STEP = FSAMP / SAMPLES_PER_FFT


def note_to_fftbin(n):
    return 440 * 2.0 ** ((n - 69) / 12.0) / FREQ_STEP

imin = max(0, int(numpy.floor(note_to_fftbin(NOTE_MIN-1))))
imax = min(SAMPLES_PER_FFT, int(numpy.ceil(note_to_fftbin(NOTE_MAX+1))))

buf = numpy.zeros(SAMPLES_PER_FFT, dtype=numpy.float32)
window = 0.5 * (1 - numpy.cos(numpy.linspace(0, 2*numpy.pi, SAMPLES_PER_FFT, False)))

stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                channels=1,
                                rate=FSAMP,
                                input=True,
                                frames_per_buffer=FRAME_SIZE)

while stream:

    buf[:-FRAME_SIZE] = buf[FRAME_SIZE:]
    buf[-FRAME_SIZE:] = numpy.fromstring(stream.read(FRAME_SIZE), numpy.int16)

    fft = numpy.fft.rfft(buf * window)

    freq = (numpy.abs(fft[imin:imax]).argmax() + imin) * FREQ_STEP

    print('Frequency:', freq, 'Hz')
