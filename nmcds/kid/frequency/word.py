class WordFrequencyProcessor:
    def __init__(self, text: str):
        self.text = text.lower()
        self.words = self.text.split()

    def totalwords(self) -> int:
        return len(self.words)
    
    def count(self, keyword: str) -> int:
        return self.words.count(keyword.lower())