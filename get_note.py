# Функція перетворює частоту на назву ноти.
# Та додає до відображення стрілочки - напрям при настройці.

import numpy
from audio_freq import audio_freq


def get_note():
    current_note = audio_freq()

    # Список всіх значень частоти для нот 0-127

    std_tune = 440  # Стандартна настройка для ноти A4.
    notes_frequencies = []

    for midi in range(0, 127):
        freq = (std_tune / 32) * (2 ** ((midi - 9) / 12))
        notes_frequencies.append(freq)

    # Пошук найближчих нот для виміряної частоти.

    for item in notes_frequencies:
        if item <= current_note:
            continue
        else:
            next_note = item
            break

    previous_note = notes_frequencies[notes_frequencies.index(next_note) - 1]

    # Визначення найближчої до виміряної частоти ноти.

    if next_note - current_note > current_note - previous_note:
        nearest_note = previous_note
    else:
        nearest_note = next_note

    # Визначення імені ноти та октави.

    def freq_to_note():
        notes_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        note = notes_list[notes_frequencies.index(nearest_note) % 12]
        octave = notes_frequencies.index(nearest_note) // 12 - 1
        if len(str(note)+str(octave)) < 3:
            return str(note) + str(octave) + ' '
        else:
            return str(note)+str(octave)

    note_name = freq_to_note()

    # Покажчик найтройки.

    def add_arrows():
        half_note = (next_note - previous_note) / 2
        arrow_entry = half_note / 3
        notes_difference = numpy.absolute(current_note - nearest_note)
        if notes_difference <= arrow_entry / 3:
            arrows = '   '
        elif notes_difference <= arrow_entry:
            arrows = '  >'
        elif notes_difference <= arrow_entry * 2:
            arrows = ' >>'
        else:
            arrows = '>>>'

        if current_note - nearest_note < 0:
            return arrows
        else:
            arrows = arrows[::-1]
            return arrows.replace('>', '<')

    if current_note - nearest_note < 0:
        full_note_view = add_arrows() + note_name + '   '
    else:
        full_note_view = '   ' + note_name + add_arrows()

    return full_note_view
