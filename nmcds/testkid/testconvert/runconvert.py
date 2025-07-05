from nmcds.kid.utils.fileloader import FileLoader
from nmcds.kid.convert.concat import WordConcatenator
from nmcds.kid.convert.wordtonum import WordToNumberConverter


class ConcatenationTask:
    def run(self):
        path = input("Enter file path: ")
        text = FileLoader(path).load()
        result = WordConcatenator(text).join_words()
        print(f"\nConcatenated result:\n{result}")


class WordToNumberTask:
    def run(self):
        path = input("Enter file path: ")
        text = FileLoader(path).load()
        result = WordToNumberConverter(text).convert()
        print("\nWord to Number Mapping:")
        for word, nums in result.items():
            print(f"{word} → {nums}")


if __name__ == "__main__":
    print("\nChoose Task:")
    print("1. Word Concatenation")
    print("2. Word to Number Conversion")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        ConcatenationTask().run()
    elif choice == "2":
        WordToNumberTask().run()
    else:
        print("❌ Invalid choice.")
