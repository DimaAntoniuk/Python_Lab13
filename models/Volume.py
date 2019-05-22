class Volume:
    def __init__(self, width=0, height=0, length=0):
        self.width = width
        self.height = height
        self.length = length

    def __str__(self):
        return str(self.width) + str(self.height) + str(self.length)
