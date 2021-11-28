class Error:

    def __init__(self, idx):
        self.idx = idx
        self.style = "style='background-color: #E89348; color: #A81818; padding: 10px; border: solid #AF6D34 4px; box-shadow: 3px 3px 3px black;"
        self.error = [
            # h* error
            '[Error]: taxable value it must be between [1, 6]'
        ]

    def returnError(self):
        return f"<p {self.style}'><strong>{self.error[self.idx]}</strong></p>"