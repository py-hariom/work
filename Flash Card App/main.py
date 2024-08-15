from tkinter import *
import pandas as pd
import random

current_card = {}  # Empty dictionary to hold current card info
to_learn = []  # List to hold all cards that need to learn

# File paths for main data and result files
main_file = 'data/file.csv'  # Main file with all cards data
known_file = "data/known_words.csv"  # File to save known cards
unknown_file = 'data/unknown_words.csv'  # File to save unknown cards
common_file = 'data/common.csv'  # File to save common cards

# Customize your flash card by adding picture and color here
BACKGROUND_COLOR = "#B1DDC6"  # Background color for window
image1 = "images/card_front.png"
image2 = "images/card_front.png"
image3 = "images/wrong.png"
image4 = "images/right.png"

try:
    data = pd.read_csv(main_file)  # Try reading main data file
    to_learn = data.to_dict(orient="records")  # Convert data to list of dicts
except FileNotFoundError:
    to_learn = []  # If file not found, empty list

# Load known and unknown words
def load_existing_words(filename):
    try:
        df = pd.read_csv(filename)
        return {row['Korean Word']: row for _, row in df.iterrows()}
    except FileNotFoundError:
        return {}

known_words_dict = load_existing_words(known_file)
unknown_words_dict = load_existing_words(unknown_file)

def next_card():
    global current_card, flip_timer  # Access global variables
    window.after_cancel(flip_timer)  # Stop timer if running
    current_card = random.choice(to_learn)  # Pick random card to show
    # Show card info on canvas
    canvas.itemconfig(main_text, text=current_card['Korean Word'], fill="black")
    canvas.itemconfig(main_text2, text='')
    canvas.itemconfig(main_text1, text='')
    canvas.itemconfig(sub_text, text=current_card['Korean Sentence'], fill="black")
    canvas.itemconfig(sub_text1, text=current_card['Hindi Sentence'], fill="black")
    canvas.itemconfig(def_text, text=current_card['Definition'], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)  # Show front image
    flip_timer = window.after(3000, func=flip_card)  # Start timer to flip card

def flip_card():
    # Flip the card and show backside info
    canvas.itemconfig(main_text, text='')
    canvas.itemconfig(main_text2, text=current_card["Hindi Meaning"], fill="white")
    canvas.itemconfig(main_text1, text=current_card['Korean Word'], fill="white")
    canvas.itemconfig(sub_text, text=current_card['Korean Sentence'], fill="white")
    canvas.itemconfig(sub_text1, text=current_card['Hindi Sentence'], fill="white")
    canvas.itemconfig(def_text, text=current_card['Definition'], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)  # Show back image

def is_know():
    """When know button pressed, remove card from to_learn and save in known file."""
    try:
        to_learn.remove(current_card)  # Remove current card from list
    except ValueError:
        pass  # If card not in list, do nothing
    save_to_csv(current_card, known_file, known_words_dict, unknown_words_dict)  # Save card to known file
    next_card()  # Show next card

def dont_know():
    """When unknown button pressed, save card in unknown file."""
    save_to_csv(current_card, unknown_file, unknown_words_dict, known_words_dict)  # Save card to unknown file
    next_card()  # Show next card

def save_to_csv(card, filename, current_dict, other_dict):
    """Function to save single card to given file if it's not already in the file."""
    word = card['Korean Word']
    
    if word in current_dict:
        return  # If the word is already in the dictionary, do not save again

    # Save to the current file
    try:
        data = pd.read_csv(filename)  # Try reading file
        data = pd.concat([data, pd.DataFrame([card])], ignore_index=True)  # Add new card
    except FileNotFoundError:
        data = pd.DataFrame([card])  # If file does not exist, create new file
    data.to_csv(filename, index=False)  # Save updated data to file
    current_dict[word] = card  # Add word to the current dictionary

    # Check for common words and save to common file
    if word in other_dict:
        save_to_csv(card, common_file, known_words_dict | unknown_words_dict, {})  # Save to common file

window = Tk()  # Create main window
window.title('Flash Card')  # Set title of window
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # Set padding and background color

flip_timer = window.after(3000, func=flip_card)  # Timer to flip card after 3 seconds

canvas = Canvas(width=800, height=526)  # Create canvas for card
card_front_img = PhotoImage(file=image1)  # Load front card image
card_back_img = PhotoImage(file=image2)  # Load back card image
card_background = canvas.create_image(400, 263, image=card_front_img)  # Place front image on canvas
# Create text elements on canvas
main_text = canvas.create_text(400, 100, text="", font=("Ariel", 100, "normal"))
main_text1 = canvas.create_text(200, 100, text="", font=("Ariel", 60, "normal"))
main_text2 = canvas.create_text(500, 100, text="", font=("Ariel", 40, "normal"))
sub_text = canvas.create_text(400, 263, text="", font=("Ariel", 20, 'normal'))
sub_text1 = canvas.create_text(400, 310, text="", font=("Ariel", 18, "normal"))
def_text = canvas.create_text(400, 400, text="", font=("Ariel", 18, "normal"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)  # Set background color and no border
canvas.grid(row=0, column=0, columnspan=2)  # Place canvas on grid

cross_image = PhotoImage(file=image3)  # Load image for wrong button
unknown_button = Button(image=cross_image, highlightthickness=0, command=dont_know)  # Create button for unknown
unknown_button.grid(row=1, column=0)  # Place unknown button on grid

check_image = PhotoImage(file=image4)  # Load image for right button
known_button = Button(image=check_image, highlightthickness=0, command=is_know)  # Create button for known
known_button.grid(row=1, column=1)  # Place known button on grid

next_card()  # Show first card

window.mainloop()  # Run the tkinter event loop
