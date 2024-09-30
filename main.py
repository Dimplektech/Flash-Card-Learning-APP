from distutils.command.config import config
from tkinter import *
import pandas
import random


from pandas.core.interchange.dataframe_protocol import DataFrame
from pandas.core.methods.to_dict import to_dict
flip_timer=""
BACKGROUND_COLOR = "#B1DDC6"

# Read CSV
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data= pandas.read_csv("data/french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")
current_card ={}

# Next French word
def next_card():
    global flip_timer,current_card
    #window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    french_word= current_card["French"]
    english_word = current_card["English"]
    canvas.itemconfig(flash_card, image=card_front)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=french_word,fill="black")
    flip_timer = window.after(3000,flip_card,english_word)


# Translate Function
def flip_card(english_word):

    canvas.itemconfig(flash_card,image=card_back)
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=english_word,fill="white")

def remove_word(): ##remove known words
    data_dict.remove((current_card))
    print(len(data_dict))
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv",index=False)
    #
    next_card()



window= Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
#window.minsize(height=100,width=1000)
card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(height=526,width=800)
flash_card = canvas.create_image(400,250,image=card_front)
canvas.grid(row=0,column=0, columnspan=2)
canvas.config(bg =BACKGROUND_COLOR,highlightthickness=0)


# Text on the Canvas

card_title = canvas.create_text(400,150,font="Arial 40 italic",text="French")
card_word = canvas.create_text(400, 263, font="Arial 60 bold", text="Word")
#canvas.create_text(400,263,font="Arial 60 bold",text="trouve")


# Buttons
cross_image = PhotoImage(file="images/wrong.png")
card_back = PhotoImage(file="images/card_back.png")
cross_button = Button(image=cross_image,highlightthickness=0,command=next_card)
cross_button.grid(row=1,column=0)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,highlightthickness=0,command=remove_word)
right_button.grid(row=1,column=1)

next_card()




window.mainloop()