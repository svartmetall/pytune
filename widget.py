# Гарне вікно з не менш гарним шрифтом.
# Шрифт обраний Digital-7 Mono через однакову ширину всіх символів.
# Зроблено це для того, щоб не змінювався розмір вікна та положення центру надпису.

from tkinter import Tk, Label


# Функція повертає значення з файлу freqs.txt

def open_file():
    freq_file = open('freqs.txt', 'r')
    freq = freq_file.read()
    freq_file.close()
    return freq


# Сама функція вікна.

def widget():

    # Оновлює вміст екрану, беручи нові значення з файлу.

    def refresh():
        lcd.after(300, refresh)
        lcd['text'] = open_file()

    # Те, що стосується вікна.

    window = Tk()
    window.title('Audio frequency - PyTune')
    window.geometry('357x79+200+200')
    window.resizable(False, False)

    # Те, що стосується вмісту вікна.

    lcd = Label(window, font=('Digital-7 Mono', 64), bg='black', fg='red')
    lcd.place(anchor="nw")
    lcd.after_idle(refresh)

    window.mainloop()
