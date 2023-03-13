import random
from tkinter import *


word_list = [
    "zealous", "didactic", "return", "weave", "wide", "outrageous", "miniature", "ring", "bells", "pull", "buy",
    "fling", "permissible", "poison", "google", "excited", "insect", "grandiose", "convince", "leak", "valuable",
    "fine", "fantastic", "believe", "ugliest", "vengeful", "attention", "land", "opt", "truculent", "value", "spotted",
    "seemly", "rattle", "title", "committee", "high-pitched", "tightfisted", "light", "race", "jolly", "pain", "placid",
    "cuddly", "average", "low", "sun", "spiteful", "red", "nondescript", "icy", "amusing", "kindly", "burst", "gray",
    "lethal", "crown", "grey", "useful", "puzzled", "faucet", "ply", "roll", "lead", "elbow", "undesirable", "choose",
    "hook", "lade", "cuddly", "embarrassed", "throne", "lame", "marked", "limp", "record", "penitent", "disease",
    "produce", "basketball", "afterthought", "scowl", "locket", "meat", "rabbits", "insurance", "potato", "price",
    "point", "school", "wary", "ultra", "violet", "nip", "wet", "majestic", "scrub", "penitent", "fast", "night "
]

test_list = []
timer = None


# Functions

def typing_test():
    # Word selection
    count_down(60)
    for i in range(1, 50):
        rand_word = word_list[random.randint(0, 99)]
        test_list.append(rand_word)
    words_prnt = " ".join(test_list)
    words.config(text=words_prnt, wraplength=300, justify="center")


def count_down(count_sec):
    global timer
    if count_sec > 0:
        timer = window.after(1000, count_down, count_sec - 1)

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    timer_text.config(text=f"{count_sec}")
    if count_sec == "00":
        typed_words = (type_input.get()).split()
        collect_words(typed_words)



def collect_words(typed_words):
    wordspm = 0
    worderrors = 0
    for i in typed_words:
        if i in test_list:
            wordspm += 1
        else:
            worderrors +=1
    word_count.config(text=f"{wordspm} words per minute. You made {worderrors} errors")






# Window settings

window = Tk()
window.title("Typing speed tester")
window.config(width=1000, height=500, padx=50, pady=50)

# Words Label

words = Label(text="Click on the start timer button to display the text")
words.grid(column=1, row=0, columnspan=2)
# Entry Box for input

type_input = Entry()
type_input.focus_set()
type_input.grid(column=1, row=1)

# Button to start the timer

start = Button(text="Start Timer", command=typing_test)
start.grid(column=0, row=2)

# Word count

word_count = Label(text="0")
word_count.grid(column=3, row=2)

# Timer Text

timer_text = Label(text="60")
timer_text.grid(column=3, row=3)

window.mainloop()
