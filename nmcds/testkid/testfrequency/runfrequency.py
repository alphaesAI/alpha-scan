import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from nmcds.kid.utils.fileloader import FileLoader
from nmcds.kid.frequency.word import WordFrequencyProcessor
from nmcds.kid.frequency.bigram import BigramFrequencyProcessor

class WordFrequencyTask:
    def run(self):
        file = input("enter file path: ")
        word = input("enter keyword to count: ")

        text = FileLoader(file).load()
        processor = WordFrequencyProcessor(text)
        print(f"total words: {processor.totalwords()}")
        print(f"'{word}' found: {processor.count(word)} times")

class BigramFrequencyTask:
    def run(self):
        file = input("enter file path: ")
        word1 = input("first word: ")
        word2 = input("second word: ")

        text = FileLoader(file).load()
        processor = BigramFrequencyProcessor(text)
        print(f"total words: {processor.total()}")
        print(f"'{word1} {word2}' appeared: {processor.count(word1, word2)} times")

if __name__ == "__main__":
    print("Choose task:\n1. Word Frequency\n2. Bigram Frequency")
    choice = input("Enter choice: ").strip()
    if choice == "1":
        WordFrequencyTask().run()
    elif choice == "2":
        BigramFrequencyTask().run()
    else:
        print("Invalid choice.")
