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

def main():
    """Creates a dictionary with the paths and runs the program."""
    script_dir = Path(__file__).parent

    files_dict = {
        "1": script_dir / "tarzan.md",
        "2": script_dir / "treasure_island.md",
        "3": script_dir / "sherlock_holmes.md",
        "4": script_dir / "the_odyssey.md"
    }
    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        print(f"1. Tarzan ({files_dict['1'].name})")
        print(f"2. Treasure Island ({files_dict['2'].name})")
        print(f"3. Sherlock Holmes ({files_dict['3'].name})")
        print(f"4. The Odyssey ({files_dict['4'].name})")
        print("5. Exit")

        user_choice = input("\nEnter your choice (1-5): ").strip()

        if user_choice == "5":
            print("\nExiting program.")
            break
        if user_choice in files_dict:
            selected_path = files_dict[user_choice]
            print(f"\nProcessing '{selected_path.name}' ...")
            analyzer = WordAnalyzer(str(selected_path))
            success = analyzer._process_file()
            if success:
                print(f"\n--- Word Frequency ---")
                analyzer.print_report()
                input("\nPress Enter to return to the menu...")
        else:
            print("\nInvalid Choice. Please select from 1-5.")

if __name__ == "__main__":
    main()