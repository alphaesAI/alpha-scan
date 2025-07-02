class BigramFrequencyProcessor:
    def __init__(self, text: str):
        self.text = text.lower()
        self.words = self.text.split()
    
    def total(self) -> int:
        return len(self.words)
    
    def count(self, word1: str, word2: str) -> int:
        count = 0
        for i in range(len(self.words) - 1):
            if self.words[i] == word1.lower() and self.words[i + 1] == word2.lower():
                count += 1
        return count
    