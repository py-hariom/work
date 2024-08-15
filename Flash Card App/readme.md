# Flash Card App

Welcome to the Flash Card App! This guide will help you get started with the app and use it effectively. This app helps you learn Korean vocabulary using flash cards.

## Overview

The app displays flash cards with Korean words and allows you to mark words as “known” or “unknown” based on your familiarity. Known words are saved in a file for review, while unknown words are stored separately. Words that appear frequently across different files are also tracked.

## Getting Started

### 1. Install the App

1. **Download and Install**: Ensure you have Python installed on your computer. Download the app's files and install the required libraries using the command:
   ```bash
   pip install pandas
   ```

2. **Prepare Your Files**: 
   - Ensure you have a file named `file.csv` in the `data` folder. The file should be formatted as follows:
     ```bash
     Korean Word,English Meaning,Hindi Meaning,Definition,Korean Sentence,Hindi Sentence
     가게,"Store, Shop","इकट्ठा करना","A place where goods are sold","가게에 물건을 사러 갑니다.","मैं दुकान से सामान खरीदने जा रहा हूँ।"
     ```
   - Make sure the `images` folder contains images named `card_front.png`, `wrong.png`, and `right.png` for card display and button actions.

### 2. Run the App

1. **Launch the App**: Run the app by executing the Python script. Open a terminal or command prompt, navigate to the directory containing the script, and run:
   ```bash
   python main.py
   ```

2. **App Window**: The app will open a window displaying a flash card. The card will show a Korean word and sentence. After a few seconds, it will flip to reveal the English and Hindi meanings.

## Using the App

### 1. Interacting with Flash Cards

- **Next Card**: The app automatically shows a new card every 3 seconds. Click the “known” or “unknown” button to manually move to the next card.

- **Known Button**: Click the button with the checkmark if you know the word. This will remove the card from the current list and save it in `known_words.csv`.

- **Unknown Button**: Click the button with the cross if you don’t know the word. This will save the card in `unknown_words.csv` for future review.

### 2. Saving and Reviewing Words

- **Known Words**: Words marked as known are saved in `known_words.csv`. You can review these words later.

- **Unknown Words**: Words marked as unknown are saved in `unknown_words.csv`. Review these to help improve your knowledge.

- **Common Words**: Words that appear in both the known and unknown lists are saved in `common.csv`.

## Troubleshooting

- **File Not Found**: If the app cannot find `file.csv`, it will start with an empty list. Ensure the file exists and is correctly formatted.

- **Images Missing**: If images are missing, the app will display default placeholders. Ensure that the `images` folder contains the required files.

- **Errors**: If you encounter any errors while running the app, check for typos in file names or paths and ensure all required files are correctly placed.

## Contact and Support

For further assistance or questions, reach out to `hariomdhakad1@gmail.com` for support.

---

Enjoy learning with your Flash Card App! Happy studying!
```
