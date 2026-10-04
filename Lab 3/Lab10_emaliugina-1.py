"""Name: Lab10_emaliugina-1.py
   Author: Elizaveta Maliugina
   Purpose: Lab 3 for CSCI 1511. Displays a menu of 4 predefined text files, lets the user choose one, then reads and analyzes that file. The program will count the frequency of every word in the selected file and print an alphabetical report.
   Date: 10/03/2026"""

from pathlib import Path
import string

class WordAnalyzer:
    """Creates the Word Analyzer that checks if the file exists and returns false if it doesn't. If the file exists, it formats, translates, and sorts the text to display the words and the number of their instances."""
    def __init__(self, filepath:str):
        self._filepath = Path(filepath)
        self._frequencies = {}

    def _process_file(self) -> bool:
        try:
            if not self._filepath.exists():
                raise FileNotFoundError
            with self._filepath.open('r', encoding='utf-8') as file:
                translator = str.maketrans('','', string.punctuation)
                for line in file:
                    lowercase_line = line.lower()
                    clean_line = lowercase_line.translate(translator)
                    words = clean_line.split()
                    for word in words:
                        self._frequencies[word] = self._frequencies.get(word,0) + 1
            return True
        except FileNotFoundError:
            return False

    def print_report(self):
        sorted_words = sorted(self._frequencies.keys())
        for word in sorted_words:
            print(f"{word:<7} :: {self._frequencies[word]}")
