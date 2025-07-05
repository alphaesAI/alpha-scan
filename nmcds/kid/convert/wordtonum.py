class WordToNumberConverter:
    def __init__(self, text: str):
        self.text = text

    def convert(self) -> dict[str, list[int]]:
        word_map = {}
        for word in self.text.strip().split():
            word_clean = word.lower().strip(".,:;!?\"'")
            if word_clean:
                word_map[word_clean] = [ord(c) for c in word_clean]
        return word_map
