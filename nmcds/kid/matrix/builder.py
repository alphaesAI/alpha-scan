class WordMatrixBuilder:
    def __init__(self, text: str):
        self.text = text
        self.matrix = self._build_matrix()

    def _build_matrix(self) -> list[list[str]]:
        lines = self.text.strip().split('\n')
        return [line.strip().split() for line in lines if line.strip()]
    
    def get_matrix(self) -> list[list[str]]:
        return self.matrix
    
    def print_matrix(self):
        print("\n Matrix:")
        for row in self.matrix:
            print("   " + " | ".join(row))