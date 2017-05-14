import pyaudio
import numpy

FRAME_SIZE = 2048
RATE = 44100

stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                channels=1,
                                rate=RATE,
                                input=True,
                                frames_per_buffer=FRAME_SIZE)

while stream:
    data = numpy.fromstring(stream.read(FRAME_SIZE), dtype=numpy.int16)
    peak = numpy.average(numpy.abs(data)) * 2
    bars = ">"*int(50*peak/2**11)
    print(peak, bars)
