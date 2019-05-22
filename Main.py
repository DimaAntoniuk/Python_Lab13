from models.Exhibit import Exhibit
from models.Armor import Armor
from models.Vase import Vase
from models.Crown import Crown
from models.Painting import Painting
from models.Topic import Topic
from managers.ExhibitManager import ExhibitManager
from models.Date import Date

def main():
    armor = Armor(start_date_in_current_exhibition = Date(1, 1, 2001))
    vase = Vase(start_date_in_current_exhibition = Date(2, 1, 2003))
    crown = Crown(start_date_in_current_exhibition = Date(5, 3, 2007))
    painting = Painting(start_date_in_current_exhibition = Date(6, 9, 2011))

    list_of_exhibits = [painting, vase, crown, armor]
    manager = ExhibitManager(list_of_exhibits)

    manager.find_by_theme(Topic.ANCIENT_ROME)
    manager.print_exhibit_list_info()
    manager.sort_by_age()
    manager.print_exhibit_list_info()
    manager.sort_by_date_in_current_exhibition()
    manager.print_exhibit_list_info()
