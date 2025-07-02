class FileLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load(self) -> str:
        with open(self.filepath, "r", encoding="utf-8") as f:
            return f.read()