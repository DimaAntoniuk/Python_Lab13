class Date:
    def __init__(self,  day = 9, month = 4, year = 2001):
        self.day = day
        self.month = month
        self.year = year

    def __gt__(self, other):
        if(self.year<other.year):
            return True
        if(self.year<=other.year and self.month<other.month):
            return True
        if(self.year<=other.year and self.month<=other.month\
            and self.day<other.day):
            return True
        return False

    def __str__(self):
        return str(self.day) + " " + str(self.month) + " " + str(self.year)
