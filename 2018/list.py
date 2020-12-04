class List():
    def __init__(self, file):
        self.fileName = file
        self.list = []

    def load(self):
        with open(self.fileName) as input:
            self.data = input.read().splitlines()

    def __str__(self):
        output = []
        for item in self.list:
            output.append(f"{item}")
        return str(output)
