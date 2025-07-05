class WordConcatenator:
    def __init__(self, text: str):
        self.text = text

    def join_words(self) -> str:
        words = self.text.lower().split()
        return "".join(words)
