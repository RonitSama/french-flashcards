__author__ = "Ronit Samanta"

from tkinter import Tk, Canvas, PhotoImage, Button
import random
from words import words

BACKGROUND_COLOR = "#B1DDC6"

timer = 'after#0'
current_word: dict[str, str]
canvas: Canvas
window: Tk
front_img: PhotoImage
back_img: PhotoImage
wrong_img: PhotoImage
right_img: PhotoImage


def new_word():
    global timer, current_word
    window.after_cancel(timer)

    if words:
        subjects = ['je', 'tu', 'il/elle', 'nous', 'vous', 'ils/elles']
        temp_word: str = random.choice(list(words.keys()))
        temp_conj: str = random.choice(subjects)
        current_word = {'Infinitive': f'{temp_word}, {temp_conj}', 'Conjugated': words[temp_word][temp_conj]}
        del words[temp_word]
    else:
        canvas.itemconfig(2, text='', fill='black')
        canvas.itemconfig(3, text='All done!', fill='black')
        canvas.itemconfig(1, image=front_img)
        return

    canvas.itemconfig(1, image=front_img)
    canvas.itemconfig(2, text='Infinitive', fill='black')
    canvas.itemconfig(3, text=current_word['Infinitive'], fill='black')

    timer = window.after(6000, flip_card)


def flip_card():
    canvas.itemconfig(1, image=back_img)
    canvas.itemconfig(2, text='Conjugated', fill='white')
    canvas.itemconfig(3, text=current_word['Conjugated'], fill='white')


def main():
    global canvas, window, front_img, back_img, wrong_img, right_img

    # window
    window = Tk()
    window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
    window.title('French Flashcards')

    # images
    front_img = PhotoImage(file='../images/card_front.png')
    back_img = PhotoImage(file='../images/card_back.png')
    wrong_img = PhotoImage(file='../images/wrong.png')
    right_img = PhotoImage(file='../images/right.png')

    # canvas
    canvas = Canvas(height=526, width=800,
                    bg=BACKGROUND_COLOR, highlightthickness=0)

    # flashcards
    canvas.create_image(400, 263, image=front_img)
    canvas.create_text(400, 150, text='French',
                    font=('Arial', 40, 'italic'), fill='black')
    canvas.create_text(400, 300,
                    font=('Arial', 60, 'bold'), fill='black', width=600)
    canvas.grid(row=0, column=0, columnspan=2)

    # buttons
    wrong_button = Button(image=wrong_img, highlightthickness=0,
                        borderwidth=0, command=new_word)
    wrong_button.grid(row=1, column=0)
    right_button = Button(image=right_img, highlightthickness=0,
                        borderwidth=0, command=new_word)
    right_button.grid(row=1, column=1)

    new_word()

    window.mainloop()

if __name__ == '__main__':
    main()
