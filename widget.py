# Гарне вікно з не менш гарним шрифтом.
# Шрифт Digital-7 Mono.

import tkinter
from get_note import get_note


def widget():

    # Те, що стосується вікна.

    window = tkinter.Tk()
    window.title('Audio frequency - PyTune')
    window.geometry('357x79+200+200')
    window.resizable(False, False)

    # Оновлює екран, беручи нові показники частоти.

    def refresh():
        lcd.after(150, refresh)
        lcd['text'] = get_note()

    # Те, що стосується вмісту вікна.

    lcd = tkinter.Label(window, font=('Digital-7 Mono', 64), bg='black', fg='red')

    lcd.after_idle(refresh)
    lcd.place(anchor="nw")

    window.mainloop()
