class ExhibitManager:
    def __init__(self,  exhibit_list=None):
        self.exhibit_list=exhibit_list

    def sort_by_date_in_current_exhibition(self, reverse=True):
        return sorted(self.exhibit_list, key = lambda exhibit: exhibit.start_date_in_current_exhibition, reverse=reverse)

    def sort_by_age(self, reverse=False):
        return sorted(self.exhibit_list, key = lambda exhibit: exhibit.century_of_creation, reverse = reverse)

    def find_by_theme(self, theme):
        return list(filter(lambda exhibit: exhibit.theme==theme, self.exhibit_list))

    def print_exhibit_list_info(self):
        for exhibit in self.exhibit_list:
            print(exhibit)
        print('\n')
