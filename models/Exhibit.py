from models.Date import Date
from models.Topic import Topic
from models.InterestedPeople import InterestedPeople

class Exhibit():

    def __init__(self, name="some_exhibit", portable=True,
            century_of_creation=0, country_of_creation="Italy",
            size=3, popularity=None,
            theme=None, destroyed_in_persentage=20,
            start_date_in_current_exhibition = None):
        self.name = name
        self.portable = portable
        self.century_of_creation = century_of_creation
        self.country_of_creation = country_of_creation
        self.size = size
        self.popularity = popularity
        self.theme = theme
        self.destroyed_in_persentage = destroyed_in_persentage
        self.start_date_in_current_exhibition = start_date_in_current_exhibition

    def __del__(self):
        print("Destructor was called")

    def __str__(self):
        return  str(self.__dict__)
