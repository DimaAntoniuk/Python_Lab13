
from models.Exhibit import Exhibit
from models.InterestedPeople import InterestedPeople
from models.Date import Date
from models.Topic import Topic

class Armor(Exhibit):

    def __init__(self, name="some_exhibit", portable=True,
            century_of_creation=0, country_of_creation="Italy",
            size=3, popularity=None,
            theme=None, destroyed_in_persentage=20,
            start_date_in_current_exhibition = None,
            made_of_metal = True, pattern = False):
        super().__init__(name, portable, century_of_creation,
            country_of_creation, size, popularity, theme,
            destroyed_in_persentage, start_date_in_current_exhibition)
        self.made_of_metal = made_of_metal
        self.pattern = pattern

    def __str__(self):
        return "Armor " + str(self.__dict__)
