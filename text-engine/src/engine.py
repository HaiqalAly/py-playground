class EtcherEngine:
    def __init__(self):
        self.history = [] # Undo
        self.future = [] # Redo

    def add_text(self, text: str):
        self.history.append(text)
        self.future.clear()

    def undo(self):
        if self.history:
            item = self.history.pop()
            self.future.append(item)
            return self.get_state()
        return None
    
    def redo(self):
        if self.future:
            item = self.future.pop()
            self.history.append(item)
            return self.get_state()
        return None
    
    def get_state(self):
        return " ".join(self.history)