from nmcds.kid.utils.fileloader import FileLoader
from nmcds.kid.matrix.builder import WordMatrixBuilder
from nmcds.kid.matrix.searcher import WordSearcher

class MatrixBuilderTask:
    def run(self):
        file = input("enter matrix file: ")
        text = FileLoader(file).load()
        builder = WordMatrixBuilder(text)
        builder.print_matrix()


class MatrixSearcherTask:
    def run(self):
        file = input("enter matrix file: ")
        word = input("word to search: ")

        text = FileLoader(file).load()
        matrix = WordMatrixBuilder(text).get_matrix()
        positions = WordSearcher(matrix).search_word(word)

        if positions:
            for row, col in positions:
                print(f"found '{word}' at row: {row}, col: {col}")
        else:
            print(f"'{word}' not found.")

if __name__ == "__main__":
    print("choose task:\n1. matrix builder\n2. word search")
    choice = input("enter choice: ").strip()
    if choice == "1":
        MatrixBuilderTask().run()
    elif choice == "2":
        MatrixSearcherTask().run()
    else:
        print("Invalid choice.")
